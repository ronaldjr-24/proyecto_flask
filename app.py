from flask import Flask, render_template

# Creamos la aplicación
web = Flask(__name__)

# Ruta de inicio
@web.route('/')
def inicio():
    return '¡Bienvenido! Has iniciado correctamente tu proyecto Flask.'

# Ruta con parámetro dinámico
@web.route('/saludo/<usuario>')
def saludo(usuario):
    return f'Hola {usuario}, me alegra verte aquí en la app.'

# Punto de entrada
if __name__ == '__main__':
    # Modo debug activo para desarrollo
    web.run(debug=True)