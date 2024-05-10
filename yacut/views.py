from flask import Blueprint, flash, redirect, render_template, request

from yacut import db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    original_link = form.original_link.data
    custom_id = form.custom_id.data
    base_url = request.host_url

    if custom_id and URLMap.query.filter_by(short=custom_id).first():
        flash(
            'Предложенный вариант короткой ссылки уже существует.',
            'warning',
        )
        return render_template('index.html', form=form)

    short = custom_id if custom_id else get_unique_short_id()
    url_map = URLMap(original=original_link, short=short)
    db.session.add(url_map)
    db.session.commit()

    full_url = f'{base_url}{short}'
    flash(
        f"""
        Короткая ссылка создана:
        <a href="{full_url}" target="_blank">{full_url}</a>
        """,
        'success',
    )
    return render_template('index.html', form=form)


@main.route('/<string:short>', methods=['GET'])
def redirect_to_url(short: str):
    """Редирект по сокращенной ссылке к оригинальной."""
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
