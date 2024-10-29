from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    nombre = StringField('Nombre', 
                         validators=[DataRequired(message='Este campo es obligatorio.'),
                                     Length(min=2, max=150, 
                                            message='El nombre debe tener entre 2 y 150 caracteres.')])
    
    dni = StringField('DNI', 
                      validators=[DataRequired(message='Este campo es obligatorio.'),
                                  Length(min=7, max=20, 
                                         message='El DNI debe tener entre 7 y 20 caracteres.')])
    
    email = StringField('Correo Electrónico', 
                        validators=[DataRequired(message='Este campo es obligatorio.'),
                                    Email(message='Ingresa un correo electrónico válido.')])
    
    nacimiento = DateField('Fecha de Nacimiento', 
                           validators=[DataRequired(message='Este campo es obligatorio.')],
                           format='%Y-%m-%d')
    
    rol = SelectField('Rol', 
                      choices=[('maestro', 'Maestro'), ('alumno', 'Alumno')],
                      validators=[DataRequired(message='Este campo es obligatorio.')])
    
    submit = SubmitField('Registrar')

class ClassForm(FlaskForm):
    nombre = StringField('Nombre de la Clase', 
                         validators=[DataRequired(message='Este campo es obligatorio.'),
                                     Length(min=2, max=100, message='El nombre debe tener entre 2 y 100 caracteres.')])
    
    descripcion = TextAreaField('Descripción', 
                                 validators=[Length(max=250, message='La descripción no debe exceder 250 caracteres.')])
    
    submit = SubmitField('Crear Clase')