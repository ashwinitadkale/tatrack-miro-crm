from flask import Blueprint, request, jsonify
from app import db
from app.models.reminder import Reminder
from datetime import datetime

reminders_bp = Blueprint("reminders", __name__)

@reminders_bp.route("/reminders", methods=["POST"])
def create_reminder():
    data = request.json

    reminder_date = datetime.strptime(
        data["reminder_date"], "%Y-%m-%d"
    ).date()

    reminder = Reminder(
        inquiry_id=data["inquiry_id"],
        reminder_date=reminder_date,
        reason=data.get("reason")
    )
    db.session.add(reminder)
    db.session.commit()
    return jsonify({"message": "Reminder created"}), 201


@reminders_bp.route("/reminders/today", methods=["GET"])
def reminders_today():
    today = datetime.today()
    reminders = Reminder.query.filter_by(
        reminder_date=today,
        is_completed=False
    ).all()

    return jsonify([
        {
            "id": r.id,
            "inquiry_id": r.inquiry_id,
            "reason": r.reason
        } for r in reminders
    ])


@reminders_bp.route("/reminders/<int:id>/complete", methods=["PUT"])
def complete_reminder(id):
    reminder = Reminder.query.get_or_404(id)
    reminder.is_completed = True
    db.session.commit()
    return jsonify({"message": "Reminder completed"})
# quick route test 
@reminders_bp.route("/test", methods=["GET"])
def test_route():
    return {"message": "reminders blueprint working"}
