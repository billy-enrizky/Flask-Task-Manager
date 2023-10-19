from app import app, db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    desc = db.Column(db.String(1000), nullable=False)
    
    def __repr__(self):
        return f'{self.title} created on {self.date} with description {self.desc}'