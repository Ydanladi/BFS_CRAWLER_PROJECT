from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from IPython.display import display,Image
from bs4 import BeautifulSoup
from collections import deque
import requests
import time
from graphviz import Digraph

starting_url = 'https://quotes.toscrape.com/'

gv=Digraph(engine="neato")

queue = deque([starting_url])
visited = set()
depth = {starting_url: 0}

def fetch_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

while queue:
    max_depth = 3
    current_url = queue.popleft()
    current_depth = depth[current_url]
    if current_depth < max_depth:
        soup = fetch_page(current_url)
        for link in soup.find_all('a', href=True):
            url = link['href']
            if url.startswith('/'):
                url = starting_url + url
                if url not in visited:
                    visited.add(url)
                    queue.append(url)
                    depth[url] = current_depth + 1
        time.sleep(2)
    time.sleep(2)
print(len(visited))
    
    

        

