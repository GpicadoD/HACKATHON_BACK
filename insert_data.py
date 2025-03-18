# backend/insert_data.py
from datetime import datetime
from database import db, Perfil, Pista, Valoraciones

# Función para insertar datos de ejemplo
def insertar_datos_ejemplo():
    # Insertar perfiles
    perfiles = [
        Perfil(Nombre='Juan Pérez', Categoria='Avanzado', Nuevo=False),
        Perfil(Nombre='Ana Gómez', Categoria='Intermedio', Nuevo=True),
        Perfil(Nombre='Carlos López', Categoria='Principiante', Nuevo=True),
        Perfil(Nombre='María Fernández', Categoria='Avanzado', Nuevo=False),
        Perfil(Nombre='Pedro Martínez', Categoria='Intermedio', Nuevo=True),
        Perfil(Nombre='Laura Sánchez', Categoria='Principiante', Nuevo=True),
        Perfil(Nombre='David Romero', Categoria='Avanzado', Nuevo=False),
        Perfil(Nombre='Sofía Herrera', Categoria='Intermedio', Nuevo=True),
        Perfil(Nombre='Miguel Torres', Categoria='Principiante', Nuevo=True),
        Perfil(Nombre='Elena Ruiz', Categoria='Avanzado', Nuevo=False),
    ]
    db.session.add_all(perfiles)

    # Insertar pistas
    pistas = [
        Pista(Nombre='Gallinero', Dificultad='Negra'),
        Pista(Nombre='Cogulla', Dificultad='Roja'),
        Pista(Nombre='Basibé', Dificultad='Roja'),
        Pista(Nombre='Robellons', Dificultad='Verde'),
        Pista(Nombre='La Olla', Dificultad='Negra'),
        Pista(Nombre='Ampriu', Dificultad='Verde'),
        Pista(Nombre='El Molino', Dificultad='Azul'),
        Pista(Nombre='Rincón del Cielo', Dificultad='Roja'),
        Pista(Nombre='Fontanals', Dificultad='Azul'),
        Pista(Nombre='Barranco', Dificultad='Roja'),
        Pista(Nombre='Telesilla Batisielles', Dificultad='Azul'),
        Pista(Nombre='Sarrau', Dificultad='Negra'),
        Pista(Nombre='Cibollés', Dificultad='Roja'),
        Pista(Nombre='Tubo de Gallinero', Dificultad='Negra'),
        Pista(Nombre='Pico Cerler', Dificultad='Negra'),
        Pista(Nombre='Perdiz Blanca', Dificultad='Azul'),
        Pista(Nombre='Quebrantahuesos', Dificultad='Roja'),
        Pista(Nombre='Canal Amplia', Dificultad='Negra'),
        Pista(Nombre='Escuela', Dificultad='Verde'),
    ]
    db.session.add_all(pistas)

    # Insertar valoraciones
    valoraciones = [
        Valoraciones(IdPerfil=1, IdPista=1, Valoracion=5, FechaValoracion=datetime(2024, 3, 18, 10, 0, 0), Comentario='Increíble vista y muy técnica.'),
        Valoraciones(IdPerfil=2, IdPista=2, Valoracion=4, FechaValoracion=datetime(2024, 3, 18, 11, 0, 0), Comentario='Muy divertida y bien pisada.'),
        Valoraciones(IdPerfil=3, IdPista=3, Valoracion=3, FechaValoracion=datetime(2024, 3, 18, 12, 0, 0), Comentario='Algo complicada para mi nivel.'),
        Valoraciones(IdPerfil=4, IdPista=4, Valoracion=5, FechaValoracion=datetime(2024, 3, 18, 13, 0, 0), Comentario='Perfecta para esquiar relajado.'),
        Valoraciones(IdPerfil=5, IdPista=5, Valoracion=4, FechaValoracion=datetime(2024, 3, 18, 14, 0, 0), Comentario='Difícil pero muy emocionante.'),
        Valoraciones(IdPerfil=6, IdPista=6, Valoracion=5, FechaValoracion=datetime(2024, 3, 18, 15, 0, 0), Comentario='Ideal para principiantes, me encantó.'),
        Valoraciones(IdPerfil=7, IdPista=7, Valoracion=4, FechaValoracion=datetime(2024, 3, 18, 16, 0, 0), Comentario='Me gustó el desnivel de la pista.'),
        Valoraciones(IdPerfil=8, IdPista=8, Valoracion=5, FechaValoracion=datetime(2024, 3, 18, 17, 0, 0), Comentario='Una de las mejores pistas de la estación.'),
        Valoraciones(IdPerfil=9, IdPista=9, Valoracion=3, FechaValoracion=datetime(2024, 3, 18, 18, 0, 0), Comentario='Algo complicada para un principiante, pero muy divertida.'),
        Valoraciones(IdPerfil=10, IdPista=10, Valoracion=5, FechaValoracion=datetime(2024, 3, 18, 19, 0, 0), Comentario='Fantástica, con una vista espectacular.'),
    ]
    db.session.add_all(valoraciones)

    # Guardar los cambios en la base de datos
    db.session.commit()

# Si ejecutas este archivo directamente, se insertarán los datos
if __name__ == '__main__':
    from main import app  # Importar la aplicación Flask
    with app.app_context():
        insertar_datos_ejemplo()  # Insertar datos de ejemplo