import datetime
import numpy as np
import pandas as pd
import re
import pandas as pd
import time
import csv
import concurrent.futures
import requests
import threading
import time

from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me



def run_scraper(alpha):
    #alpha = input("What is your main ingredient you've wasted:  ")
    data = pd.read_csv('RecipeData.csv')  

    for x in range(len(data)):
      food_data = data.iloc[x]["Wasted Food"]
      found = re.search(alpha, str(food_data))
      if found != None:
        link = data.iloc[x]["BBCGoodFood link"]
        break

    def download_url(url):
        resp = requests.get(url)
        title = "Content"
        with open(title, "wb") as fh:
            fh.write(resp.content)

    download_url(link)

    list_content = []
    file1 = open("Content","r+") 
    list_content.append(file1.read())
    list = []

    content = str(list_content)

    for y in range(1000):
      try:
        #list.append(re.search("(?P<url>https?://[^\s]+)", content).group("url"))
        x = re.search("(?P<url>https?://[^\s]+)", content).group("url")
        list.append(x)
        content = content.replace(str(x),"")
      except:
        break
        
    list_recipes = []

    for n in range(len(list)):
      a = re.search("recipes/", str(list[n]))
      b = re.search("https", str(list[n]))
      c = re.search("collection", str(list[n]))
      if a != None and b != None and c == None and n%2 == 0:
        list_recipes.append(list[n])

    for x in range(len(list_recipes)):
      link = str(list_recipes[x])
      link = link.partition('"')[0]
      list_recipes[x] = link

    list_scrape = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_RECIPES = []

    thread_local = threading.local()
    sites = list_recipes

    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    def download_site(url):
        session = get_session()
        recipe = str(url)
        scrape = scrape_me(recipe)
        title = scrape.title()
        ingredients = scrape.ingredients()
        instructions = scrape.instructions()
        return [title, len(ingredients), ingredients, instructions]

    def download_all_sites(sites):
        global title_links
        title_links = []
        title_names = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=13) as executor:
            for url in sites:
                title_links.append(executor.submit(download_site, url))
            for task in as_completed(title_links):
                title_names.append(task.result())
            return title_links, title_names

    title_links, data = download_all_sites(sites)
    return title_links, data