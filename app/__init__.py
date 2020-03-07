from flask import Flask
from config import Config

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.dice_cal import bp as dice_cal_bp
    app.register_blueprint(dice_cal_bp)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    return app

from app.main import routes