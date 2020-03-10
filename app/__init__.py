from flask import Flask
from config import Config

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.dice_cal import bp as dice_cal_bp
    app.register_blueprint(dice_cal_bp)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.post_wall import bp as post_wall_bp
    app.register_blueprint(post_wall_bp)


    return app

from app.main import routes
from app.post_wall import models