#!/bin/bash

# Create venv
python3 -m venv venv
source venv/bin/activate

# Install app
pip3 install --no-cache-dir  -e .

# Variables
export FLASK_ENV=development
export GUNICORN_RELOAD=True
export FLASK_APP=app
export API_TOKEN=token
export DATABASE_URI=mysql+pymysql://root:root@localhost:3306/myfingerprint

docker rm -f mariadb
docker rm -f adminer

docker run -d \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=myfingerprint \
    --name mariadb \
    mariadb:10.5.5

docker run -d \
    --link mariadb:db \
    -p 8080:8080 \
    --name adminer \
    adminer

flask run

# Remove virtualenv
deactivate
rm -rf venv
