# YaCut

[![Flask][Flask-badge]][Flask-url]
[![SQLAlchemy][SQLAlchemy-badge]][SQLAlchemy-url]

---

[Flask-badge]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com

[SQLAlchemy-badge]: https://img.shields.io/badge/sqlalchemy-fbfbfb?style=for-the-badge
[SQLAlchemy-url]: https://www.sqlalchemy.org/

### Описание
Сервис для создания и использования коротких ссыылок. Есть API интерфейс.

---

Шаблон файла ".env":
```python
SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'
SECRET_KEY=<секретный ключ>
FLASK_APP=yacut
FLASK_DEBUG=0
```

### Инструкция по запуску
Перед запуском необходимо склонировать проект:
```bash
git clone https://github.com/MuKeLaNGlo/yacut.git
cd yacut
```

Выполнить миграции:
```bash
flask db upgrade
```

Теперь проект можно проверить по адресу [http://localhost:5000/](http://localhost:5000/)

Сайт доступен по ссылке: http://127.0.0.1:5000/
