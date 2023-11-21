import requests
import json
import pandas as pd
import numpy
class ApiProcess:
    def __init__(self,auth):
        self.auth=auth
        pass
    def get_uid(self,player,pf='PC'):
        url = f'https://api.mozambiquehe.re/nametouid?auth={self.auth}&player={player}&platform={pf}'

        response = requests.get(url)

        # Check response status and content
        if response.status_code == 200:
            data = json.loads(response.text)
            # Get the value of 'uid'
            uid_value = data['uid']
            print("uid:",uid_value)
            return uid_value
        else:
            print(response.status_code) 
    def get_data(self,uid,pf='PC'):
        url = f'https://api.mozambiquehe.re/bridge?auth={self.auth}&uid={uid}&platform={pf}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            my_legends_data = data['legends']["all"]
        df = pd.DataFrame(my_legends_data)
        return df
    def json2df(self,df):
        '''
        
        '''
        names = (df.columns.to_list())
        legend_list=[]
        for i in range(24):
            if df.iloc[1,i] is numpy.NAN:
                continue
            Kills=df.iloc[1,i][0]['value']
            Damage=df.iloc[1,i][1]['value']
            Games_played=df.iloc[1,i][2]['value']


            result_dict = {
                            'Legend': names[i],
                            'kills': Kills,
                            'Damage': Damage,
                            'Games_played': Games_played
                        }

            legend_list.append(result_dict)  # Append the dictionary to the list
        return pd.DataFrame(legend_list)

