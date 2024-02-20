from flask import Flask,request,render_template, Response
import forms
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g

app = Flask(__name__)
app.secret_key = "esta es la clave secreta"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.before_request
def before_request():
    g.prueba = 'hola'
    print("despues de la ruta 1")

@app.route("/")
def INDEX():
    return render_template("index.html")

@app.route("/alumnos",methods=("GET","POST"))
def alumnos():
    print('despues de la ruta 2')
    valor = g.prueba
    print('el dato es:{}'.format(valor))
    alum_forms=forms.UserForm(request.form)
    nom = ''
    apa = ''
    email = ''
    
    if request.method=='POST' and alum_forms.validate():
      nom = alum_forms.nombre.data
      apa = alum_forms.apaterno.data
      email = alum_forms.email.data
      
      messages = 'Bienvenido {}'.format(nom)
      flash(messages)
      
      print("Nombre: {}".format(nom))
      print("Apellido: {}".format(apa))
      print("Correo: {}".format(email))
    return render_template("alumnos.html", form=alum_forms,nom=nom,apa=apa,email=email)

@app.after_request
def after_request(response):
    print("despues de la ruta 3")

@app.route("/maestros")
def INDEX3():
    return render_template("maestros.html")

@app.route("/")
def hola():
    return "<p> Hola Mundo </p>"

@app.route("/hola")
def hola2():
    return "<h1> Saludo desde Hola </h1>"

@app.route("/saludo")
def hola3():
    return "<h1> Saludo desde saludo </h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola</h1>" + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1>EL valor es {}</h1>".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def nomYid(nom,id):
    return "<h1>ID:{} NOMBRE:{}</h1>".format(id,nom)

@app.route("/sume/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "<h1>La sume de {} + {} = {}</h1>".format(n1,n2, n1+n2)

@app.route("/multiplicar",methods=("GET","POST"))
def mult():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1> El resultado es: {}</h1>".format(str(int(num1)*int(num2)))
    else:
        return '''
        <form  action="/multiplicar" method="POST">
        <label>N1:</label>
        <input type="text" name="n1">
        <label>N2:</label>
        <input type="text" name="n2">
        <input type="submit">
        </form>
        '''
    
@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado",methods=("GET","POST"))
def res():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        
        
        return "<h1> El resultado es: {}</h1>".format(str(int(num1)*int(num2)))

if __name__ == "__main__":
    app.run(debug = True)