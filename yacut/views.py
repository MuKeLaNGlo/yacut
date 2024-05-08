from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import URLForm
from .models import URLMap
from . import db
import random
import string

main = Blueprint("main", __name__)


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    short_id = "".join(random.choice(characters) for _ in range(6))
    return (
        short_id
        if not URLMap.query.filter_by(short=short_id).first()
        else get_unique_short_id()
    )


@main.route("/", methods=["GET", "POST"])
def index():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data

        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first():
                flash("Предложенный вариант короткой ссылки уже существует.")
                return redirect(url_for("index.html"), form=form)
            short = custom_id
        else:
            short = get_unique_short_id()

        url_map = URLMap(original=original_link, short=short)
        db.session.add(url_map)
        db.session.commit()

        flash(f"Короткая ссылка создана: {short}")
        return redirect(url_for("index.html"), form=form)

    return render_template("index.html", form=form)


@main.route('/<string:short>', methods=['GET'])
def redirect_to_url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
