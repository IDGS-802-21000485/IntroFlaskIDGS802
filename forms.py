from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class UserForm(Form):
    nombreSelc = SelectField("Nombre")
    nombre = StringField("Nombre")
    email = EmailField("Correo")
    apaterno = StringField("Apaterno")
    materias = SelectField(choices=[("Espanol", "Esp",), ("Mat", "matematicas"), ('Ingles', 'ING')])

    radios = RadioField('Curso', choices=[('1', '1'), ('2','2'), ('3','3')])