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

The data was easily stored in their respective dictionaries, but there were a few issues encountered when it came to writing up code to create a new folder and data dumping in the required json file that also needed to be created in the new folder. The first part was relatively simple, but to create the file in the desired folder required another line or two of code before this worked (the same applied with adding any downloaded images to the desired folder), otherwise the file was created in the current working directory instead. For the images, the code was amended so that any images downloaded at an earlier part in the script were simply moved to the desired folder.

Additional code was also required to be able to dump the UUID numbers into the json file. Fortunately the code was readily available on StackOverflow, so it was copied and pasted in.

The code was reviewed and modified where possible, before the Scraper class was moved to a .py file and imported into the newly created .ipynb (original script has been retained just in case older code is required).

Milestone 4

This milestone was comprised of documenting and testing the webscraper to help understand what each method in the Scraper class was for, their parameters and what would be returned, and to test each method in a separate script to ensure everything was working properly.

Documenting was relatively simple, but the difficulty experienced during this milestone came from unit testing; given that each method was essentially being tested anyway in the relevant script(s), it was hard to understand why testing would also be required, otherwise it was quite straightforward to create tests for the public methods to check they were working properly.

Although all the tests are passing, they can be improved in some parts.

The Scraper class was also modified to include the method that would add links to a list (to be iterated through in the webpage (Square Enix) script); this was a sensible step to take given links would be accessed for any website from which data would be scraped, thereby completely separating all the generic methods from the custom methods.
