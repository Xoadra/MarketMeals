



import re
import random
from marketmeals import db
from marketmeals.index.utils import html
from marketmeals.product.models import FarmerProduct
from flask import Blueprint, render_template, redirect, url_for



index = Blueprint( 'index', __name__, template_folder = html )



@index.route( '/', methods = [ 'GET' ] )
def land( ):
	return render_template( 'index/index.html' )


@index.route( '/about', methods = [ 'GET' ] )
def about( ):
	return render_template( 'index/about.html' )


@index.route( '/error' )
def error( ):
	return render_template( 'index/error.html' )



""" for rand in range( 74, 1016 ):
	print( ' - - - - - ')
	print( 'SET ' + str( rand ) )
	for series in range( 0, 8 ):
		item = random.randint( 1, 159 )
		print( item )
		if FarmerProduct.query.filter_by( farmer_id = rand, product_id = item ).first( ):
			pass
		else:
			merch = FarmerProduct( farmer_id = rand, product_id = item )
			db.session.add( merch )
			db.session.commit( )
	print( ' - - - - - ') """



