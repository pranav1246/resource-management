from flask import Flask
from application.models import db , User, Role
from config import DevelopmentConfig
from application.resources import api
from flask_security import SQLAlchemyUserDatastore, Security

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)  # config the app
    db.init_app(app)  # config sqlalchemy
    api.init_app(app)
    datastore=SQLAlchemyUserDatastore(db,User,Role)
    app.security=Security(app,datastore)
    with app.app_context():
        import application.views

    return app , datastore


app , datastore = create_app()

if __name__ == '__main__':
    app.run(debug=True)
