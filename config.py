from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

#initialize instances
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    #initialize extensions with the app 
    db.init_app(app)
    migrate.init_app(app)

    return app
