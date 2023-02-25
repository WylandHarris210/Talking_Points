import io
import pandas as pd
import requests as r

url = 'http://news.google.com/search?q='

search = input('What would you like to look for?\n')

res = r.get(url + search)

if res.status_code != 200:
    print('Bad request, recieved code', res.status_code)
    exit()

print('Request is good')

