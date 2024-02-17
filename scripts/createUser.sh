#!/bin/bash

username=$1
password=$2

echo "Username: $username"
echo "Password: $password"

curl -X POST -d '{"username": "'"$username"'", "password": "'"$password"'"}' http://localhost:8000/user/create | json
