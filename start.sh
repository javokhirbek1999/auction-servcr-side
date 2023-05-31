#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py makemigrations
python manage.py migrate
python manage.py crontab add
python manage.py runserver ${HOST}:${PORT}