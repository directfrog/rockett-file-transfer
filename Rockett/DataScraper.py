from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.bbcgoodfood.com/recipes/slow-cooker-pork-fillet-apples")

content = driver.page_source()
soup = BeautifulSoup(content)

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	preptime=a.find('time', attrs={'datetime':'PT0H15M'})
