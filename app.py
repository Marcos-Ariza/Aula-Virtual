from flask import Flask, redirect, url_for, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_required
from forms import RegistrationForm, ClassForm  # Importa el nuevo formulario ClassForm
from models import db, Persona, Clase  # Asegúrate de importar el nuevo modelo Clase
from config import Config

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicialización de extensiones
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Rutas
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        dni = form.dni.data
        existing_persona = Persona.query.filter_by(dni=dni).first()
        if existing_persona:
            flash('El DNI ya está registrado. Verifica la información ingresada.', 'danger')
        else:
            new_persona = Persona(
                nombre=form.nombre.data,
                dni=form.dni.data,
                email=form.email.data,
                nacimiento=form.nacimiento.data,
                rol=form.rol.data
            )
            try:
                db.session.add(new_persona)
                db.session.commit()
                flash('¡Registro creado exitosamente!', 'success')
                return redirect(url_for('home'))
            except Exception as e:
                db.session.rollback()
                flash('Ocurrió un error al crear el registro.', 'danger')
    
    return render_template('register.html', form=form)

@app.route('/create_class', methods=['GET', 'POST'])
@login_required  # Solo usuarios logueados pueden acceder
def create_class():
    form = ClassForm()
    if form.validate_on_submit():
        new_clase = Clase(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            docente_id=current_user.id  # Asumiendo que current_user tiene el ID del docente
        )
        try:
            db.session.add(new_clase)
            db.session.commit()
            flash('¡Clase creada exitosamente!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash('Ocurrió un error al crear la clase.', 'danger')
    
    return render_template('create_class.html', form=form)

@app.route('/classes')
@login_required  # Solo usuarios logueados pueden acceder
def classes():
    clases = Clase.query.filter_by(docente_id=current_user.id).all()  # Obtener clases del docente actual
    return render_template('classes.html', clases=clases)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)