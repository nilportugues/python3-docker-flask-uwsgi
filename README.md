# Flask Sample Application

# 1 - Local deployment

In order to make the package developed available to any other project running in the same machine, follow these steps:

```bash
cd example/flask_app_example
sudo pip install .
```

After the installation process, you may try it works by writing a new script outside the directory, for instance `/tmp`

```bash
#/tmp/test.py
from flask_app_example import app

print app.home()
```

Then run it and an output message should be printed on your screen: 

```bash
python /tmp/test.py 
> This is a sample library that has been imported from local python repository
```

See https://python-packaging.readthedocs.io/en/latest/minimal.html for more deployment options and publication over PyPI.

# 2 - Production Deployment with Docker

## 2.1 - Setup
In order to make it run, we will need to configure nginx and uwsgi and generate the package for the flask application. 

```
nginx (port 80 or 443) 
    --> uwsgi (port 8080) 
        --> your flask application
```

## 2.1 - Create the build

In order to create a build that we can use anywhere, we need to generate a tarball using `easy_install`'s proxy file `setup.py`. 

```sh
# Git clone the project
git clone <git repo>.git example
 
# Generate release tarball
cd example/
python setup.py sdist

# save somewhere the build at: 
./example/dist/flask_app_example-0.1.tar.gz
```

This generated tarball will be installed inside the docker container using:
 
```
pip install /path/to/flask_app_example-0.1.tar.gz
```

## 2.3 - uwsgi Configuration

The uwsgi configuration is fairly simple `docker/uwsgi/uwsgi.ini` too. 

**It is important to keep `0.0.0.0:8080` untouched. Don't use 127.0.0.1 or localhost.**

```
[uwsgi]
socket = 0.0.0.0:8080
wsgi-file = /var/www/example/flask_app_example/app.py
callable = app
processes = 4
threads = 2
stats = 127.0.0.1:9191
```

Internally, inside docker, it will run as follows: `uwsgi --ini /path/to/uwsgi.ini &`
## 2.4 - Nginx Configuration

The nginx configuration is fairly simple `docker/nginx/conf/app.conf`:

```
server {
  location / {
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:8080;
  }
}
```
