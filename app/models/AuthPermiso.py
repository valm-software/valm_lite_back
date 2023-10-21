# AuthPermiso.py

from app import db

class AuthPermiso(db.Model):
    __tablename__ = 'AuthPermisos'
    
    id = db.Column(db.Integer, primary_key=True)  
    menu = db.Column(db.String(64))
    permissions = db.Column(db.String(64))
    controlador = db.Column(db.String(64))
    metodoHTTP = db.Column(db.String(10)) 
    ruta = db.Column(db.String(256))
    descripcion = db.Column(db.String(256))
    isActive = db.Column(db.Boolean, default=True)
    
    # Relaciones
    # usuarios = db.relationship('AuthUsuario', secondary='AuthUsuariosPermisos', lazy='subquery',
    #                            backref=db.backref('permisos', lazy=True))

    def __repr__(self):
        return f'<AuthPermiso {self.nombre}>'
