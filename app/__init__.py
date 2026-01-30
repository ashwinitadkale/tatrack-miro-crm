from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager # Add this

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager() # Add this

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app) # Add this
    login_manager.login_view = "auth.login" # Redirect here if login required

    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register the new auth blueprint (created in next step)
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.inquiries import inquiries_bp
    from app.routes.reminders import reminders_bp
    from app.routes.sessions import sessions_bp

    app.register_blueprint(inquiries_bp)
    app.register_blueprint(reminders_bp)
    app.register_blueprint(sessions_bp)

    @app.route("/")
    def home():
        return {"status": "TatTrack CRM backend running"}

    return app