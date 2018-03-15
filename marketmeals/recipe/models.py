



from marketmeals import db
from marketmeals.index.utils import get_now
from marketmeals.index.models import Base
from sqlalchemy.dialects import postgresql



## Unsure of the exact purpose of this table
''' class FarmerProdcatLink( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmer_prodcat_link'
	
	farmer_id = db.Column( db.Integer, db.ForeignKey( 'farmer.farmer_id' ), primary_key = True )
	prodcat_id = db.Column( db.Integer, db.ForeignKey( 'prodcat.prodcat_id' ), primary_key = True ) '''


class Recipe( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'recipes'
	recipe_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 50 ), nullable = False, unique = True )
	## Refactoring into its own normalized, alternative table
	''' recipe_directions = db.Column( db.Text ) '''
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	ingredients = db.relationship( 'Ingredient', backref = 'recipes' )
	directions = db.relationship( 'Direction', backref = 'recipes' )
	
	def __init__( self, name, recipe_directions ):
		self.name = name
		## Placed into its own table for optimal normalization
		''' self.recipe_directions = recipe_directions '''
	
	def __repr__( self ):
		return '<Recipe %r' % self.recipe_name


## New normalized table for containing recipe directions
class Direction( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'directions'
	direction_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	order = db.Column( db.SmallInteger ) ## NOT NULL
	summary = db.Column( db.String( 200 ) )
	instruction = db.Column( db.Text ) ## NOT NULL
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	recipe_id = db.Column( db.Integer, db.ForeignKey( 'recipes.recipe_id' ) )
	
	def __init__( self, order, instruction ):
		self.order = order
		self.instruction = instruction
	
	def __repr__( self ):
		return '<Direction %r' % self.instruction


## Was Recipeproduct table, but given more semantic naming
class Ingredient( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'ingredients'
	ingredient_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	ingredient_quantity = db.Column( db.String( 255 ) )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	recipe_id = db.Column( db.Integer, db.ForeignKey( 'recipes.recipe_id' ) )
	product_id = db.Column( db.Integer, db.ForeignKey( 'products.product_id' ) )
	
	def __init__( self, ingredient_quantity ):
		## Old names for previous database model backrefs
		''' owner_recipe, owner_product '''
		self.ingredient_quantity = ingredient_quantity
		''' self.owner_recipe = owner_recipe
		self.owner_product = owner_product '''
	
	def __repr__( self ):
		return '<Ingredient %r' % self.ingredient_quantity



