from flask import Blueprint, request
from services.report_service import generate_report

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/report")
def report():
    return generate_report(request.args.get("file"))
