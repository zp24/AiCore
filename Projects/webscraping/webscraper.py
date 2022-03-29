'''
This is a docstring for the module
'''

import selenium
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager #installs Chrome webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

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

        self.driver.maximize_window() #maximise window upon loading

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

        return self.driver.find_element(By.XPATH, xpath)
    
    def collect_page_links(self, xpath : str = ".//a"):
        self.container = self.find_container()
        #find many elements that correspond with the XPath - they have to be direct children of the container
        #i.e. one level below the container
        self.list_products = self.container.find_elements(By.XPATH, xpath)
        self.link_list = []
        for product in self.list_products: #iterate through each product
            #print(product.text) #print each product in text format
            self.link_list.append(product.get_attribute("href"))
        
        return self.link_list

if __name__ == "__main__": #will only run methods below if script is run directly
    scraper = Scraper() #call scraper class
    scraper.accept_cookies()
    scraper.navigate()
    scraper.search_bar("final fantasy") #add search keyword here
    