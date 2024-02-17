#!/bin/bash

username=$1
password=$2

echo "Username: $username"
echo "Password: $password"

curl -X GET "http://localhost:8000/user/get?username=$username&password=$password" | json
