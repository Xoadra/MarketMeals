



from datetime import datetime, timezone



html = 'templates'


def get_now( ):
	return lambda : datetime.now( timezone.utc )


""" def get_farmers( ):
	return Farmer.query.filter_by( ).all( )

def get_markets( ):
	return Market.query.filter_by( ).all( )

def get_recipes( ):
	return Recipe.query.filter_by( ).all( )

def get_categories( ):
	return Category.query.filter_by( ).all( )

def get_farmer_products( ):
	return FarmerProduct.query.filter_by( ).all( )

def get_products( ):
	return Product.query.filter_by( ).all( ) """



