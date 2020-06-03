from djongo import models
from django import forms

class Nutrition(models.Model):
	item = models.CharField(max_length=200)
	score = models.CharField()
	class Meta:
		abstract = True
	def __str__(self):
		return self.item

class Ingredient(models.Model):
	item = models.CharField(max_length=200)
	quantity = models.CharField()
	class Meta:
		abstract = True
	def __str__(self):
		return self.item

class RecipeURL(models.Model):
	url = models.CharField(max_length=2000)

class Recipe(models.Model):
	title = models.CharField(max_length=200)
	ingredients = models.ArrayModelField(model_container=Ingredient)
	nutritions = models.ArrayModelField(model_container=Nutrition)
	instructions = models.TextField()
	def __str__(self):
		return self.title