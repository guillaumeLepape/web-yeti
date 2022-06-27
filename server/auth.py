from datetime import datetime
from datetime import timedelta

import jwt
from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import request

from . import db
from .auth_utils import token_required
from .constants import GLOBAL_ENDPOINT
from .constants import VERSION
from .models import Match
from .models import Matches
from .models import User
from .telegram_sender import send_message
from .utils import success_response

auth = Blueprint("auth", __name__)


@auth.route(f"/{GLOBAL_ENDPOINT}/{VERSION}/login", methods=["POST"])
def login_post():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({"message": "Invalid credentials", "authenticated": False}), 401

    send_message(f"User {user.name} login.")

    token = jwt.encode(
        {
            "sub": user.id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=30),
        },
        current_app.config["SECRET_KEY"],
    )
    return jsonify({"token": token})


@auth.route(f"/{GLOBAL_ENDPOINT}/{VERSION}/signup", methods=["POST"])
def signup_post():
    data = request.get_json()

    # Check existing user in db
    existing_user = User.query.filter_by(name=data["name"]).first()
    if existing_user:
        return jsonify({"message": "Name already exists", "signup": False}), 401

    # Initialize user and integrate in db
    user = User(**data)
    db.session.add(user)
    db.session.commit()

    # Initialize matches and integrate in db
    for match in Matches.query.all():
        db.session.add(
            Match(user_id=user.id, match_id=match.id, score1=None, score2=None)
        )
    db.session.commit()

    return jsonify(user.to_user_dict()), 201


@auth.route(f"/{GLOBAL_ENDPOINT}/{VERSION}/current_user")
@token_required
def current_user(current_user):
    return success_response(200, current_user.to_user_dict())
