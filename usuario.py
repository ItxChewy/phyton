from database import db
from sqlalchemy.sql import func

# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from estudiante import Estudiante
# app.app_context().push()
# db.create_all()

class Usuario(db.Model):
    
    __tablename__ = 'usuario'
         
    id = db.Column(db.Integer, primary_key=True)
    nombreusuario = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)

    def __init__(self, nombreusuario, nombre, contraseña):
        self.nombreusuario = nombreusuario
        self.nombre = nombre
        self.contraseña = contraseña

    def __repr__(self):
        return f'<Usuario {self.id}>: {self.nombre}'
    
    