from flask import Flask

# Crear instancia de la aplicación
app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def inicio():
    return '¡Bienvenido! Has iniciado correctamente tu proyecto Flask.'

# Ruta con parámetro dinámico
@app.route('/saludo/<string:usuario>')
def saludo(usuario):
    return f'Hola {usuario}, me alegra verte aquí en la app.'

# Punto de entrada
if __name__ == '__main__':
    # Modo debug activo para desarrollo
    app.run(debug=True)
