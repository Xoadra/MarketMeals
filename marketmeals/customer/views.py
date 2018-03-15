



from marketmeals.customer.utils import html
from flask import Blueprint, render_template



customer = Blueprint( 'customer', __name__, template_folder = html )



@customer.route( '/login' )
def login( ):
	return render_template( 'customer/login.html' )


@customer.route( '/logout' )
def logout( ):
	return render_template( 'index/index.html' )


@customer.route( '/customer' )
def profile( ):
	return render_template( 'customer/customer.html' )



