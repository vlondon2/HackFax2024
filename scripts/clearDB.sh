#!/bin/bash

rm ../backend/treeapp/db.sqlite3

python3 ../backend/treeapp/manage.py makemigrations

python3 ../backend/treeapp/manage.py migrate
