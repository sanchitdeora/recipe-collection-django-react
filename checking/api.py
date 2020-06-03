from checking.models import Recipe, RecipeURL
from rest_framework import viewsets, permissions
from .serializers import RecipeSerializer, RecipeURLSerializer
from .scraper import RecipeScraper

# RecipeURL Viewset
class RecipeURLViewSet(viewsets.ModelViewSet):
	serializer_class = RecipeURLSerializer


	def get_queryset(self):
		return RecipeURL.objects.all()

	def perform_create(self, serializer):
		serializer.save()
		RecipeScraper.fetch()

# Recipe Viewset
class RecipeViewSet(viewsets.ModelViewSet):
	# permission_classes = [
	# 	permissions.IsAuthenticated,
	# ]
	serializer_class = RecipeSerializer

	def get_queryset(self):
		return Recipe.objects.all()
		# return self.request.user.leads.all()

	def perform_create(self, serializer):
		serializer.save(owner=self.request)