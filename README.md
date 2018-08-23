# dope job app [![CircleCI](https://circleci.com/gh/delitamakanda/activcar/tree/master.svg?style=svg)](https://circleci.com/gh/delitamakanda/activcar/tree/master)
app for job finding in django framework

![Alt text](https://cdn.dribbble.com/users/272011/screenshots/2289607/dribbble_13oct.png)

## requirements
* python3
* django 2.0

set virtual environement with virtualenv with python3 support:

```bash
virtualenv venv -p python3
```

for mac users
```bash
source venv/bin/activate
```

for windows users
```bash
.\venv\Scripts\activate
```

install packages for django
```bash
pip install -r requirements-dev.txt
```

create a config file .env in your root folder, same level than manage.py with the content below
```text
SECRET_KEY=dummy_secret_key
DEBUG=True
OTHER_VARIABLE=variable_1
```



## Resources useful
- [AWS EB](https://stackoverflow.com/questions/41161691/how-to-run-a-celery-worker-with-django-app-scalable-by-aws-elastic-beanstalk)
- [Django Girls](https://tutorial.djangogirls.org/fr/)
- [Django Girls: extensions](https://tutorial-extensions.djangogirls.org/en/)
