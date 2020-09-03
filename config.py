import os

# Informo que a classe será um objeto

class Config(object):
    DEBUG = False
    TESTING = False
    #SEGREDO DA APLICAÇÃO
    SECRET_KEY= os.getenv('SECRET_KEY')
    # APLICA O BOOTSTRAP LOCAL (SEM NECESSIDADE DE POR CDN DO BOOTSTRAP)
    BOOTSTRAP_SERVE_LOCAL = True

class proConfig(Config):
     pass

class devConfig(Config):
    pass

class testConfig(Config):
   pass