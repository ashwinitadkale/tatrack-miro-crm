from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.inquiries import inquiries_bp
    from app.routes.reminders import reminders_bp

    app.register_blueprint(inquiries_bp)
    app.register_blueprint(reminders_bp)


    @app.route("/")
    def home():
        return {"status": "TatTrack CRM backend running"}




    return app
