# config.py
import os
from datetime import timedelta

class Config:
    # CORS_ORIGINS = "*" 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'valm@2023'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://javier:valm2023@192.168.1.199/valm_lite'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:root@192.168.0.3/valm_lite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuraciones para la gestión de sesiones
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'valm:'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)

 