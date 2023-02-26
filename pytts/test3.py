import pyttsx3
import json
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
    with open("dev.json") as file:
        js = json.load(file)
        name = get_element_from_json(js["trends"], "name")
        return name

def tts():
    x='temp'
    while(x!=''):
        x = input()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) 
        engine.setProperty('rate', 111) 
        for i in range(0,20):
            engine.say()
            
        engine.runAndWait()
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
ttsorg()

