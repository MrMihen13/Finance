# Система контроля и анализа финансов

[Техническое задание на разработку](./docs/technical_requirements.md)

[Репозиторий с Telegram ботом](https://github.com/MrMihen13/Finance-tgbot)

## Local run server

1. Create `.env` file and copy there environment variable from `.emv.template`
2. Run command `>> pipenv shell` for creating virtual environment
3. Run command `>> pipenv install` for install project requirements
4. Run command `>> python manage.py migrate` for complete project migrations
5. Run command `>> python manage.py collectstatic` for collect project`s static files
6. Run command `>> python manage.py runserver` for run local server

If you did everything correctly, you will see this text in your console.

```
System check identified no issues (0 silenced).
April 17, 2022 - 18:46:34
Django version 4.0.4, using settings 'finance.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```