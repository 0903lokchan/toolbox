from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.dice_cal import bp as dice_cal_bp
    app.register_blueprint(dice_cal_bp)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app.main import routes