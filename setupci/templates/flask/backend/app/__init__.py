import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class="app.config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from app.api.items import items_bp
    app.register_blueprint(items_bp, url_prefix="/api/v1/items")

    # Simple root healthcheck
    @app.route("/")
    def index():
        return {"status": "ok", "message": "Welcome to Flask Professional Backend"}

    return app
