from IPython.display import display,Image
from bs4 import BeautifulSoup
from collections import deque
import requests
import time
import csv
import pandas as pd
from graphviz import Digraph

starting_url = 'https://quotes.toscrape.com/' # starting point for bfs crawler

#gv=Digraph(engine="neato")

#creating containers to store data and process the queue
queue = deque([starting_url])
visited = set()
depth = {starting_url: 0}

#function that will take each url and return the contents with bs4 parser
def fetch_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

#while loop will run as long as the queue container has an item, and pick the next url to process again till its empty
while queue:
    max_depth = 3
    current_url = queue.popleft()
    current_depth = depth[current_url]
    #give that the depth of our search is three level, the if statement will chech the contion that we are still within require depth
    if current_depth < max_depth:
        soup = fetch_page(current_url)
        for link in soup.find_all('a', href=True):
            url = link['href']
            if url.startswith('/'):
                #joining short url with the incomplete scrapped link
                url = starting_url + url
                #avoiding repetations
                if url not in visited:
                    visited.add(url)
                    queue.append(url)
                    depth[url] = current_depth + 1
        time.sleep(2)
    time.sleep(2)
#saving links to csv fine named data
with open('data.csv','w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerows(visited)

df=pd.DataFrame(visited)
df.to_csv("data2.csv",index=False,header=False)
print("finished")
    