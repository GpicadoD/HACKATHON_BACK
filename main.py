from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definir un modelo de ejemplo
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

# Crear la base de datos
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)