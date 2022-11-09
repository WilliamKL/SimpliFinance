#!/usr/bin/env bash
poetry install
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
