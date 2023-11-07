from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

#Create the server
app=Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] =os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://vxhujtvo:bhftWTnW2cEOnnwHud2q7luV_xRZN3nO@trumpet.db.elephantsql.com/vxhujtvo"
#Creating an instance of database
db=SQLAlchemy(app)

#Anything that is using app then would be imported after the app is initialised above

from application import routes