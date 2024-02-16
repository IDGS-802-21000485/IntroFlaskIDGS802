from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class UserForm(Form):
    '''nombreSelc = SelectField("Nombre")
    nombre = StringField("Nombre")
    email = EmailField("Correo")
    apaterno = StringField("Apaterno")
    materias = SelectField(choices=[("Espanol", "Esp",), ("Mat", "matematicas"), ('Ingles', 'ING')])
    radios = RadioField('Curso', choices=[('1', '1'), ('2','2'), ('3','3')])
    '''
    
    nombre=StringField('nombre',[
        validators.DataRequired(message='el compo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')
    ])
    apaterno=StringField('apeterno')
    amaterno=StringField('amaterno')
    edad = IntegerField('edad',[
        validators.number_range(min = 1,max=10,message='valor no valido')
    ])
    email = StringField('Correo',[
        validators.email(message='Correo no valido')
    ])
    