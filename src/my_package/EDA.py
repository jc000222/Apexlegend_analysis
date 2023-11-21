import pandas as pd
import matplotlib.pyplot as plt
import random

class Analysis:
    def __init__(self) -> None:
        pass

    def random_color(self):
        """
        Returns a randomly generated color in hexadecimal format.

        Returns:
            str: Hexadecimal color string.
        """
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def run_analysis(self, df):
        """
        Plot bar charts for each column in the DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.
        """
        fig, axes = plt.subplots(nrows=1, ncols=len(df.columns[1:]), figsize=(15, 5))

        for i, col in enumerate(df.columns[1:]):
            axes[i].bar(df['Legend'], df[col], color=self.random_color())
            axes[i].set_ylabel(col)
            axes[i].set_title(col)
            axes[i].tick_params(axis='x', rotation=60)

        plt.tight_layout()
        plt.show()

    def correct_legend(self, df):
        """
        Corrects data types and formats in the DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.

        Returns:
            pd.DataFrame: DataFrame with corrected data types and formats.
        """
        df['Pick Rate'] = df['Pick Rate'].str.rstrip('%').astype(float)
        df['Avg Level'] = df['Avg Level'].astype(int)
        # Convert 'Change' to integer, considering ▲ as positive and ▼ as negative
        df['Change'] = df['Change'].str.replace('▲', '').str.replace('▼', '-').str.rstrip('%').astype(float)

        # Map 'Avg Rank' to a rank order dictionary
        rank_order = {
            'Rookie 4': 0,
            'Rookie 3': 1,
            'Rookie 2': 2,
            'Rookie 1': 3,
            'Bronze 4': 4,
            'Bronze 3': 5,
            'Bronze 2': 6,
            'Bronze 1': 7  # Assuming there is a Bronze 1 level
        }
        df['Avg Rank'] = df['Avg Rank'].map(rank_order)
        df = df.sort_values(by='Avg Rank')
        return df
