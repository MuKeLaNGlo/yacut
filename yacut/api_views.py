from flask import Blueprint, jsonify, request

from yacut import db
from yacut.models import URLMap
from yacut.utils import extract_id_from_url, validate_custom_id
from yacut.views import get_unique_short_id

api = Blueprint('api', __name__)


@api.route('/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()

    if not data:
        return jsonify(message='Отсутствует тело запроса'), 400

    if 'url' not in data:
        return jsonify(message='"url" является обязательным полем!'), 400

    original = data.get('url')
    custom_id = data.get('custom_id')

    if custom_id:
        custom_id = extract_id_from_url(custom_id)
        if not validate_custom_id(custom_id):
            return jsonify(
                message='Указано недопустимое имя для короткой ссылки'
            ), 400
        if URLMap.query.filter_by(short=custom_id).first():
            return (
                jsonify(
                    message='Предложенный вариант'
                            'короткой ссылки уже существует.'
                ),
                400,
            )

    base_url = request.host_url
    short = custom_id if custom_id else get_unique_short_id()
    short_url = base_url + short
    url_map = URLMap(original=original, short=short)
    db.session.add(url_map)
    db.session.commit()

    return jsonify(url=original, short_link=short_url), 201


@api.route('/id/<short_id>/', methods=['GET'])
def get_original_link(short_id: str):
    if not short_id:
        return jsonify(
            message='Не передан короткий идентификатор ссылки.'
        ), 201

    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        return jsonify(message='Указанный id не найден'), 404
    return jsonify(url=url_map.original), 200
