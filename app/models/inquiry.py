from app import db
from datetime import datetime

class Inquiry(db.Model):
    __tablename__ = "inquiries"

    id = db.Column(db.Integer, primary_key=True)
    # Link to the User model
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    tattoo_idea = db.Column(db.Text)
    estimated_price = db.Column(db.Float)
    status = db.Column(db.String(20), default="new")
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)