#permissions.py
from flask import session, jsonify, make_response
from functools import wraps

# Decorador para requerir un permiso específico
def require_permission(permission_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Verificamos si el usuario tiene el permiso requerido
            if 'permissions' not in session or permission_name not in [perm['permissions'] for perm in session['permissions']]:
                return make_response(jsonify({'message': 'Permiso denegado'}), 403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
