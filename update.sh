#!/bin/bash
heroku maintenance:on
git push heroku master
heroku run python manage.py deploy
maintenance:off
