#authService.py
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app
from app.models.all_models import AuthUsuario, AuthPermiso, AuthUsuariosPermisos
from app import db  # Importar db desde app
from collections import defaultdict

def authenticate(username, password):
    with current_app.app_context():
        user = AuthUsuario.query.filter_by(nombreUsuario=username).first()
        
        if not user:
            return {'status': 'error', 'message': 'Usuario no encontrado'}
        
        password_check = check_password_hash(user.contrasenaHash, password)
        
        if password_check:
            return {'status': 'success', 'data': {'id': user.id, 'username': user.nombreUsuario}}
        else:
            return {'status': 'error', 'message': 'Contraseña incorrecta'}

def get_user_permissions(user_id):
    with current_app.app_context():
        permissions = AuthPermiso.query.\
                    join(AuthUsuariosPermisos, AuthUsuariosPermisos.permisoId == AuthPermiso.id).\
                    filter(AuthUsuariosPermisos.usuarioId == user_id).all()

        # Usamos un diccionario para agrupar los permisos por módulo
        grouped_permissions = defaultdict(list)

        for perm in permissions:
            grouped_permissions[perm.menu].append(perm.permissions)

        # Convertimos el diccionario a formato JSON
        menu_json = {menu: perms for menu, perms in grouped_permissions.items()}

        return {'menu': menu_json}

def build_menu(user_id):
    permissions = get_user_permissions(user_id)
    menu_structure = {}  # Aquí puedes construir tu menú como más te convenga

    # Asegurarse de que 'menu' está en permissions y es un diccionario
    if 'menu' in permissions and isinstance(permissions['menu'], dict):
        for menu_item, actions in permissions['menu'].items():
            menu_structure[menu_item] = actions

    return menu_structure

def crear_usuario(username, password):
    # Verificar si el usuario ya existe
    usuario_existente = AuthUsuario.query.filter_by(nombreUsuario=username).first()
    
    if usuario_existente:
        return {"status": "error", "message": "El usuario ya existe"}
    
    nuevo_usuario = AuthUsuario(nombreUsuario=username)
    nuevo_usuario.asignarContrasena(password)  # No doble hash
    
    db.session.add(nuevo_usuario)  # Utilizar db.session
    db.session.commit()
    
    return {"status": "success", "message": "Usuario creado exitosamente"}

def cambiar_contrasena(username, nueva_contrasena):
    with current_app.app_context():
        user = AuthUsuario.query.filter_by(nombreUsuario=username).first()
        
        if not user:
            return {"status": "error", "message": "Usuario no encontrado"}
        
        try:
            user.asignarContrasena(nueva_contrasena)
            AuthUsuario.query.session.commit()
            return {"status": "success", "message": "Contraseña actualizada exitosamente"}
        except Exception as e:
            current_app.logger.error(f"Error al actualizar la contraseña: {e}")
            return {"status": "error", "message": "No se pudo actualizar la contraseña"}

