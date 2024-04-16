from ...utils.extensions import db,ma
from werkzeug.security import check_password_hash

class User(db.Model):
    dni=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    surname=db.Column(db.String(100))
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(100),unique=True)
    def __str__(self,dni,name,surname,password,email):
        self.dni=dni
        self.name=name
        self.surname=surname
        self.password=password
        self.email=email
    @classmethod
    def check_password(self,password_hash,password):
        return check_password_hash(password_hash,password)
class UserSchema(ma.Schema):
    class Meta:
        fields=('dni','name','surname',"password",'email')

user_schema=UserSchema()
users_schema=UserSchema(many=True)