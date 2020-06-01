
## Generate a fresh new virtual env and activate it
python3 -m venv .env
source .env/bin/activate

Install the dependencies

pip install -r requirements.txt


## Move Django Application (https://stackoverflow.com/questions/47230523/django-not-working-after-moving-directory-do-i-have-a-path-python-installation)

Before to move the project and with the virtual environment activated

pip freeze > requirements.txt

Then deactivate the environment and remove it

deactivate
rm -rf .env

Move the project to the desired directory

Generate a fresh new virtual env and activate it

python3 -m venv .env
source .env/bin/activate

Install the dependencies

pip install -r requirements.txt