



import os
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib import parse



app = Flask( __name__ )
db = SQLAlchemy( app )


## Modularize app by registering blueprints
from marketmeals.index.views import index
from marketmeals.zipcode.views import zipcode
from marketmeals.market.views import market
from marketmeals.farmer.views import farmer
from marketmeals.customer.views import customer
from marketmeals.product.views import product
from marketmeals.recipe.views import recipe
app.register_blueprint( index )
app.register_blueprint( zipcode )
app.register_blueprint( market )
app.register_blueprint( farmer )
app.register_blueprint( customer )
app.register_blueprint( product )
app.register_blueprint( recipe )


## Using psycopg2 to connect to database
parse.uses_netloc.append( 'postgres' )
url = parse.urlparse( os.environ[ 'DATABASE_URL' ] )

conn = psycopg2.connect(
	database = url.path[ 1: ],
	user = url.username,
	password = url.password,
	host = url.hostname,
	port = url.port
)


app.config[ 'DEBUG' ] = True
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.environ[ 'DATABASE_URL' ]
## Omitted placeholder database access data
''' app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.environ.get(
	'DATABASE_URL',
	'postgresql+psycopg2://' + 'user' + ':' + 'password' + '@' + 'host' + ':' + 'port' + '/' + 'dbname'
) '''
app.config[ 'SQLALCHEMY_ECHO' ] = False


## This is a security risk and should be moved
app.secret_key = 'MarKetMeaLSiSAMAzinG'



