from flask import Flask, redirect, url_for, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm  # Asegúrate de tener LoginForm importado
import os

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'seZu8xMTVvnxb5IrTtkO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uc35dobnafnb1kwi:seZu8xMTVvnxb5IrTtkO@bjyltygzpjcyqmru0gwg-mysql.services.clever-cloud.com/bjyltygzpjcyqmru0gwg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Modelo de Usuario
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rutas
@app.route('/')
def home():
    return render_template('home.html')  # Cambia esto según tu plantilla de inicio

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Has iniciado sesión con éxito!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Inicio de sesión fallido. Verifica tu nombre de usuario y contraseña.', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('El nombre de usuario ya está en uso. Elige otro.', 'danger')
        else:
            password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)