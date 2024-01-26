from wtforms import form
from wtforms import StringField, TextAreaField, TextField, SelectField, RadioField
from wtforms import EmailField

class UserFind (form):
    nombre = StringField("nombre")
    email = EmailField("correo")
    apeterno = TextField("apaterno")
    materno = SelectField(choices=[('Español','esp'),('Matematica','mat'),('Ingles','ing')])
    radios = RadioField('Curso', choices=[('1','1'),('2','2'),('3','3')])