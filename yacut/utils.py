import random
import string
from re import match

from yacut.models import URLMap


def generate_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def get_unique_short_id():
    """Генерирует уникальную сокращенную ссылку."""
    while True:
        short_id = generate_random_string()
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id


def validate_custom_id(custom_id):
    """Проверяет, соответствует ли custom_id условиям:
    только буквы и цифры, длина до 16 символов."""
    return bool(match(r'^[A-Za-z0-9]{1,16}$', custom_id))


def extract_id_from_url(url):
    """Извлекает ID из URL или возвращает строку как есть, если это не URL."""
    if 'http://' in url or 'https://' in url:
        return url.rsplit('/', 1)[-1]
    return url
