class BaseConfig(object):
<<<<<<< HEAD
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'makesure to set a very secret key'
    INDEX_PER_PAGE=9
    ADMIN_PER_PAGE=15
   
=======
    SECRET_KEY = 'makesure to set a very secret key'

>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

