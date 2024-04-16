from flask import Flask,render_template
from flask_cors import CORS
from .utils.extensions import db,ma
from .routes.UserRoute import user_router
from .routes.IndexRoute import index_router

def configure_app():
    app=Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:1234@localhost/users_crud"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    app.secret_key="1234"

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_router)
    app.register_blueprint(index_router)
    return app

