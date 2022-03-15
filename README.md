# New_Repo

Webscraping Project

Milestone 1

Square Enix store was chosen as I am familiar with the site and the company.

Milestone 2

A Scraper class was created to access a site, click on the accept cookies button, and includes a few methods for standard navigation around a site (e.g. clicking on tabs and adding keywords to the search bar.
There were some issues in accessing the "accept cookies" button in terms of checking if the button was within another frame, locating the proper Xpath and clicking on the button, but these were eventually rectified.
Once the methods were added and tested, if __name__ == "__main__" block was added to initialise the class only if the script was run directly.

Milestone 3

This milestone was quite complex yet interesting. Whilst it was relatively straightforward to iterate through the specified number of links, issues arose and were resolved (partially if not fully) when it came to scraping specific data from each page, such as the product name, price, description and images. The first and last pieces of data seem to have a lower success rate in being scraped, but this may be dependent on the size of the window the webpage is in (which could have an effect on the xpath copied as found in a demo), although the xpaths remained the same for these regardless of size.

The data was easily stored in their respective dictionaries, but there were a few issues encountered when it came to writing up code to create a new folder and data dumping in the required json file. The first part was relatively simple, but to create the folder in the desired file required another line or two of code before this worked (the same applied with adding any downloaded images to the desired folder), otherwise the file was created in the current working directory instead. 

Additional code was also required to be able to dump the UUID numbers into the json file.

The code was reviewed and modified where possible, before the Scraper class was moved to a .py file and imported into the newly created .ipynb (original script has been retained just in case older code is required).
