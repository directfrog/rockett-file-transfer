from WordProcessor import *
from WebScraper import *
import pandas as pd 
import math, time, sys, os, csv

def ProcessWords(text):
	processor = WordProcessor(text)
	results = processor.run()
	return results
     

def get_common_ingredients(results, ingreds):
	common_ingreds = []
	for x in ingreds:
		if x in results:
			common_ingreds.append(x)
	return common_ingreds             

def sort_num_ingreds(arr):
	copy_arr = arr.copy()
	sorted_arr = []
	for x in copy_arr:
		smallest = arr[0]
		for compare in arr:
			if compare[1] < smallest[1]:
				smallest = compare
		sorted_arr.append(smallest)
		arr.pop(arr.index(smallest))
	return sorted_arr


def get_foods():
	main_item = ProcessWords('my main item is apple')
	AnyOtherIngreds = ProcessWords('my other ingredients are apricots and bread and almonds')
	print('WORD PROCESSOR RESULTS: ', AnyOtherIngreds)
	time.sleep(1)
	title_links, data = run_scraper(main_item[0])
	commonVals = []
	common = []
	common_recipes = []
	true_common_recipes = []
	for x in data:
		results_ingredients = ' '.join(x[2])
		result_ingreds = ProcessWords(results_ingredients)
		common_ingreds = []
		for ingred in result_ingreds:
			if ingred == main_item or ingred in AnyOtherIngreds:
				if ingred not in common_ingreds:
					common_ingreds.append(ingred)
		commonVals.append(len(common_ingreds))
		common_recipes.append(x)
		common.append(common_ingreds)
		common_recipes.append(x)

	for x in common_recipes:
		if x not in true_common_recipes:
			true_common_recipes.append(x)
	true_common_recipes = sort_num_ingreds(true_common_recipes)
	for x in true_common_recipes:
		print([x[0], x[1]])
	

if __name__ == '__main__':
	get_foods()
