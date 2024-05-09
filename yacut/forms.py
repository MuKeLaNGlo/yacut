from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка', validators=[DataRequired(message='Поле не может быть пустым')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=16, message='Максимальная длина - 16 символов'),
        ],
    )
    submit = SubmitField('Создать')
