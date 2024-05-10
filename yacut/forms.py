from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Поле не может быть пустым'),
            URL(message='Некорректный URL'),
            Length(max=512, message='Максимальная длина URL - 512 символов'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(min=1, max=16, message='Максимальная длина - 16 символов'),
            Regexp(
                '^[a-zA-Z0-9-]*$',
                message='Допустимы только буквы, цифры и дефисы'
            )
        ],
    )
    submit = SubmitField('Создать')
