from flask import Flask, send_from_directory, jsonify
from database import db, Usuario

app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos con la aplicacion de Flask
db.init_app(app)

# Crear la base de datos (si no existe)
with app.app_context():
    db.create_all()
    
# Ruta para servir el archivo index.html desde la carptea frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

# Ruta para servir archivos estaticos (CSS, JS, imagenes, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('../frontend/static', filename)

# Ruta de ejemplo para interactuar con la base de datos
@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': usuario.id, 'nombre': usuario.nombre} for usuario in usuarios])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
