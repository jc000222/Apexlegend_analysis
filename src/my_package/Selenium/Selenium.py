from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Account_progress:
    def __init__(self,lv,Purchased_packs,play_since):
        self.lv=lv
        self.pp=Purchased_packs
        self.ps=play_since
    def use_selenium(self):

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # Initialize the WebDriver with the specified options
        driver = webdriver.Chrome(options=chrome_options)

        # Open a website
        driver.get('https://apexlegendsstatus.com/apex-pack-calculator')  # Replace with the URL of the website

        # Close a window
        butt = driver.find_element(By.ID, 'FirstDismiss')
        butt.click()
        time.sleep(1)

        #lv
        input_lv = driver.find_element(By.ID, 'account_level-9999-AccountLevel')  # Replace with the actual ID of the input field
        input_lv.clear()
        input_lv.send_keys(self.lv)
        time.sleep(1)
        #Purchased_packs
        input_pp = driver.find_element(By.ID, 'purchased-9999-Purchasedpacks')  # Replace with the actual ID of the input field
        input_pp.clear()
        input_pp.send_keys(self.pp)
        time.sleep(1)
        #seasons
        for i in range(int(self.ps),19):
            input_seasons = driver.find_element(By.ID, f'battlepass-{i}-Season{i}Battlepass')  # Replace with the actual ID of the input field
            input_seasons.clear()
            input_seasons.send_keys(110)  # Replace with the max level
            time.sleep(1)
            checkbox = driver.find_element(By.ID, f'battlepass-{i}-Season{i}Battlepass_bp')
            if not checkbox.is_selected():
                checkbox.click()
                time.sleep(1)


        t = driver.find_element(By.ID, 'packProgressBar')
        return t.text
