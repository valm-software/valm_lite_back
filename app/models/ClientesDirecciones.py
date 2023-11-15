from app import db
from datetime import datetime

class ClienteDireccion(db.Model):
    __tablename__ = 'ClientesDirecciones'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    barrio = db.Column(db.String(100), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    cp = db.Column(db.String(10), nullable=False)
    nota = db.Column(db.Text)
    ubicacion = db.Column(db.Text)  # Puede ser un campo para coordenadas u otra información geográfica
    fecha_creado = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificada = db.Column(db.DateTime, onupdate=datetime.utcnow)
    id_usuario = db.Column(db.Integer, nullable=False)