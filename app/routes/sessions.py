from flask import Blueprint, request, jsonify
from app import db
from app.models.session import Session
from app.models.inquiry import Inquiry

sessions_bp = Blueprint("sessions", __name__)

@sessions_bp.route("/sessions", methods=["POST"])
def create_session():
    data = request.json

    inquiry = Inquiry.query.get_or_404(data["inquiry_id"])
    inquiry.status = "booked"

    session = Session(
        inquiry_id=inquiry.id,
        session_date=data["session_date"],
        session_time=data.get("session_time")
    )

    db.session.add(session)
    db.session.commit()

    return jsonify({"message": "Session booked"}), 201


@sessions_bp.route("/sessions", methods=["GET"])
def get_sessions():
    sessions = Session.query.all()
    return jsonify([
        {
            "id": s.id,
            "client": s.inquiry.client_name,
            "date": str(s.session_date),
            "time": s.session_time,
            "status": s.status
        } for s in sessions
    ])


@sessions_bp.route("/sessions/<int:id>", methods=["PUT"])
def update_session(id):
    session = Session.query.get_or_404(id)
    data = request.json

    session.status = data.get("status", session.status)
    session.session_date = data.get("session_date", session.session_date)
    session.session_time = data.get("session_time", session.session_time)

    if session.status == "completed":
        session.inquiry.status = "completed"

    if session.status == "cancelled":
        session.inquiry.status = "lost"

    db.session.commit()
    return jsonify({"message": "Session updated"})
