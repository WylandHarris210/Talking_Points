import io
import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import csv
import json

NUM_ARTICLES = 2
NUM_TOPICS = 5

def main(topic, num):
    url = 'http://news.google.com/search?q='
    # header = {'user_agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

    res = r.get(url + topic)

    if res.status_code != 200:
        print('Bad request, recieved code', res.status_code)
        exit()

    print('Request is good')
    
    soup = BeautifulSoup(res.content, 'lxml')

    stories = soup.find('div', attrs = { 'class': 'lBwEZb BL5WZb GndZbb' })

    stories_list = stories.find_all('div', attrs = { 'class': 'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc' })[:3]

    stories_urls = [None] * NUM_ARTICLES

    for i in range(NUM_ARTICLES):
        stories_urls[i] = 'https://news.google.com' + stories_list[i].find('a', attrs = { 'class': 'VDXfz' })['href'][1:]

    # stories_urls_json = json.dumps(stories_urls)
    return stories_urls

    # with open('scrape/links' + str(num) + '.json', 'w') as outfile:
    #     outfile.write(stories_urls_json)

if __name__ == '__main__':
    big_chungus = dict()
    with open('scrape/topics.csv', newline='') as f:
        reader = list(csv.reader(f))
        for i in range(NUM_TOPICS):
            big_chungus[str(reader[0][i])] = main(reader[0][i], i)

    with open('Tweeter/outputs.json', 'w') as outfile:
        # outfile.write(json.dumps(big_chungus))
        temp = json.dumps(big_chungus)
        outfile.write(temp)