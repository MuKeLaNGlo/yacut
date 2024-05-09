from http import HTTPStatus
from typing import Tuple

from flask import render_template
from werkzeug.exceptions import HTTPException

from yacut import app, db


@app.errorhandler(404)
def page_not_found(error: HTTPException) -> Tuple[str, int]:
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(500)
def internal_error(error: HTTPException) -> Tuple[str, int]:
    db.session.rollback()
    return render_template('errors.html'), HTTPStatus.INTERNAL_SERVER_ERROR
