from flask import Flask, render_template, url_for

app = Flask(__name__)

# Filtros personalizados
@app.add_template_filter
def filtro_today(date):
    return date.strftime('%d/%m/%Y')

# app.add_template_filter(filtro_today, 'filtro_today')

# funciones personalizadas
@app.add_template_global
def repeat(string, numero_veces):
    return string * numero_veces

# app.add_template_global(repeat, 'repeat') Es otra manera de hacerlo
#--------------------------------------------

from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    name = 'Irene'
    friends = ['Juan', 'Pedro', 'Luis']
    current_data = datetime.now()
    return render_template(
        'index.html',
        name = name,
        friends = friends,
        date=current_data
    )

@app.route('/hello/')
@app.route('/hello/<name>/')
@app.route('/hello/<name>/<int:age>/')
@app.route('/hello/<name>/<int:age>/<email>/')
def hello(name = None, age = None, email = None):
    my_data= {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data = my_data)

#Bloque raro
# --------------------------------
from markupsafe import escape

# Para mostrar código sin ejecutar (no sé cuando lo voy a usar: nunca.)
# Solo podría usarlo si alguien muy listo (poco probable) intentase atacar mi página web.
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
# -------------------------------------------