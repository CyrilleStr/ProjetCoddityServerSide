# ProjetCoddityServerSide
## About
- Android app Api developed with Django Rest Framework
- UTBM school Project
## Api usage
```http
/* Create new user */
POST https://projetcoddityserverside.herokuapp.com/auth/register/ HTTP/1.1
content-type: application/json

{
    "username":"sosacy",
    "password":"calottedetesmorts"
}
/* Expected response */
HTTP/1.1 200 OK

/* Get authentification token */
POST https://projetcoddityserverside.herokuapp.com/auth/token/ HTTP/1.1
content-type: application/json

{
    "username":"cyrille1",
    "password":"calottedetesmorts"
}
/* Expected response */
HTTP/1.1 200 OK
{
  "token": "8850f382acf9d6ea761024e9cf8e9b51a3d5e884"
}

/* List user using authentification token */
GET https://projetcoddityserverside.herokuapp.com/auth/list HTTP/1.1
Authorization: Token 8850f382acf9d6ea761024e9cf8e9b51a3d5e884
/* Expected response */
[
  {
    "username": "cyrille1"
  },
  {
    "username": "zebi"
  }
]
```
## Installation
```bash
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # Linux
env\Scripts\activate # Win

# Install dependencies
pip install -r requirements.txt

# Generate staticfiles and databases
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Launch debug application
python manage.py runserver
```