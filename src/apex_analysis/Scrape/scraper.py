"""this python file is for scrape for Apex analysis"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


class Scraper:
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
        pattern = r"(.+?)(\d.?.?)%(.+)%Avg rank\s(.+)\s\|\slevel\s(\d+)"

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
                    "Legend": legend_name,
                    "Pick Rate": pick_rate,
                    "Change": change_rate,
                    "Avg Rank": avg_rank,
                    "Avg Level": avg_level,
                }
                legend_list.append(result_dict)  # Append the dictionary to the list

        df = pd.DataFrame(legend_list)
        df_fixed = self.correct_legend(df)
        return df_fixed  # Return the list of dictionaries containing legend information

    def correct_legend(self, df):
        """
        Corrects data types and formats in the DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.

        Returns:
            pd.DataFrame: DataFrame with corrected data types and formats.
        """
        df["Pick Rate"] = df["Pick Rate"].str.rstrip("%").astype(float)
        df["Avg Level"] = df["Avg Level"].astype(int)
        # Convert 'Change' to integer, considering ▲ as positive and ▼ as negative
        df["Change"] = (
            df["Change"]
            .str.replace("▲", "")
            .str.replace("▼", "-")
            .str.rstrip("%")
            .astype(float)
        )

        # Map 'Avg Rank' to a rank order dictionary
        rank_order = {
            "Rookie 4": 0,
            "Rookie 3": 1,
            "Rookie 2": 2,
            "Rookie 1": 3,
            "Bronze 4": 4,
            "Bronze 3": 5,
            "Bronze 2": 6,
            "Bronze 1": 7,  # Assuming there is a Bronze 1 level
        }
        df["Avg Rank"] = df["Avg Rank"].map(rank_order)
        df = df.sort_values(by="Avg Rank")
        return df
