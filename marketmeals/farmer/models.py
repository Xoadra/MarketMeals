



from marketmeals import db
from marketmeals.index.utils import get_now
from marketmeals.index.models import Base



class Farmer( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farmers'
	farmer_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	first_name = db.Column( db.String( 40 ), nullable = False )
	last_name = db.Column( db.String( 40 ), nullable = False )
	## Potential columns for login and registration authentication
	''' gender = db.Column( db.String( 20 ) )
	birthday = db.Column( db.Date )
	email_address = db.Column( db.String( 75 ), unique = True )
	password = db.Column( db.String( 50 ) )
	phone_number = db.Column( db.String( 20 ) )
	street_address = db.Column( db.Text )
	city = db.Column( db.String( 40 ) )
	state = db.Column( db.String( 2 ) )
	zip_code = zip_code = db.Column( db.Integer( 5 ) ) '''
	joined_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	farm_id = db.Column( db.Integer, db.ForeignKey( 'farms.farm_id' ) )
	
	markets = db.relationship( 'MarketDay', secondary = 'farmer_days', backref = 'farmers' )
	products = db.relationship( 'FarmerProduct', backref = 'vendors' )
	
	def __init__( self, first_name, last_name ):
		self.first_name = first_name
		self.last_name = last_name
	
	def __repr__( self ):
		return str( 'Farmer: ' + str( self.farmer_id ) + ' ' + self.first_name + ' ' + self.last_name )


## Optional table for participating farms at market
class Farm( Base ):
	__table_args__ = { 'extend_existing': True }
	__tablename__ = 'farms'
	farm_id = db.Column( db.Integer, autoincrement = True, primary_key = True )
	name = db.Column( db.String( 75 ) ) ## NOT NULL
	email_address = db.Column( db.String( 75 ), unique = True )
	phone_number = db.Column( db.String( 20 ) )
	street_address = db.Column( db.Text ) ## NOT NULL
	city = db.Column( db.String( 40 ) ) ## NOT NULL
	state = db.Column( db.String( 2 ) ) ## NOT NULL
	zip_code = zip_code = db.Column( db.Integer )
	created_at = db.Column( db.DateTime( timezone = True ), nullable = False, default = get_now( ) )
	updated_at = db.Column( db.DateTime( timezone = True ), default = get_now( ), onupdate = get_now( ) )
	
	farmers = db.relationship( 'Farmer', backref = 'farms' )
	
	def __init__( self, name, email_address, phone_number, street_address, city, state, zip_code ):
		self.name = name
		self.email_address = email_address
		self.phone_number = phone_number
		self.street_address = street_address
		self.city = city
		self.state = state
		self.zip_code = zip_code
	
	def __repr__( self ):
		return str( 'Farm: ' + str( self.farm_id ) + ' ' + self.name )


## Farmers' days at market, a many-to-many db.relationship
farmer_days = db.Table( 'farmer_days', Base.metadata,
	db.Column( 'farmer_id', db.Integer, db.ForeignKey( 'farmers.farmer_id' ), primary_key = True ),
	db.Column( 'market_day_id', db.Integer, db.ForeignKey( 'market_days.market_day_id' ), primary_key = True )
)


