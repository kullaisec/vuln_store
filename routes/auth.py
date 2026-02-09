from flask import Blueprint, request
from controllers.user_controller import login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user(request)
