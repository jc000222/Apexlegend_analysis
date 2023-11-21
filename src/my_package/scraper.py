import requests 
from bs4 import BeautifulSoup
import pandas as pd
import re

class Scrape:
    def __init__(self, url):
        """
        Initialize Scrape class.

        Args:
            url (str): The URL of the webpage to be scraped.
        """
        self.url = url
        self.soup = self.html2soup()

    def test_html(self):
        """
        Test HTML content.

        Returns:
            bytes: The content of the HTML page if the request is successful, None otherwise.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content

    def html2soup(self):
        """
        Convert HTML content to BeautifulSoup object.

        Returns:
            BeautifulSoup object: The parsed HTML content as a BeautifulSoup object if the request is successful, None otherwise.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup
        else:
            print(f"Failed to fetch {self.url}")
            return None
        
    def get_df(self):
        """
        Extract legend information and create a DataFrame.

        Returns:
            pandas.DataFrame: DataFrame containing legend information (Legend, Pick Rate, Change, Avg Rank, Avg Level).
        """
        # To extract the first and last page numbers
        legends = self.soup.find_all("div", {"class": "legends-banner__content"})
        legend_list = []  # Initialize a list to store dictionaries for each legend
        pattern = r'(.+?)(\d.?.?)%(.+)%Avg rank\s(.+)\s\|\slevel\s(\d+)'
        
        for legend in legends:
            matches = re.match(pattern, legend.text.strip())

            # Creating a dictionary based on extracted groups
            if matches:
                legend_name = matches.group(1)
                pick_rate = f"{matches.group(2)}%"
                change_rate = f"{matches.group(3)}%"
                avg_rank = matches.group(4)
                avg_level = matches.group(5)

                result_dict = {
                    'Legend': legend_name,
                    'Pick Rate': pick_rate,
                    'Change': change_rate,
                    'Avg Rank': avg_rank,
                    'Avg Level': avg_level
                }
                legend_list.append(result_dict)  # Append the dictionary to the list

        df = pd.DataFrame(legend_list)
        return df  # Return the list of dictionaries containing legend information


scrape_webpage = 'https://apexlegendsstatus.com/game-stats/legends-pick-rates'
scraper = Scrape(scrape_webpage)
scraper.get_df()
