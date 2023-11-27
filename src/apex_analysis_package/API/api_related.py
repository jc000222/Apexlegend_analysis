import requests
import json
import pandas as pd
import numpy
from requests.exceptions import HTTPError


class ApiProcess:
    def __init__(self, auth, player, pf):
        """
        Initializes the ApiProcess class with authentication, player, and platform information.

        Args:
        auth (str): Authentication key.
        player (str): Player name.
        pf (str): Platform information.
        """
        self.auth = auth
        self.player = player
        self.pf = pf
        self.url = f"https://api.mozambiquehe.re/nametouid?auth={self.auth}"

    def get_uid(self, player=None, pf=None):
        """
        Gets the UID based on the player and platform.

        Args:
        player (str, optional): Player name. Defaults to None.
        pf (str, optional): Platform information. Defaults to None.

        Returns:
        str: UID value.
        """
        url = self.url
        if player is not None:
            url += f"&player={player}"
        else:
            url += f"&player={self.player}"
        if pf is not None:
            url += f"&platform={pf}"
        else:
            url += f"&platform={self.pf}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                uid_value = data["uid"]
                return uid_value
        except HTTPError as e:
            print(f"HTTP error while getting uid: {e}")
        except Exception as e:
            print(f"An error occurred while getting uid: {e}")

    def get_data(self, uid, pf=None):
        """
        Gets the data for a specific UID and platform.

        Args:
        uid (str): User ID.
        pf (str, optional): Platform information. Defaults to None.

        Returns:
        pandas.DataFrame: DataFrame containing legend information.
        """
        url = f"https://api.mozambiquehe.re/bridge?auth={self.auth}&uid={uid}"
        if pf is not None:
            url += f"&platform={pf}"
        else:
            url += f"&platform={self.pf}"
        try:
            response = requests.get(url)
            if response.ok:
                data = response.json()
                my_legends_data = data["legends"]["all"]
                df = pd.DataFrame(my_legends_data)
        except HTTPError as e:
            print(f"HTTP error while getting api: {e}")
        except Exception as e:
            print(f"An error occurred while getting api: {e}")

        names = df.columns.to_list()
        legend_list = []
        for i in range(24):
            if df.iloc[1, i] is numpy.NAN:
                continue
            Kills = df.iloc[1, i][0]["value"]
            Damage = df.iloc[1, i][1]["value"]
            Games_played = df.iloc[1, i][2]["value"]

            result_dict = {
                "Legend": names[i],
                "kills": Kills,
                "Damage": Damage,
                "Games_played": Games_played,
            }
            legend_list.append(result_dict)
        return pd.DataFrame(legend_list)
