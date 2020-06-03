# from django.urls import path
# from . import views
# from rest_framework import routers

# urlpatterns = [
#     path('', views.ListRecipe.as_view()),
#     path('<int:pk>/', views.DetailRecipe.as_view()),
# ]

from rest_framework import routers
from .api import RecipeViewSet, RecipeURLViewSet

router = routers.DefaultRouter()
router.register('api/recipes', RecipeViewSet, 'recipes')
router.register('api/recipe_url', RecipeURLViewSet, 'recipe_url')

urlpatterns = router.urls