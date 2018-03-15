



import re
from marketmeals.zipcode.utils import path, html, static
from flask import Blueprint, request, render_template, redirect, url_for, session



zipcode = Blueprint( 'zipcode', __name__, static_url_path = path, static_folder = static, template_folder = html )



@zipcode.route( '/location', methods = [ 'GET', 'POST' ] )
def location( ):
	if request.method == 'GET':
		return session[ 'zipcode' ]
	elif request.method == 'POST':
		session[ 'zipcode' ] = request.form[ 'zipcode' ]
		return redirect( url_for( 'zipcode.mapapi', zipcode = session[ 'zipcode' ] ) )
	else:
		return redirect( '/' )


@zipcode.route( '/zipcode/<zipcode>', methods = [ 'GET' ] )
def mapapi( zipcode ):
	if re.match( r'^[0-9]{5}$', zipcode ):
		session[ 'zipcode' ] = zipcode
		print( 'SESSION ' + session[ 'zipcode' ] )
		print( 'ZIPCODE ' + zipcode )
		return render_template( 'zipcode/map.html', zipcode = zipcode )
	else:
		return redirect( '/' )



