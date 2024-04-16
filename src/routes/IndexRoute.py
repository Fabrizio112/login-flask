from flask import Blueprint,render_template,request,redirect,url_for,flash
from ..models.entities.User import User,user_schema
from werkzeug.security import generate_password_hash,check_password_hash
from ..utils.extensions import db

index_router=Blueprint('index_router',__name__)

@index_router.route("/")
def index():
    return redirect(url_for("index_router.login"))


@index_router.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        user_exist=User.query.filter_by(email=email).first()
        if user_exist != None:
            user_dict=user_schema.dump(user_exist)
            password_user=user_dict["password"]
            if check_password_hash(password_user,password) == True:
                return redirect(url_for("index_router.home"))
            else:
                flash("Contraseña incorrecta")
                return render_template("login.html")
        else:
            flash("Usuario No encontrado")
            return render_template("login.html")

    return render_template("login.html")
    
@index_router.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        dni_ingresado=request.form["dni"]
        usuario_dni=User.query.filter_by(dni=dni_ingresado).first()
        if usuario_dni == None:
            email_ingresado=request.form["email"]
            usuario_email=User.query.filter_by(email=email_ingresado).first()
            if usuario_email == None:
                if request.form["password"] == request.form["check_password"]:
                    password_to_encrypt=generate_password_hash(request.form["password"])
                    user_to_add=User(dni=request.form["dni"],name=request.form["name"],surname=request.form["surname"],password=password_to_encrypt,email=request.form["email"])
                    db.session.add(user_to_add)
                    db.session.commit()
                    return redirect(url_for("index_router.login"))
                else:
                    flash("Las constraseñas no coinciden")
                    return render_template("registrarse.html")
            else:
                flash("El email ya se encuentra registrado")
                return render_template("registrarse.html")
        else:
            flash("DNI ya registrado")
            return render_template("registrarse.html")
    return render_template("registrarse.html")

@index_router.route("/home")
def home():
    return render_template("home.html")