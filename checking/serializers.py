from rest_framework import serializers
from .models import Recipe, RecipeURL

class RecipeURLSerializer(serializers.ModelSerializer):
	class Meta:
		fields = "__all__"
		model = RecipeURL

class RecipeSerializer(serializers.ModelSerializer):
	ingredients = serializers.SerializerMethodField()
	nutritions = serializers.SerializerMethodField()
	class Meta:
		fields = '__all__'
		model = Recipe
	
	def get_ingredients(self, obj):
		return_data = None
		if type(obj.ingredients) == list:
			ingredients_list = []
			for item in obj.ingredients:
				ingredients_dict = item.__dict__
				for key in list(ingredients_dict.keys()):
					if key.startswith('_'):
						ingredients_dict.pop(key)
				ingredients_list.append(ingredients_dict)
			return_data = ingredients_list
		else:
			ingredients_dict = field.__dict__
			for key in list(ingredients_dict.keys()):
				if key.startswith('_'):
					ingredients_dict.pop(key)
			return_data = ingredients_dict
		return return_data
		
	def get_nutritions(self, obj):
		return_data = None
		if type(obj.nutritions) == list:
			nutritions_list = []
			for item in obj.nutritions:
				nutritions_dict = item.__dict__
				for key in list(nutritions_dict.keys()):
					if key.startswith('_'):
						nutritions_dict.pop(key)
				nutritions_list.append(nutritions_dict)
			return_data = nutritions_list
		else:
			nutritions_dict = field.__dict__
			for key in list(nutritions_dict.keys()):
				if key.startswith('_'):
					nutritions_dict.pop(key)
			return_data = nutritions_dict
		return return_data	