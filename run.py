import os
from flaskapp import create_app, mongodb

app = create_app(os.getenv("FLASK_CONFIG") or "default")

@app.shell_context_processor
def make_shell_context():
    return dict(mongodb=mongodb)