from django.shortcuts import render
from utils.recipes.recipe_details import make_recipe_details

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipe': [make_recipe_details() for _ in range(10)]
    })


def recipes(request, recipe_id):
    return render(request, 'recipes/pages/recipe.html', context={
        'recipe': make_recipe_details(),
        'is_detail_page': True
    })