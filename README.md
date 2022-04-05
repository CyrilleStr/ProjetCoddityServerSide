# ProjetCoddityServerSide
# Installation
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