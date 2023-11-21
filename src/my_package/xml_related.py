import requests
from bs4 import BeautifulSoup
import pandas as pd
class xml_load:
    def __init__(self,url):
        self.url = url
        self.robotstxt = self.get_robotstxt()
    def get_robotstxt(self,new_url=None):
        '''
        '''
        robots_url = self.url+"/robots.txt"

        if new_url is not None:
            robots_url=new_url+"/robots.txt"

        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch robots.txt")
            return None
    def get_sitemap(self,new_url=None):
        sitemap_urls=[]
        lines = self.robotstxt.split('\n')

        if new_url is not None:
            lines = self.get_robotstxt(new_url).split('\n')
        
        # Parsing robots.txt to extract sitemap directives
        for line in lines:
            if line.lower().startswith('sitemap:'):
                sitemap_url = line.split(':', 1)[1].strip()
                sitemap_urls.append(sitemap_url)
                if sitemap_urls == []:
                    print("No sitemaps found")
                    return None
                return sitemap_urls

    def sitemap2df(self,sitemap_url):
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'xml')  # Parse XML content with Beautiful Soup
            # Extract data from XML elements and append to lists
            urls = [loc.text for loc in soup.find_all('loc')]
            last_mod = [lastmod.text for lastmod in soup.find_all('lastmod')] if soup.find_all('lastmod') else ['N/A'] * len(urls)
            prior = [prior.text for prior in soup.find_all('priority')]
            # Create a DataFrame from extracted data
            df = pd.DataFrame({'URL': urls, 'Last Modified': last_mod, 'priority': prior})
            return df

    def get_sitemap_df(self):
        sitemaps = self.get_sitemap()
        dataframes=[]
        for sm in sitemaps:
            dataframes.append(self.sitemap2df(sm))
        return dataframes

