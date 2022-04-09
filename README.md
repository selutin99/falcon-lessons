# falcon-tutorials

## Table of contents
- [Overview](#Overview)
- [Git info](#Git-info)
- [Local Development](#Local-Development)
- [Other useful info](#Other-useful-info)
	- [YouTube lessons](#YouTube-lessons)

## Overview
Repo with tutorials for falcon micro framework. 

## Documentation
* Documentation by falcon: [link](https://falconframework.org/)

## Git info
* For each issue, a separate branch is created with the name "feature/[name_of_feature]" (without []);
* After the work is completed, a pull request is created to the master branch;
* Make sure that all CI & CD validations are passed successful.

## Local Development
* Check you have Python 3.7.2 installed by typing on commandline `python --version`
* Install environment
```
pip install virtualenv
virtualenv venv
CALL venv/Scripts/activate (on Windows)
source venv/bin/activate (on Linux)
pip install -r requirements.txt
```
* Run server `gunicorn app.py_script_file_name_without_extension:api`
* Point your web browser to `http://localhost:8000/`

## Other useful info

### YouTube lessons
Lessons based on: [link](https://www.youtube.com/watch?v=vHbdyL9aZ-M&list=PLLhEJK7fQIxBzJtrjyVDu6RGhSCTmo5rH&index=1)

