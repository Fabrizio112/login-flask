from flask import Blueprint,jsonify,request
from ..models.entities.User import User,user_schema,users_schema
from ..utils.extensions import db
from werkzeug.security import generate_password_hash

user_router=Blueprint("user_router",__name__)

@user_router.route("/user",methods=['GET'])
def get_users():
    users=User.query.all()
    results=users_schema.dump(users)
    return jsonify(results)
