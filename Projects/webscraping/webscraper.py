'''
This is a docstring for the module
'''
import os
import selenium
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager #installs Chrome webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import boto3
from sqlalchemy import create_engine
import urllib.request
import tempfile #temporary directory - to be removed after all operations have finished

class Scraper:
    '''
    This class is a scraper that can be used to browse different websites

    Parameters:
    url: str
        Link we want to visit
    --------------
    Attributes:
    driver:
        Webdriver object

    '''

    #load webpage in initialiser
    def __init__(self, url: str = "https://store.eu.square-enix-games.com/en_GB/"): #default url
        self.driver = Chrome(ChromeDriverManager().install()) 
        try:
            self.driver.get(url)
            #driver = Chrome() #specify location of chromedriver if downloading webdriver
            print("Webpage loaded successfully")
        except NoSuchElementException:
            print("Webpage not loaded - please check")

        self.driver.maximize_window() #maximise window upon loading webpage

        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2' #database API - API to connect Python with database
        #use AWS details to connect database
        HOST = os.environ.get('DB_HOST') #endpoint
        USER = os.environ.get('DB_USER')
        PASSWORD = os.environ.get('DB_PASS')
        DATABASE = 'postgres'
        PORT = 5432

        self.engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
        self.client = boto3.client('s3')

        self.bucket = os.environ.get('DB_BUCKET')

    #click accept cookies button on webpage
    def accept_cookies(self, xpath: str = '//*[@id="onetrust-accept-btn-handler"]'): 
        '''
        Looks for and clicks on the accept cookies button

        Parameters:
        ---------
        xpath: str
            The xpath of the accept cookies button

        '''
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            time.sleep(5)
            self.driver.find_element(By.XPATH, xpath).click()
            print("'Accept Cookies' button clicked")
        except TimeoutException: #if accept button is not found after 10 seconds by driver
            print("No cookies found") 
        
        return None

    #access and type in search bar
    def search_bar(self, text, xpath: str = './/a[@id="search-button"]', 
                    xpath1: str = '//*[@id="search-form-wrapper"]/form/div/input',
                    xpath2: str = './/button[@class="btn search-button-submit"]'): 
        
        '''
        Look for and write something in search bar

        Parameters
        ----------
        xpath: str
            xpath for the search button - opens search bar

        xpath1: str
            xpath for search bar - allows keywords to be be input
        
        xpath2: str
            xpath for search button to submit keywords - forward to result page

        text: str
            text to be passed to search bar

        '''
        #click on search bar icon
        try:
            time.sleep(1)
            (WebDriverWait(self.driver, 5)
                .until(EC.presence_of_element_located((By.XPATH, xpath))))
            self.driver.find_element(By.XPATH, xpath).click()
            print("Search bar opened")
        except TimeoutException:
            print("Search bar not found")
        
        #open search bar
        try:
            time.sleep(1)
            (WebDriverWait(self.driver, 5)
                .until(EC.presence_of_element_located((By.XPATH, xpath1))))
            time.sleep(2)
            self.driver.find_element(By.XPATH, xpath1).click()
        except TimeoutException:
            print("Search bar not found - input")
        
        #input keywords to search
        try:
            self.search = self.driver.find_element(By.XPATH, xpath1)
            self.search.send_keys(text)
            print("Search keywords entered")
            time.sleep(2)
        except NoSuchElementException:
            print("Cannot input keywords")
        
        #submit input
        try:
            self.search = self.driver.find_element(By.XPATH, xpath2).click()
            print("Submit search button clicked - redirected to results")
            time.sleep(2)
        except NoSuchElementException:
            print("Cannot submit search")

        return text #output to be returned from function
        
    #navigate tabs - change id for games, merchandise or preorders
    def navigate(self, xpath: str = '//*[@id="merchandise"]'): 
        '''
        This is to navigate the site using the navigation bar

        Parameters
        -------------
        xpath: str
            xpath to identify desired tab on navigation bar
        '''
        
        self.tab_select = self.driver.find_element(By.XPATH,xpath)
        time.sleep(2)
        self.tab_select.click()
        time.sleep(2)

        return None
        
    
    def find_container(self, xpath: str = '//div[@class="catalogue row"]'):
        '''
        This is to find the container with the search results so the links can be accessed 
        for data scraping

        Parameters
        -------
        xpath: str
            locate the results container
        '''
        #### Following code block will only scroll through results page once ####
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        return self.driver.find_element(By.XPATH, xpath)
    
    def collect_page_links(self, xpath : str = ".//a"):
        '''
        This is to find links in the search results container 
        Parameters
        -------
        xpath: str
            locate the links in the results container
        '''
        self.container = self.find_container()
        #find many elements that correspond with the XPath - they have to be direct children of the container
        #i.e. one level below the container
        time.sleep(5)
        self.driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight);") #scroll straight to bottom of page
        time.sleep(5)
        self.list_products = self.container.find_elements(By.XPATH, xpath)
        self.link_list = []
        for product in self.list_products: #iterate through each product
            #print(product.text) #print each product in text format
            self.link_list.append(product.get_attribute("href"))
        
        return self.link_list
    
    def find_images(self, container, xpath : str = '//figure[@class="product-boxshot-container"]'):
        #//figure[@class="product-boxshot-container hover-boxshot"]
        '''
        This is to find the product images in the search results container 
        Parameters
        -------
        xpath: str
            locate the images in the results container and their respective links from srcset
        '''
        list_div = container.find_elements(By.XPATH, '//img[@class="product-boxshot lazyloaded"]')
        src_list = []
        for product in list_div:
            image_container = product.find_element(By.XPATH, xpath)
            src = image_container.find_element(By.XPATH, './/img').get_attribute('srcset')
            r = src.split("1x") #split src as srcset contains two links by default
            src_list.append(r[0]) #obtain image from 1st link only
        return src_list
    
    def upload_images(self, src):
        '''
        This is to save images to a temporary directory and upload them to the s3 bucket 
        Parameters
        -------
        src: str
            product image links obtained in find_images()
        '''
        with tempfile.TemporaryDirectory() as tmpdirname:
            for i in range(len(src)):
                urllib.request.urlretrieve(src[i], tmpdirname + f'/image_{i}.png')
                self.client.upload_file(tmpdirname + f'/image_{i}.png', self.bucket, f'image_{i}.png')
        #//img[@class = "product-boxshot secondary-boxshot lazyloaded"]
    
    

if __name__ == "__main__": #will only run methods below if script is run directly
    scraper = Scraper() #call scraper class
    scraper.accept_cookies()
    scraper.navigate()
    scraper.search_bar('final fantasy') #add search keyword here
    