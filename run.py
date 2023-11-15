#run.py
from flask_cors import CORS
from app import create_app


app = create_app()
CORS(app)
# CORS(app, resources={r"/auth/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True, ssl_context=('localhost.pem', 'localhost-key.pem'))




