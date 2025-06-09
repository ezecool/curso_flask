from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

products = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

@app.route('/')
def index():
  user_ip_information = request.remote_addr
  response = make_response(redirect('/show_information'))
  response.set_cookie('user_ip_information', user_ip_information)
  return response


@app.route('/show_information')
def show_information():
  user_ip_information = request.cookies.get('user_ip_information')
  context = {
    'user_ip_information': user_ip_information,
    'products': products
  }
  return render_template('information.html', **context)


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html', error=e)


app.run(host='0.0.0.0', port=5000, debug=True)

