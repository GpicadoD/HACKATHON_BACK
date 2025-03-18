--
-- Archivo generado con SQLiteStudio v3.4.17 el ma. mar. 18 17:04:32 2025
--
-- Codificación de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: Perfil
DROP TABLE IF EXISTS Perfil;

CREATE TABLE IF NOT EXISTS Perfil (
    Id        INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre    TEXT    NOT NULL,
    Categoria TEXT    NOT NULL,
    Nuevo     BOOLEAN NOT NULL
);

INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (1, 'Juan Pérez', 'Avanzado', 0);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (2, 'Ana Gómez', 'Intermedio', 1);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (3, 'Carlos López', 'Principiante', 1);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (4, 'María Fernández', 'Avanzado', 0);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (5, 'Pedro Martínez', 'Intermedio', 1);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (6, 'Laura Sánchez', 'Principiante', 1);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (7, 'David Romero', 'Avanzado', 0);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (8, 'Sofía Herrera', 'Intermedio', 1);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (9, 'Miguel Torres', 'Principiante', 1);
INSERT INTO Perfil (Id, Nombre, Categoria, Nuevo) VALUES (10, 'Elena Ruiz', 'Avanzado', 0);

-- Tabla: Pista
DROP TABLE IF EXISTS Pista;

CREATE TABLE IF NOT EXISTS Pista (
    Id         INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre     TEXT    NOT NULL,
    Dificultad TEXT    NOT NULL
);

INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (1, 'Gallinero', 'Negra');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (2, 'Cogulla', 'Roja');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (3, 'Basibé', 'Roja');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (4, 'Robellons', 'Verde');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (5, 'La Olla', 'Negra');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (6, 'Ampriu', 'Verde');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (7, 'El Molino', 'Azul');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (8, 'Rincón del Cielo', 'Roja');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (9, 'Fontanals', 'Azul');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (10, 'Barranco', 'Roja');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (11, 'Telesilla Batisielles', 'Azul');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (12, 'Sarrau', 'Negra');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (13, 'Cibollés', 'Roja');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (14, 'Tubo de Gallinero', 'Negra');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (15, 'Pico Cerler', 'Negra');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (16, 'Perdiz Blanca', 'Azul');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (17, 'Quebrantahuesos', 'Roja');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (18, 'Canal Amplia', 'Negra');
INSERT INTO Pista (Id, Nombre, Dificultad) VALUES (19, 'Escuela', 'Verde');

-- Tabla: Valoraciones
DROP TABLE IF EXISTS Valoraciones;

CREATE TABLE IF NOT EXISTS Valoraciones (
    idValoracion    INTEGER  PRIMARY KEY AUTOINCREMENT,
    IdPerfil        INTEGER  NOT NULL,
    IdPista         INTEGER  NOT NULL,
    Valoracion      INTEGER  NOT NULL,
    FechaValoracion DATETIME NOT NULL,
    Comentario      TEXT,
    FOREIGN KEY (
        IdPerfil
    )
    REFERENCES Perfil (Id),
    FOREIGN KEY (
        IdPista
    )
    REFERENCES Pista (Id) 
);

INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (1, 1, 1, 5, '2024-03-18 10:00:00', 'Increíble vista y muy técnica.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (2, 2, 2, 4, '2024-03-18 11:00:00', 'Muy divertida y bien pisada.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (3, 3, 3, 3, '2024-03-18 12:00:00', 'Algo complicada para mi nivel.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (4, 4, 4, 5, '2024-03-18 13:00:00', 'Perfecta para esquiar relajado.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (5, 5, 5, 4, '2024-03-18 14:00:00', 'Difícil pero muy emocionante.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (6, 6, 6, 5, '2024-03-18 15:00:00', 'Ideal para principiantes, me encantó.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (7, 7, 7, 4, '2024-03-18 16:00:00', 'Me gustó el desnivel de la pista.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (8, 8, 8, 5, '2024-03-18 17:00:00', 'Una de las mejores pistas de la estación.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (9, 9, 9, 3, '2024-03-18 18:00:00', 'Algo complicada para un principiante, pero muy divertida.');
INSERT INTO Valoraciones (idValoracion, IdPerfil, IdPista, Valoracion, FechaValoracion, Comentario) VALUES (10, 10, 10, 5, '2024-03-18 19:00:00', 'Fantástica, con una vista espectacular.');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
