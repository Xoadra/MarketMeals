



import re
import json
from marketmeals import db
from marketmeals.market.utils import path, html, static, urlify, catalog
from marketmeals.market.models import Market, MarketDay
from marketmeals.farmer.models import Farmer, farmer_days
from marketmeals.product.models import Product, FarmerProduct, Category
from marketmeals.recipe.models import Recipe, Ingredient
from flask import Blueprint, request, render_template, redirect, url_for, session, jsonify



market = Blueprint( 'market', __name__, static_url_path = path, static_folder = static, template_folder = html )



@market.route( '/url', methods = [ 'POST' ] )
def url( ):
	session[ 'market' ] = json.loads( request.data.decode( 'utf-8' ) )
	print( 'MARKET ' + session[ 'market' ][ 'name' ] )
	print( 'ZIPURL ' + session[ 'market' ][ 'zip_code' ] )
	session[ 'url' ] = urlify( session[ 'market' ][ 'name' ], session[ 'market' ][ 'zip_code' ] )
	print( 'NEWURL ' + session[ 'url' ] )
	url = Market.query.filter_by( url = session[ 'url' ] ).first( )
	if url is None:
		market = catalog( session[ 'market' ][ 'name' ], session[ 'url' ], session[ 'market' ][ 'address_components' ] )
		db.session.add( market )
		db.session.commit( )
	via = { 'url': session[ 'url' ], 'title': session[ 'market' ][ 'name' ] }
	return jsonify( via )


@market.route( '/market/<market>', methods = [ 'GET', 'POST' ] )
def view( market ):
	print( 'GETURL ' + market )
	print( 'SESURL ' + session[ 'url' ] )
	data = Market.query.filter_by( url = market ).first( )
	if market == session[ 'url' ] or data:
		farmers = [ ]
		categories = [ ]
		products = [ ]
		days = MarketDay.query.filter_by( market_id = data.market_id ).all( )
		for day in days:
			farmers.append( day.farmers )
			print( 'FARMDAY ', day.farmers )
		print( 'FARMERS ', farmers )
		for vendors in farmers:
			for farmer in vendors:
				matches = [ ]
				print( 'NEWFARMER' )
				print( farmer.products )
				for product in farmer.products:
					pid = product.product_id
					matches.append( Product.query.filter_by( product_id = pid ).first( ) )
				farmer.products = matches
				print( 'PRODUCTS ', farmer.products )
		categories = Category.query.all( )
		total = {
			'session': session[ 'market' ],
			'database': data,
			'farmers': farmers,
		}
		return render_template( 'market/market.html', total = total )
	else:
		return redirect( '/' )


## View method not yet linked to originally from templates branch
@market.route( '/join', methods = [ 'GET' ] )
def join( ):
	farmers = [ ]
	recipes = [ ]
	identifiers = {  }
	## Grabbing market via get request from the url most likely
	market = request.args.get( 'market' )
	if market:
		market = Market.query.filter_by( name = market ).first( )
		## Linking farmers with markets, so use farmer_days table
		days = farmer_days.query.filter_by( market_id = market.market_id ).all( )
		""" days = FarmerMarketLink.query.filter_by( market_id = market.market_id ).all( ) """
		for day in days:
			farmer = Farmer.query.filter_by( farmer_id = day.farmer_id ).first( )
			pid = farmer.farmer_id
			farmers.append( farmer )
			## Obtain the farmer's goods to be for sale at the market
			## Replace by querying the farmer_products table instead
			merch = FarmerProduct.query.filter_by( farmer_id = farmer.farmer_id ).all( )
			for good in merch:
				product = Product.query.filter_by( product_id = good.product_id ).first( )
				## Query the more semantic ingredients table for querying
				for ingredient in Ingredient.query.all( ):
					if ingredient.product_id == product.product_id:
						if ingredient not in recipes:
							recipes.append( Recipe.query.filter_by( recipe_id = ingredient.recipe_id ).first( ) )
				## Seems to be collecting farmer ids for a certain purpose
				if pid in identifiers:
					identifiers[ pid ].append( product )
				else:
					## Pretty sure this creates a 2D list for no good reason
					identifiers[ pid ] = [ product ]
		## Badly needs trimming down via a context dictionary variable
		return render_template(
			'market/market.html',
			market = market,
			farmers = farmers,
			categories = Category.query.all( ),
			identifiers = identifiers,
			recipes = recipes
		)
	else:
		return redirect( '/' )


