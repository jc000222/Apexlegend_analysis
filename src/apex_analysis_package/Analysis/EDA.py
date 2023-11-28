"""this python file is for eda for Apex analysis"""
import pandas as pd
import matplotlib.pyplot as plt
import random


class Analysis:
    def __init__(self, df1, df2):
        """
        Initializes the Analysis class with two dataframes.

        Args:
        df1(pd.DataFrame): Input DataFrame df_player.
        df2(pd.DataFrame): Input DataFrame df_legend.
        """
        self.df_player = df1
        self.df_legend = df2

    def random_color(self):
        """
        Returns a randomly generated color in hexadecimal format.

        Returns:
            str: Hexadecimal color string.
        """
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def run_analysis(self, which_dataframe):
        """
        Plot bar charts for each column in the DataFrame.

        Args:
            which_dataframe (str): Input which DataFrame being used.
        """
        if which_dataframe == "df_player":
            df = self.df_player
        if which_dataframe == "df_legend":
            df = self.df_legend

        fig, axes = plt.subplots(nrows=1, ncols=len(df.columns[1:]), figsize=(15, 5))

        for i, col in enumerate(df.columns[1:]):
            axes[i].bar(df["Legend"], df[col], color=self.random_color())
            axes[i].set_ylabel(col)
            axes[i].set_title(col)
            axes[i].tick_params(axis="x", rotation=60)

        plt.tight_layout()
        plt.show()

    def per_game(self):
        """
        Plot bar charts in the DataFrame for df_player.
        """
        df = self.df_player
        df["Kills_per_game"] = df["kills"] / df["Games_played"]
        df["Damage_per_game"] = df["Damage"] / df["Games_played"]

        # Plotting
        plt.figure(figsize=(10, 6))

        plt.subplot(121)
        plt.bar(df["Legend"], df["Kills_per_game"], color=self.random_color())
        plt.xlabel("Legend")
        plt.ylabel("Kills per Games Played")
        plt.title("Kills per Games Played")
        plt.xticks(rotation=45)

        plt.subplot(122)
        plt.bar(df["Legend"], df["Damage_per_game"], color=self.random_color())
        plt.xlabel("Legend")
        plt.ylabel("Damage per Games Played")
        plt.title("Damage per Games Played")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()
