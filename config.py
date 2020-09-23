import os

# Informo que a classe será um objeto

class Config(object):
    DEBUG = False
    TESTING = False
    #SEGREDO DA APLICAÇÃO
    SECRET_KEY= os.getenv('SECRET_KEY')
    # APLICA O BOOTSTRAP LOCAL (SEM NECESSIDADE DE POR CDN DO BOOTSTRAP)
    BOOTSTRAP_SERVE_LOCAL = True

class ProConfig(Config):
    pass

class DevConfig(Config):
    pass

class TestConfig(Config):
   pass