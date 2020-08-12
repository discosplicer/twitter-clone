from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter-clone.db"

db = SQLAlchemy(app)
@app.route('/')
def index():
    """
    Returns what's in the index. Right now this is just Hello World.
    """
    db.create_all()
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True) # restarts the server when code changes