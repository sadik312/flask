# Following YouTube Tutorial

## Installation
1. set Path (.zshrc in my case)
    - `export PATH="$PATH;/home/sadik/.local/bin"`
2. install pipenv
    - `pip3 install pipenv`
3. activate virtual environment
    - `pipenv shell` - if this doesn't work
    - `sudo -H pip install -U pipenv`
4. install dependencies for project
    - `pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy`


# Questions I had
1. Why don't I just install packages globally on my system?