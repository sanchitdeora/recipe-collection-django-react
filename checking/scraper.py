from bs4 import BeautifulSoup
import requests
from .models import RecipeURL, Recipe, Ingredient
from recipe_scrapers import scrape_me

class RecipeScraper:
	
	def fetch():
		count = RecipeURL.objects.all().count()
		url = RecipeURL.objects.all()[count-1]
		RecipeScraper.scrape(url.url)

	def scrape(url):
		recipe = scrape_me(url)
		recipe_ingredients = []

		for ingredient in recipe.ingredients():
			item = ingredient.split(" ", 1)[1]
			quantity = ingredient.split(" ", 1)[0]
			new_ingredient = Ingredient(
				item=item,
				quantity=quantity
			)
			recipe_ingredients.append(new_ingredient)
			
		new_recipe = Recipe(title=recipe.title(), ingredients=recipe_ingredients, nutritions=[], instructions=recipe.instructions())
		new_recipe.save()
		