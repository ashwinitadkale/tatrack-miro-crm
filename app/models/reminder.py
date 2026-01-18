from app import db
from datetime import datetime

class Reminder(db.Model):
    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)
    inquiry_id = db.Column(
        db.Integer,
        db.ForeignKey("inquiries.id"),
        nullable=False
    )
    reminder_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(200))
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    inquiry = db.relationship("Inquiry", backref="reminders")
