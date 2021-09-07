"""

Task 2: scraping the “site” command (optional)

"""

# -*- coding: utf-8 -*-

from googlesearch import search
from serpapi import GoogleSearch
import pandas as pd

""" 
Created on Thur. Sep. 02 11:30:00 2021

@author: rafalwilk4ti1

"""

""" The risk of using this program is enormous. Web scraping can simply
    overload a server with large numbers of automated requests. Thus we 
    should always check the API documentation and ensure the traffic load
    is reasonable.The worst scenario we can expect is Google disallows
    automated access in their Terms of Service and might block your IP
    address in case of violation. 
"""


class ScrappingTheSiteCommand:

    """ Initialing variables
        file_name -  is given by user because it's file name,
        keyword_list - is finally result of the keywords from the file,
        site is given - top-down address url,
        modified_url - is the url which we use to check if the retrieved
                       addresses contain our phrase
        counter - keep the appropriate index, when it comes to return
                    correct keyword
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.keywords_list = []
        self.site = 'site:https://www.searchenginejournal.com/'
        self.modified_url = self.site.replace('site:', '')
        self.counter = 0
        self.counter_2 = 0

    def loop_through_file(self) -> None:
        """
         Function loops through the file with keywords
         and append each word to the list Return nothing.
        """
        with open(self.file_name, 'r') as file_1:
            for line in file_1:
                self.keywords_list.append(line.strip('\n'))

    def google_search(self, number_of_pages=1) -> list:
        """
            Function gets next element from the list which will be concatenated
            to query, to make request from google search result.
            Using parameter "number_of_pages" we can adjust the number of pages
            The result of links of one page is in mostly cases equal to 10, so
            by multiple the num and stop by 10 we can decide which page we
            want to check. The parameter must be int. Returns list of url.
        """

        url_list = []
        query = self.site + '  ' + self.keywords_list[self.counter]
        search_result = search(query, tld='com', lang='pl', num=number_of_pages*10,
                               start=0, stop=number_of_pages*10,  pause=1)
        for url in search_result:
            if self.modified_url in url:
                url_list.append(url)
        return list(url_list)

    def total_number_of_results(self) -> str:
        """
        The function is responsible for taking next elem
        from keywords_list, and looking for the number of total
        results which we get using GoogleSearch from serpapi
        libraries. The we convert into dict type, and get
        access to the interesting content. Returns the number
        of search result.

        By free subscription we can get api_key, that
        enable us get the json file(we convert to dict type)
        where we can find wanted number of results, and due to
        the fact it's free it is very slow and limited 100
        searches per months.

        """

        next_elem = self.keywords_list[self.counter]
        url = self.site + ' ' + next_elem
        params = {
            'engine': 'google',
            'q': url,
            'api_key': 'd95a98e4bdd58352d7d8a085865b57d6e3932f8c706db2d1073ace82e04aed60'
        }
        google_search = GoogleSearch(params)
        results = google_search.get_dict()
        total_result = results["search_information"]["total_results"]
        return total_result

    def preparing_url_results(self) -> dict:
        """
            Creating dictionary where we'll save each keyword
            as a key and list of results as a value. Make
            iteration keywords_list, set as a key, addition
            url_list using results from google_search() function.
        """
        self.counter = 0
        url_dict = dict()
        for _ in self.keywords_list:
            url_list = self.google_search()
            url_dict[self.keywords_list[self.counter]] = url_list
            self.counter += 1
        return url_dict

    @staticmethod
    def save_file_to_csv(link_frame=dict) -> None:
        """
            Create new csv file where we insert
            created data frame using pandas libraries,
            the parameter must be dictionary.
        """
        df = pd.DataFrame(link_frame)
        with open('urls_results.csv', 'a') as csv_file:
            df.to_csv(csv_file, encoding='utf-8', index=False)

    def preparing_total_results_csv(self) -> dict:
        """
            Prepare data to save. Using self.count we can
            be in charge of which word will be add.
            Each word and result is insert into dict, and
            return to be simply saved in csv later.
        """
        self.counter = 0
        total_result_dict = dict()
        for _ in self.keywords_list:
            total_result = self.total_number_of_results()
            total_result_dict[self.keywords_list[self.counter]] = total_result
            self.counter += 1
        return total_result_dict

    @staticmethod
    def save_total_results_to_csv(total_results: dict) -> None:
        """
            Saving results into csv file
        """
        db = pd.DataFrame([total_results])
        with open('total_results.csv', 'a') as csv_file:
            db.to_csv(csv_file, encoding='utf-8', index=False)


# Creating object with name of file we are about to loop through
scrape_object = ScrappingTheSiteCommand('example_keywords.txt')
# Loop through the object to append keywords in the list
scrape_object.loop_through_file()

##################################################################################
# Search results in google
scrape_object.google_search()
# Preparing urls result
prepared_urls_result = scrape_object.preparing_url_results()

################################################################################

# Save url results in new csv file
ScrappingTheSiteCommand.save_file_to_csv(prepared_urls_result)
# Prepare total results
prepared_total_results = scrape_object.preparing_total_results_csv()
# Save total results in the new csv
ScrappingTheSiteCommand.save_total_results_to_csv(prepared_total_results)
