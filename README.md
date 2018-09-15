Pitch
===================

- - - -
Author: [Brian Mutai](https://github.com/brayonski)
## Description
[Pitch](https://github.com/Brayonski/pitching) This is website that helps users to post pitches according to their likes e.g in technology,science,entertainment or sports. 

------------------------------------------------------------------------

## User 

1. User will see pitches from other users and comment on them
2. Users are able to add pitches
3. Categories of pitches are stated
4. Users can view pitches according to categories independently e.g from technology,science,entertainment and sports.

## Features

+ [x] List various pitches.
+ [x] List pitches from the selecte categories
+ [x] Redirect user to the actual article
+ [x] Categorize pitches
+ [ ] comment on pitch posted
+ [ ] show comment of pitch according to pitch id


## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6.4

### Cloning the repository
```bash
git clone https://github.com/Brayonski/pitching && cd pitching
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required
* Flask==0.12.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6
* gunicorn==19.7.1


### Running Tests
```bash
python3 manage.py test
```

### Running the web app in development
```bash
python3 manage.py server
```
Open the app on your browser, by default on `127.0.0.1:5000`.

## Live Demo

The web app can be accessed from the following link


## Quickstart

```
usage: manage.py [-?] {server,test,shell,runserver} ...

positional arguments:
  {server,test,shell,runserver}
    server              Runs the Flask development server i.e. app.run()
    test                Run the unit tests.
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit
```

## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/Brayonski/pitching]
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Brian Mutai](https://github.com/Brayonski)