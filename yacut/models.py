from datetime import datetime

from yacut import db


class URLMap(db.Model):
    """Модель для хранения сокращенных ссылок."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(512), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
