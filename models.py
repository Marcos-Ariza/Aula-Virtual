from flask_sqlalchemy import SQLAlchemy

# Inicialización de la instancia de SQLAlchemy
db = SQLAlchemy()

# Modelo de Persona
class Persona(db.Model):
    __tablename__ = 'personas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    dni = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    nacimiento = db.Column(db.Date, nullable=False)
    rol = db.Column(db.String(50), nullable=False)  # Ejemplo: "maestro" o "alumno"
    
    clases = db.relationship('Clase', backref='persona', lazy=True)  # Relación con las clases

    def __repr__(self):
        return f'<Persona {self.nombre}>'

# Modelo de Clase
class Clase(db.Model):
    __tablename__ = 'clases'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(250), nullable=True)
    docente_id = db.Column(db.Integer, db.ForeignKey('personas.id'), nullable=False)  # ID del docente que enseña la clase
    alumnos = db.relationship('Persona', secondary='clase_alumno', backref='clases')  # Relación con alumnos

class ClaseAlumno(db.Model):
    __tablename__ = 'clase_alumno'
    
    clase_id = db.Column(db.Integer, db.ForeignKey('clases.id'), primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('personas.id'), primary_key=True)