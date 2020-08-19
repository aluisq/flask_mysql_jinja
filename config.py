# Informo que a classe será um objeto

class Config(object):
    DEBUG = False
    TESTING = False
    #SEGREDO DA APLICAÇÃO
    SECRET_KEY = '!@unimed'
    # APLICA O BOOTSTRAP LOCAL (SEM NECESSIDADE DE POR CDN DO BOOTSTRAP)
    BOOTSTRAP_SERVE_LOCAL = True

class proConfig(Config):
     pass

class devConfig(Config):
    DB_NAME =
    DB_USERNAME = 
    DB_PASSWORD = 

class testConfig(Config):
    DB_NAME =
    DB_USERNAME = 
    DB_PASSWORD = 