# ProjetCoddityServerSide
## About
- Android app Api developed with Django Rest Framework
- UTBM school Project
## Api usage
```js
/* Create new user */
POST "https://projetcoddityserverside.herokuapp.com/auth/register/" HTTP/1.1
content-type: application/json

{
    "username":"sosacy",
    "password":"calottedetesmorts"
}
/* Expected response */
HTTP/1.1 200 OK

/* Get authentification token */
POST "https://projetcoddityserverside.herokuapp.com/auth/token/" HTTP/1.1
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
GET "https://projetcoddityserverside.herokuapp.com/auth/list" HTTP/1.1
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

/* Add bin using authentification token */
POST "https://projetcoddityserverside.herokuapp.com/grabthetrash/add-item/" HTTP/1.1
Authorization: Token 8850f382acf9d6ea761024e9cf8e9b51a3d5e884

isBin:True
owner:2
latitude:564
longitude:45656
image:image.jpg
/* Expected response */
{
    "pk": 1,
    "isBin":true,
    "owner": 2,
    "isAccepted": false,
    "latitude": 564,
    "longitude": 45656,
    "image": "/media/default/Capture_d%C3%A9cran_110.png",
    "validator1": null,
    "validatorVerdict1": false,
    "validator2": null,
    "validatorVerdict2": false,
    "validator3": null,
    "validatorVerdict3": false
}

/* List bin using authentification token */
GET "https://projetcoddityserverside.herokuapp.com/grabthetrash/list-item" HTTP/1.1
Authorization: Token 8850f382acf9d6ea761024e9cf8e9b51a3d5e884
/* Expected response */
[
    {
        "pk": 1,
        "owner": 2,
        "isAccepted": false,
        "latitude": 564,
        "longitude": 45656,
        "image": "https://projetcoddityserverside.herokuapp.com/media/default/Capture_d%C3%A9cran_110.png",
        "validator1": null,
        "validatorVerdict1": false,
        "validator2": null,
        "validatorVerdict2": false,
        "validator3": null,
        "validatorVerdict3": false
    },
    {
        "pk": 1,
        "owner": 2,
        "isAccepted": false,
        "latitude": 564,
        "longitude": 45656,
        "image": "https://projetcoddityserverside.herokuapp.com/media/default/Capture_d%C3%A9cran_110.png",
        "validator1": null,
        "validatorVerdict1": false,
        "validator2": null,
        "validatorVerdict2": false,
        "validator3": null,
        "validatorVerdict3": false
    }
]

/* Get item (3 maximum, bin or garbage) to validate using authentification token */
GET "https://projetcoddityserverside.herokuapp.com/grabthetrash/items-to-validate" HTTP/1.1
Authorization: Token 8850f382acf9d6ea761024e9cf8e9b51a3d5e884
/* Expected response */
// Same as before

/* Post user answers about item to validate using authentification token */
POST "https://projetcoddityserverside.herokuapp.com/grabthetrash/items-validation" HTTP/1.1
Authorization: Token 8850f382acf9d6ea761024e9cf8e9b51a3d5e884
pk1:1
answer1:True
pk2:2
answer2:False
pk3:0 // When no answers
answer3:False
/* Expected response */
status code = 200
```

## Dev env installation
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
## Heroku Deploy 
- Create heroku app and follow instructions
- ```
  # Deploy modifications
  git commit 
  git push heroku main
  ```

