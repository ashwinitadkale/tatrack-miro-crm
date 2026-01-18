from flask import Blueprint, request, jsonify
from app import db
from app.models.inquiry import Inquiry

inquiries_bp = Blueprint("inquiries_bp", __name__)

@inquiries_bp.route("/inquiries", methods=["POST"])
def create_inquiry():
    data = request.json
    inquiry = Inquiry(
        client_name=data["client_name"],
        contact_info=data["contact_info"],
        tattoo_idea=data.get("tattoo_idea"),
        estimated_price=data.get("estimated_price"),
        notes=data.get("notes")
    )
    db.session.add(inquiry)
    db.session.commit()
    return jsonify({"message": "Inquiry created"}), 201


@inquiries_bp.route("/inquiries", methods=["GET"])
def get_inquiries():
    inquiries = Inquiry.query.all()
    return jsonify([
        {
            "id": i.id,
            "client_name": i.client_name,
            "status": i.status,
            "estimated_price": i.estimated_price
        } for i in inquiries
    ])


@inquiries_bp.route("/inquiries/<int:id>", methods=["PUT"])
def update_inquiry(id):
    inquiry = Inquiry.query.get_or_404(id)
    data = request.json

    inquiry.status = data.get("status", inquiry.status)
    inquiry.notes = data.get("notes", inquiry.notes)

    db.session.commit()
    return jsonify({"message": "Inquiry updated"})


@inquiries_bp.route("/inquiries/<int:id>", methods=["DELETE"])
def delete_inquiry(id):
    inquiry = Inquiry.query.get_or_404(id)
    db.session.delete(inquiry)
    db.session.commit()
    return jsonify({"message": "Inquiry deleted"})
