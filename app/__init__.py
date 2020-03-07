from flask import Flask

from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)

    from app.dice_cal import bp as dice_cal_bp
    app.register_blueprint(dice_cal_bp)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    return app

from app.main import routes