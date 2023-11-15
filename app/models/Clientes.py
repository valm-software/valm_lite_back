from app import db
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = 'Clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    fechaCreado = db.Column(db.DateTime, default=datetime.utcnow)
    fechaModificada = db.Column(db.DateTime, onupdate=datetime.utcnow)
    idUsuario = db.Column(db.Integer, nullable=False)

    ClientesTelefonos = db.relationship('ClienteTelefono', backref='cliente', lazy=True)
    ClientesDirecciones = db.relationship('ClienteDireccion', backref='cliente', lazy=True)