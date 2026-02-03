from app import db 
from datetime import datetime 

class Session(db.Model):
    __tablename__="sessions"

    id=db.Column(db.Integer,primary_key=True)

    inquiry_id=db.Column(
        db.Integer,
        db.ForeignKey("inquiries.id"),
        nullable=False
    )
    session_date=db.Column(db.Date,nullable=False)
    session_time=db.Column(db.String(20),nullable=False)
    status=db.Column(
        db.String(20),
        default="scheduled"
    )
    # Added fields for finance tracking
    deposit_amount = db.Column(db.Integer, default=0.0)
    total_price = db.Column(db.Integer, default=0.0)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    inquiry = db.relationship("Inquiry", backref="sessions")