from flask import Blueprint, request, jsonify, redirect

from .views import get_unique_short_id
from .models import URLMap
from . import db

api = Blueprint("api", __name__)


@api.route("/id/", methods=["POST"])
def create_short_link():
    data = request.get_json()
    original = data.get("original")
    custom_id = data.get("custom_id", None)

    if custom_id and URLMap.query.filter_by(short=custom_id).first():
        return (
            jsonify(error="Предложенный вариант короткой ссылки уже существует."),
            400,
        )

    short = custom_id if custom_id else get_unique_short_id()
    url_map = URLMap(original=original, short=short)
    db.session.add(url_map)
    db.session.commit()

    return jsonify(original=original, short=short), 201


@api.route("/id/<short_id>/", methods=["GET"])
def get_original_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
