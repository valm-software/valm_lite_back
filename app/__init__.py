# __init__.py
from flask import Flask
from flask_cors import CORS  
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from dotenv import load_dotenv  # Importa la función load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()

# Inicializamos las extensiones sin pasar la aplicación
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    # CORS(app)
    CORS(app, supports_credentials=True)
    

    # CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}) // restringir a un origen

    app.config.from_object(config_class)
    print(config_class)

    # Inicializamos las extensiones con la aplicación
    db.init_app(app)
    migrate.init_app(app, db)
    Session(app)

    # Importación tardía de los modelos y controladores
    with app.app_context():
        from app.models import all_models  # Importa todos los modelos a través de un único archivo
        from .controllers import authController, ventasController  # Importación tardía de los controladores
        app.register_blueprint(authController.auth, url_prefix='/auth')  # Registro del Blueprint de autenticación
        app.register_blueprint(ventasController.ventas, url_prefix='/ventas')  # Registro del Blueprint de ventas

    return app
