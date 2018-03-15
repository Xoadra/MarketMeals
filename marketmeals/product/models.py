



from marketmeals import db
from marketmeals.index.utils import get_now
from marketmeals.index.models import Base
from marketmeals.recipe.models import Ingredient
from sqlalchemy.dialects import postgresql



class Product( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'products'
	product_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 40 ), nullable = False )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	category_id = db.Column( db.Integer, db.ForeignKey( 'categories.category_id' ) )
	
	markets = db.relationship( 'MarketDay', secondary = 'product_days', backref = 'products' )
	ingredients = db.relationship( 'Ingredient', backref = 'products' )
	farmers = db.relationship( 'FarmerProduct', backref = 'wares' )
	
	def __init__( self, name ):
		self.name = name
	
	def __repr__( self ):
		return str( 'Product: ' + str( self.product_id ) + ' ' + self.name + ' ' + str( self.category_id ) )


class FarmerProduct( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmer_products'
	farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmers.farmer_id' ), primary_key = True )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ), primary_key = True )
	price = db.Column( postgresql.MONEY ) ## NOT NULL
	available = db.Column( db.Boolean ) ## NOT NULL
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	farmers = db.relationship( 'Farmer', backref = 'wares' )
	products = db.relationship( 'Product', backref = 'vendors' )
	
	def __init__( self, farmer_id, product_id ):
		""" price, available """
		self.farmer_id = farmer_id
		self.product_id = product_id
		""" self.price = price
		self.available = available """
	
	def __repr__( self ):
		return str( 'FarmerProduct: ' + str( self.farmer_id ) + ' ' + str( self.product_id ) )


class Category( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'categories'
	category_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	group = db.Column( db.String( 30 ), nullable = False )
	category = db.Column( db.String( 30 ), nullable = False )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	products = db.relationship( 'Product', backref = 'categories' )
	
	def __init__( self, category ):
		self.category = category
	
	def __repr__( self ):
		return str( 'Category: ' + str( self.category_id ) + ' ' + self.group + ' ' + self.category )


## A many-to-many table for which day products are sold
product_days = db.Table( 'product_days', Base.metadata,
	db.Column( 'product_id', db.Integer, db.ForeignKey( 'products.product_id' ), primary_key = True ),
	db.Column( 'market_day_id', db.Integer, db.ForeignKey( 'market_days.market_day_id' ), primary_key = True )
)



