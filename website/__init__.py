from flask import Flask
from .models import db
from .config import DB_NAME, secret_key


def create_app():
    app = Flask(__name__)
    app.config['SECERT_KEY'] = 'smt'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.secret_key = secret_key
    db.init_app(app)
    
    from .routes import routes
    
    app.register_blueprint(routes, url_prefix='/')
    
    with app.app_context():
        db.create_all()
    
    return app

