from flask import Flask, render_template
from jobplus.config import configs
from jobplus.models import db,User,Company
from flask_migrate import Migrate
from flask_login import LoginManager
def register_blueprints(app):
<<<<<<< HEAD
    from .handlers import front, admin,user,company,job
=======
    from .handlers import front, admin,user,company
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(user) 
    app.register_blueprint(company)
<<<<<<< HEAD
    app.register_blueprint(job)
=======
>>>>>>> ead018915caac62e47b76c3778fa36791cdf20a3
def register_extensions(app):   
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    login_manager.login_view = 'front.login'

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    return app
