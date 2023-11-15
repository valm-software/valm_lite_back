#authController.py
from flask import Blueprint, request, session, jsonify, make_response
from ..services.authService import authenticate, get_user_permissions, crear_usuario, build_menu, cambiar_contrasena
from ..helpers.permissions import require_permission  # Importa el decorador
from ..helpers.api_response_builder import build_api_response

from flask import current_app

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    auth_result = authenticate(username, password)

    if auth_result['status'] == 'success':
            session.permanent = True 
            user_id = auth_result['data']['id']
            session['user_id'] = user_id
            session['username'] = auth_result['data']['username']
            
            # Construir el menú
            menu_structure = build_menu(user_id)
            
            # Construir la respuesta completa incluyendo el menú, el username y el id
            response_data = {
                'id': user_id,
                'username': session['username'],                
                'menu': menu_structure, 
            }
            
            return build_api_response('success', 'Inicio de sesión exitoso', 200, response_data)
    else:
            return build_api_response('error', auth_result['message'], 401)  

@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return make_response(jsonify({'message': 'Sesión cerrada exitosamente'}), 200)

@auth.route('/check_session', methods=['GET'])
def check_session():
    if 'user_id' in session and 'username' in session:
        user_id = session['user_id']
        username = session['username']

        menu_structure = build_menu(user_id)
        
        # Construyendo la estructura de datos del usuario para enviar al frontend
        user_data = {
            'id': user_id,
            'username': username,
            'menu': menu_structure
        }
        
        return build_api_response('authenticated', 'Sesión autenticada', 200, {'userData': user_data})
    else:
        return build_api_response('error', 'Sesión no autenticada', 401)

@auth.route('/usuarioCrear', methods=['POST'])
def usuario_crear():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"status": "error", "message": "Faltan campos obligatorios"}), 400

    resultado = crear_usuario(username, password)
    
    if resultado['status'] == 'success':
        return jsonify(resultado), 201
    else:
        return jsonify(resultado), 400

@auth.route('/cambiarContrasena', methods=['POST'])
def cambiar_contrasena_endpoint():
    data = request.get_json()
    username = data.get('username')
    nueva_contrasena = data.get('nuevaContrasena')
    
    resultado = cambiar_contrasena(username, nueva_contrasena)
    
    if resultado['status'] == 'success':
        return build_api_response('success', 'Contraseña actualizada exitosamente', 200)
    else:
        return build_api_response('error', 'No se pudo actualizar la contraseña', 400)