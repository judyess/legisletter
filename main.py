# To Do: Move API Key to a text folder so it isn't pushed to Github
# Legiscan and This program have to send statuses to eachother. Must use {status: OK} 

import requests
LEGISCAN_KEY = ""

def sessionList():
    url = f"https://api.legiscan.com/?key=LEGISCAN_KEY&op=OPERATION&PARAMS" # general format: https://api.legiscan.com/?key=APIKEY&op=OPERATION&PARAMS
    response = requests.get(url)

