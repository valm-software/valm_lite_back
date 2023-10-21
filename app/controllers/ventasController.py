from flask import Blueprint, jsonify

ventas = Blueprint('ventas', __name__)

@ventas.route('/ventaNueva', methods=['POST'])
def venta_nueva():
    return jsonify({'message': 'Nuevo punto de venta'})

@ventas.route('/ventaModificar', methods=['POST'])
def venta_modificar():
    return jsonify({'message': 'Modificar venta'})
