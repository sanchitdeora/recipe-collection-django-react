from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Recipe, RecipeURL
from .serializers import RecipeSerializer, RecipeURLSerializer

# @api_view(['GET', 'POST'])
# def recipe_list(request):
# 	if request.method == 'GET':
# 		data = Recipe.objects.all()
# 		serializer = RecipeSerializer(data, context={'request': request}, many=True)
# 		return Response(serializer.data)

class RecipeURL(generics.ListCreateAPIView):
    queryset = RecipeURL.objects.all()
    serializer_class = RecipeURLSerializer

# class DetailRecipe(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer