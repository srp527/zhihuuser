# -*- coding:utf-8 -*- 
__author__ = 'SRP'

import requests
from bs4 import BeautifulSoup


# start_urls = []

# start_page = 1
start_url = 'http://www.xicidaili.com/nt/{page}'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
# def start_request(self):
for i in range(1,5):
    url = start_url.format(page=i)
    html = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    # print(soup)
    all = soup.findAll('tr',class_='odd' or ' ')
    # print(all)
    for i in all:
        # print(i)
        t = i.find_all('td')
        ip = t[1].text
        print(ip)

