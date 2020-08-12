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
