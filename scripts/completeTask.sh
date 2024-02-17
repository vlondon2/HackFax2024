#!/bin/bash

id=$1
taskName=$2

echo "ID: $id"
echo "Task Name: $taskName"

curl -X PATCH -d "{\"id\": $id, \"taskName\": \"$taskName\"}" http://localhost:8000/user/completeTask | json
