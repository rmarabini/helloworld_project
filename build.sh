#!/usr/bin/env bash
set -o errexit # Exit on error

# Install dependencies, 
# collect static files, 
# and apply database migrations
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
