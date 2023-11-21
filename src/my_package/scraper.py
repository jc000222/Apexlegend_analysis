import requests 
from bs4 import BeautifulSoup
import pandas
import re
class Scrap:
    def __init__(self,url):
        self.url = url
        self.soup = self.html2soup()
    def test_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
    def html2soup(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
            return soup
        else:
            print("Failed to fetch {self.url}")
            return None
        
    def get_df(self):
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
                df = pandas.DataFrame(legend_list)

        return df  # Return the list of dictionaries containing legend information
