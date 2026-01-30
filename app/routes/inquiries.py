from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from app import db
from app.models.inquiry import Inquiry
from app.models.reminder import Reminder
from datetime import datetime,timedelta

inquiries_bp = Blueprint("inquiries", __name__)

@inquiries_bp.route("/dashboard")
def dashboard():
    # This will render the HTML file we just created
    return render_template("inquiries.html")

@inquiries_bp.route("/inquiries", methods=["POST"])
@login_required
def create_inquiry():
    data = request.json
    inquiry = Inquiry(
        user_id=current_user.id, # Automatically link to logged-in artist
        client_name=data["client_name"],
        contact_info=data["contact_info"],
        tattoo_idea=data.get("tattoo_idea"),
        estimated_price=data.get("estimated_price"),
        notes=data.get("notes")
    )
    db.session.flush() # This gives us the inquiry.id before committing
    
    # Auto-schedule a follow-up reminder for 2 days from now
    follow_up = Reminder(
        inquiry_id=inquiry.id,
        reminder_date=datetime.utcnow().date() + timedelta(days=2),
        reason=f"Follow up with {inquiry.client_name}"
    )
    db.session.add(follow_up)
    db.session.commit()

@inquiries_bp.route("/inquiries", methods=["GET"])
@login_required
def get_inquiries():
    # Only return inquiries belonging to the current artist
    inquiries = Inquiry.query.filter_by(user_id=current_user.id).all()
    return jsonify([
        {
            "id": i.id,
            "client_name": i.client_name,
            "status": i.status,
            "estimated_price": i.estimated_price
        } for i in inquiries
    ])
