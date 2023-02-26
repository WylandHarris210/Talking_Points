import pyttsx3
import json
import requests
def twireq():
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424977"
    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAALCVbAEAAAAAM3chpDW3NCSGAjk7%2FwCa%2B%2BbWWRk%3DN9dO47Lx9L9tEJXcaBWgehlZDuaVCGyl1ficelzA0EZrjY2uNA',
    'Cookie': 'guest_id=v1%3A167734669699093551; guest_id_ads=v1%3A167734669699093551; guest_id_marketing=v1%3A167734669699093551; personalization_id="v1_zXS78KySxicfVHRnP7YLWw=="'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    r = response.json()
    with open('parse/dev.json', 'w') as f:
        json.dump(r, f)
globarr = {}
def get_element_from_json(json_str, key):
    json_obj = json.loads(json_str)
    return json_obj[key]
def readjson():
    # with open("dev.json") as file:
    #     js = json.load(file)
    #     x = len(js['trends'])
    #     for i in range(0,x):
    #         globarr.append(js['trend'][0]["name"])
    data = json.loads('dev.json')
    names = [trend["name"] for trend in data[0]["trends"]]
    print(names)
def get_query(json_str):
    data = json.loads(json_str)
    queries = [trends["query"] for trends in data[0]["trends"]]
    return queries

def ttsorg():
    x='temp'
    while(x!=''):
        x = input()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) 
        engine.setProperty('rate', 111) 
        engine.say(x)
        engine.runAndWait()
# readjson()
# print(globarr)
# ttsorg()
# get_query('dev.json')
twireq()
