# AuthUsuariosPermisos.py

from app import db

class AuthUsuariosPermisos(db.Model):
    __tablename__ = 'AuthUsuariosPermisos'
    
    id = db.Column(db.Integer, primary_key=True)
    usuarioId = db.Column(db.Integer, db.ForeignKey('AuthUsuarios.id'))
    permisoId = db.Column(db.Integer, db.ForeignKey('AuthPermisos.id'))

    def __repr__(self):
        return f'<AuthUsuariosPermisos usuarioId={self.usuarioId}, permisoId={self.permisoId}>'
