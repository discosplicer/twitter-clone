from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter-clone.db"

# Define Database
db = SQLAlchemy(app)
class Users(db.Model):
    """
    ID = primary key, unique identifier
    Also stored: Username, password, emails
    """
    id = db.Column('id', db.Integer, primary_key = True) 
    username = db.Column(db.String(24))
    email = db.Column(db.String(64))
    pwd = db.Column(db.String(64))

    def __init__(self, username, email, pwd):
        """
        Creates new database entry.
        """
        self.username = username
        self.email = email
        self.pwd = pwd

@app.route('/')
def index():
    """
    Returns what's in the index. Right now this is just Hello World.
    """
    db.create_all()
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True) # restarts the server when code changes