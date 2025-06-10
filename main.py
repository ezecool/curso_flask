from flask import Flask, request, make_response, redirect, render_template, session
from flask_wtf import FlaskForm

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la clave secreta para las sesiones
app.config['SECRET_KEY'] = 'your_secret_key'

products = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Clase para el formulario de Login
class LoginForm(FlaskForm):
  pass
  

@app.route('/')
def index():
  user_ip_information = request.remote_addr
  response = make_response(redirect('/show_information'))
  #response.set_cookie('user_ip_information', user_ip_information)  
  # El objeto session esta incluido en la respuesta
  session['user_ip_information'] = user_ip_information
  return response


@app.route('/show_information')
def show_information():
  #user_ip_information = request.cookies.get('user_ip_information')
  # Obtener la información del usuario desde la sesión
  user_ip_information = session.get('user_ip_information', 'Unknown IP')
  context = {
    'user_ip_information': user_ip_information,
    'products': products
  }
  return render_template('information.html', **context)


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html', error=e)


app.run(host='0.0.0.0', port=5000, debug=True)

