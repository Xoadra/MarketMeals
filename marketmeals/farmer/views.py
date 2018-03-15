



from marketmeals import db
from marketmeals.farmer.utils import path, html, static
from marketmeals.farmer.models import Farmer
from marketmeals.product.models import Category, FarmerProduct
from flask import Blueprint, render_template, redirect, jsonify



farmer = Blueprint( 'farmer', __name__, static_url_path = path, static_folder = static, template_folder = html )



@farmer.route( '/farmer', methods = [ 'GET' ] )
def vendor( ):
	box = [ ]
	farmer = request.args.get( 'farmer' )
	if farmer:
		farmer = Farmer.query.filter_by( first_name = farmer ).first( )
		farpros = FarmerProduct.query.filter_by( farmer_id = farmer.farmer_id ).all( )
		for farpro in farpros:
			category = Category.query.filter_by( category_id = category.category_id ).first( )
			amount.append( category )
		return render_template( 'farmer/farmer.html', farmer = farmer, farpros = farpros, amount = amount )
	else:
		return redirect( '/' )


@farmer.route( '/farm', methods = [ 'GET' ] )
def farm( ):
	return render_template( 'farmer/farm.html' )


@farmer.route( '/data', methods = [ 'GET' ] )
def data( ):
	query = Farmer.query.all( )
	farmers = [ ]
	for item in query:
		farmer = {  }
		for data in dir( item ):
			if not hasattr( super( Farmer, item ), data ) and data[ 0 ].isalpha( ):
				farmer[ data ] = getattr( item, data )
		farmers.append( farmer )
	return jsonify( farmers )


