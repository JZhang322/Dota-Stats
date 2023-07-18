
import json
import requests
import pandas as pd
import scipy

myAccount = "79219909"
URL = "https://api.opendota.com/api/heroStats"
r = requests.get(url = URL)
data = r.json()


heroes_table = pd.DataFrame(data)
ids = heroes_table['id'].values.tolist()
print(ids)



#function to find the top 5 heroes you have the lowest winrate against
#NOTES need to somehow find how I can use only one API call 
#could also compare relative to global hero winrates, to see if you are losing disproportionately 
def most_L(accountID):
    res = {}

    for x in ids:
        
        URL = "https://api.opendota.com/api/players/" + accountID + "/matches"
        hero = str(x)
        print(hero)
        params = {
            'win' : '0',
            'against_hero_id' : hero
        }
        r = requests.get(url = URL, params = params)
        data = r.json()


        df = pd.DataFrame(data)
        losses = len(df)
        if losses == 0:
            continue

        params = {
            'win' : '1',
            'against_hero_id' : hero
        }
        r = requests.get(url = URL, params = params)
        data = r.json()


        df = pd.DataFrame(data)
        wins = len(df)
        if wins == 0:
            continue

        winrate = wins/(wins+losses)

        #flattened_data = pd.DataFrame(df['heroes'].apply(pd.Series))

        print(winrate)
        res[hero] = winrate
    hero_list = [(k, v) for k, v in res.items()]
    hero_list.sort(key=lambda s: s[1])
    keys = [i[0] for i in hero_list[:5]]
    print(keys)
    return keys

#most_L(myAccount)

