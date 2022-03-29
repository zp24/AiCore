import unittest
from webscraper import Scraper 

#make sure the method to be tested contains a return function

class TestScraper(unittest.TestCase): #gives access to testing capabilities within class
    def setUp(self):
        self.scraper = Scraper() #navigate to url
    '''
    def test_searchbar(self):
        text = "kingdom hearts"
        result = self.scraper.search_bar(text)
        self.assertIn(result, 'kingdom hearts') #strings must match for test to run successfully
    
    def test_navigate(self):
        id = '//*[@id="merchandise"]'
        result = self.scraper.navigate(id)
        self.assertIsNone(result, '//*[@id="merchandise"]') #returns None

    def test_accept_cookies(self):
        cookie_id = '//*[@id="onetrust-accept-btn-handler"]'
        result = self.scraper.accept_cookies(cookie_id)
        self.assertIsNone(result, '//*[@id="onetrust-accept-btn-handler"]') #returns None
    '''
    def test_find_container(self):
        text = "final fantasy"
        self.scraper.search_bar(text)
        container = self.scraper.find_container()
        #//*[@id="slick-slide03"]/a
        result = container.text[0:18]
        self.assertIn(result, "FINAL FANTASY VIII - REMASTERED") #assertEqual will return FAILED test
        
    #def test_find_links(self):
     #   link = './/a'
      #  result = self.scraper.collect_page_links(link)
       # self.assertIn(result, './/a') #strings must match for test to run successfully
        #get_attribute("href")

        
        
if __name__ == '__main__':
    unittest.main()

#python -m unittest test_scraper.py
'''
My Blueprint to running a successful Unittest: 

1. Tell your scraper to go to a target page 
2. Run your method on the page 
3. Make an assertion based on what your method in your class returns.

'''