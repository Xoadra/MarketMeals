from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+pymysql://market-meals:market-meals@localhost:8889/market-meals')
#app.config['SQLALCHEMY_ECHO'] = True

#db = SQLAlchemy(app)

app.secret_key = 'MarKetMeaLSiSAMAzinG'
