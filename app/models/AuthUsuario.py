# AuthUsuario.py

from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class AuthUsuario(db.Model):
    __tablename__ = 'AuthUsuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(64), unique=True)
    contrasenaHash = db.Column(db.String(128))
    
    # Relaciones
    # permisos = db.relationship('AuthPermiso', secondary='AuthUsuariosPermisos', lazy='subquery',
    #                            backref=db.backref('usuarios', lazy=True))
    permisos = db.relationship('AuthPermiso', secondary='AuthUsuariosPermisos', lazy='subquery')


    def asignarContrasena(self, contrasena):
        self.contrasenaHash = generate_password_hash(contrasena)

    def verificarContrasena(self, contrasena):
        return check_password_hash(self.contrasenaHash, contrasena)

    def __repr__(self):
        return f'<AuthUsuario {self.nombreUsuario}>'
