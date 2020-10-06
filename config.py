import os
from datetime import timedelta

# Informo que a classe será um objeto

class Config(object):
    TESTING = False
    #SEGREDO DA APLICAÇÃO
    SECRET_KEY= os.getenv('SECRET_KEY')
    # APLICA O BOOTSTRAP LOCAL (SEM NECESSIDADE DE POR CDN DO BOOTSTRAP)
    BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bigBox.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME =  timedelta(minutes=1)
    
class ProConfig(Config):
    pass    

class DevConfig(Config):
    pass

class TestConfig(Config):
   pass