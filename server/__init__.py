from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .utils.telegram_sender import send_message

db = SQLAlchemy()


def create_app():
    send_message("The app is starting")

    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    # Registrer blueprint
    from .auth import auth as auth_blueprint
    from .bets import bets as bets_blueprint
    from .results import results as results_blueprint
    from .groups import groups as groups_blueprint
    from .final_phase import final_phase as final_phase_blueprint
    from .teams import teams as teams_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(bets_blueprint)
    app.register_blueprint(results_blueprint)
    app.register_blueprint(groups_blueprint)
    app.register_blueprint(final_phase_blueprint)
    app.register_blueprint(teams_blueprint)

    CORS(app, resources={r"/*": {"origins": "*"}})

    return app
