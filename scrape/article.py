import io
import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import json

def main():
    url = 'http://news.google.com/search?q='
    # header = {'user_agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

    search = input('What would you like to look for?\n')

    # res = r.get(url + 'Tennis', headers = header)
    res = r.get(url + search)
    # res = r.get(url + search, headers = header)

    if res.status_code != 200:
        print('Bad request, recieved code', res.status_code)
        exit()

    print('Request is good')
    
    soup = BeautifulSoup(res.content, 'lxml')

    stories = soup.find('div', attrs = { 'class': 'lBwEZb BL5WZb GndZbb' })

    stories_list = stories.find_all('div', attrs = { 'class': 'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc' })[:3]

    stories_urls = [None] * 3

    for i in range(3):
        stories_urls[i] = 'https://news.google.com' + stories_list[i].find('a', attrs = { 'class': 'VDXfz' })['href'][1:]

    stories_urls_json = json.dumps(stories_urls)

    with open('scrape/links.json', 'w') as outfile:
        outfile.write(stories_urls_json)

if __name__ == '__main__':
    main()