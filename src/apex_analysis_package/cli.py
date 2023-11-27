"""Run Apex analysis CLI for part 1 to part 4 """
from src.apex_analysis_package.XML.xml_related import XmlLoad
from src.apex_analysis_package.API.api_related import ApiProcess
from src.apex_analysis_package.Scrape.scraper import Scrape
from src.apex_analysis_package.Analysis.EDA import Analysis
from src.apex_analysis_package.Selenium.Selenium import Account_progress
from src import auth


def main():
    """
    Run Apex analysis as a script. Choose which part to run.
    """
    print(
        "APEX Legend Analysis:-Project 2 (M9): Working with Web Data\nAuthor: Ruoyu Chen\nGithub Repository: https://github.com/jc000222/Apexlegend_analysis"
    )

    while True:
        print("-----------------------------------")
        print(
            "(1)Part 1: XML Parsing\n(2)Part 2: Using an API\n(3)Part 3: Web Scraping\n(4)Part 4: Analyze dataset"
        )
        print("(5)Extra: Selenium\n(0)Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            part1()
        elif choice == "2":
            part2()
        elif choice == "3":
            part3()
        elif choice == "4":
            part4()
        elif choice == "5":
            Selenium()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def part1():
    website = "https://apexlegendsstatus.com"
    xml_parse = XmlLoad(website)
    print(
        "Take a look at the robot.txt file to see if it has sitemaps.From the result, 'apexlegendsstatus.com' allows scraping all webpages and provide one Sitemap.\n",
        xml_parse.robotstxt,
    )
    xml_parse.get_sitemap()
    dataframes = xml_parse.get_sitemap_df()
    print(dataframes[0])


def part2():
    player_name = "nndkale"
    platform = "PC"
    loader = ApiProcess(auth.auth_key(), player_name, platform)
    player_name = "nndkale"
    uid = loader.get_uid(player_name)
    print("uid of the player is:", uid)
    df_player = loader.get_data(uid)
    print(df_player)
    return df_player


def part3():
    scrape_webpage = "https://apexlegendsstatus.com/game-stats/legends-pick-rates"
    scraper = Scrape(scrape_webpage)
    df_legend = scraper.get_df()
    print(df_legend)
    return df_legend


def part4():
    runner = Analysis(part2(), part3())
    runner.run_analysis("df_player")
    runner.per_game()
    runner.run_analysis("df_legend")


def Selenium():
    account_level = "100"
    Purchased_packs = "180"
    play_since_season = "17"

    dyn_scraper = Account_progress(account_level, Purchased_packs, play_since_season)
    print(dyn_scraper.use_selenium())
