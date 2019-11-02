import os
from flaskapp import db, create_app
from flask_migrate import Migrate, upgrade, init

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app,db)

def update():
    with app.app_context():
        upgrade()