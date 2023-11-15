from app import db
from datetime import datetime

class ClienteTelefono(db.Model):
    __tablename__ = 'ClientesTelefonos'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    numero_telefono = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    principal = db.Column(db.Boolean, default=False)
    permite_wa = db.Column(db.Boolean, default=False)
    fecha_creado = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificada = db.Column(db.DateTime, onupdate=datetime.utcnow)
    id_usuario = db.Column(db.Integer, nullable=False)
