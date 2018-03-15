



from marketmeals.recipe.utils import html
from flask import Blueprint, render_template



recipe = Blueprint( 'recipe', __name__, template_folder = html )



@recipe.route( '/recipe', methods = [ 'GET' ] )
def cuisine( ):
	return render_template( 'recipe/recipe.html' )


## Temporarily commented out changes from templates branch
""" @recipe.route( '/kitchen' )
def kitchen( ):
	Fetching the recipe name from the url through a get request
	recipe = request.args.get( 'recipe' )
	if recipe:
		recipe = Recipe.query.filter_by( name = recipe ).first( )
		Unsure if this is meant to be a collective value or not
		return render_template( 'recipe/kitchen.html', recipes = recipe )
	else:
		Querying for all recipes for displaying on templates
		return render_template( 'recipe/kitchen.html', recipes = get_recipes( ) ) """



