# config.py
import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'valm@2023'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://javier:valm2023@192.168.1.199/valm_lite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuraciones para la gestión de sesiones
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'tu_app:'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)

 
#     # config.py
# import os
# from datetime import timedelta

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'valm@2023'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:root@192.168.0.2/bd_valm_lite'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
    
#     # Configuraciones para la gestión de sesiones
#     FLASK_ENV = os.environ.get('FLASK_ENV', 'development')  # Valor por defecto es 'development'

#     SESSION_TYPE = 'filesystem'
#     SESSION_PERMANENT = False
#     SESSION_USE_SIGNER = True
#     SESSION_KEY_PREFIX = 'tu_app:'
#     PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)

#     # if FLASK_ENV == 'production':
#     #     SESSION_COOKIE_SECURE = True
#     #     SESSION_COOKIE_SAMESITE = "None"
#     # else:
#     #     SESSION_COOKIE_SECURE = False
#     #     SESSION_COOKIE_SAMESITE = "Lax"  # Puedes utilizar "Lax" o "Strict" en entornos de desarrollo

#     # SESSION_COOKIE_SECURE = True
#     # SESSION_COOKIE_SAMESITE = "None"

#     SESSION_COOKIE_SECURE = False
#     SESSION_COOKIE_SAMESITE = "Lax"  # Puedes utilizar "Lax" o "Strict" en entornos de desarrollo

