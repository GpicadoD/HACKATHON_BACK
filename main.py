from flask import Flask, send_from_directory, jsonify
from database import db, Perfil, Pista, Valoraciones

app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos con la aplicación Flask
db.init_app(app)

# Crear la base de datos (si no existe)
with app.app_context():
    db.create_all()

# Ruta para servir el archivo index.html desde la carpeta frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

# Ruta para servir archivos estáticos (CSS, JS, imágenes, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('../frontend/static', filename)

# Ruta de ejemplo para obtener todos los perfiles
@app.route('/perfiles')
def listar_perfiles():
    perfiles = Perfil.query.all()
    return jsonify([{'Id': perfil.Id, 'Nombre': perfil.Nombre, 'Categoria': perfil.Categoria, 'Nuevo': perfil.Nuevo} for perfil in perfiles])

# Ruta de ejemplo para obtener todas las pistas
@app.route('/pistas')
def listar_pistas():
    pistas = Pista.query.all()
    return jsonify([{'Id': pista.Id, 'Nombre': pista.Nombre, 'Dificultad': pista.Dificultad} for pista in pistas])

# Ruta de ejemplo para obtener todas las valoraciones
@app.route('/valoraciones')
def listar_valoraciones():
    valoraciones = Valoraciones.query.all()
    return jsonify([{'idValoracion': valoracion.idValoracion, 'IdPerfil': valoracion.IdPerfil, 'IdPista': valoracion.IdPista, 'Valoracion': valoracion.Valoracion, 'FechaValoracion': valoracion.FechaValoracion, 'Comentario': valoracion.Comentario} for valoracion in valoraciones])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)