import io
import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import csv
import json

NUM_ARTICLES = 1
NUM_TOPICS = 5

def getLinks(topic, num):
    url = 'http://news.google.com/search?q='
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

    return stories_urls

def main():
    big_chungus = dict()
    with open('scrape/topics.csv', newline='') as f:
        reader = list(csv.reader(f))
        for i in range(NUM_TOPICS):
            big_chungus[i] = getLinks(reader[0][i], i)
            # big_chungus[str(reader[0][i])] = getLinks(reader[0][i], i)

    with open('parse/outputs.json', 'w') as outfile:
        outfile.write(json.dumps(big_chungus))

if __name__ == '__main__':
    main()