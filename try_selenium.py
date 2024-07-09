from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from IPython.display import display,Image
import graphviz
from selenium.webdriver.common.by import By
from graphviz import Digraph
from collections import deque
import time

gv=Digraph(engine="neato")

Options=Options()
Options.add_argument('--headless')

driver=webdriver.Chrome(options=Options)

starting_url='https://quotes.toscrape.com/'

task=deque([starting_url])
links=set()
depth = {starting_url: 0}

def visting_url(url):
    driver.get(url)
    driver.save_screenshot("shot.png")
    #display(Image("shot.png"))
    driver.set_window_size(300,200)

    links=driver.find_elements(By.XPATH,'//a[@href]')
    item=[a.get_attribute("href") for a in links]
    return item

# print(task)
# print(links)
# print(depth)
while len(task)>0:
    max_depth = 1
    url=task.popleft()
    depth[url] = 0
   
    if depth[url] < max_depth:
        children_url=visting_url(url)
        time.sleep(3)
        for child in children_url:
            if not child in links:
                task.append(child)
                links.add(child)
                depth[url] += 1
                time.sleep(3)
print(len(links))



#visting_url('https://quotes.toscrape.com/')
