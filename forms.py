from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(message='Este campo es obligatorio.'),
                                       Length(min=2, max=20, 
                                              message='El nombre de usuario debe tener entre 2 y 20 caracteres.')])
    
    password = PasswordField('Password', 
                             validators=[DataRequired(message='Este campo es obligatorio.')])
    
    confirm_password = PasswordField('Confirm Password', 
                                      validators=[DataRequired(message='Este campo es obligatorio.'),
                                                  EqualTo('password', message='Las contraseñas deben coincidir.')])
    
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(message='Este campo es obligatorio.')])
    
    password = PasswordField('Password', 
                             validators=[DataRequired(message='Este campo es obligatorio.')])
    
    submit = SubmitField('Login')