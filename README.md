# Trucleenx Services


### Introduction

This is a cleaning company website. it provides all logos, fliers, images design etc needed to run a business. The client has not paid for the website but it's in great shape. We are planning to intergrate emails with this platform so that it can be a fully functional business

### How to create environment

Install all packages on ubuntu. Requirements for ubuntu are in ubuntu_req.txt while requirements for the website are in requirements.txt

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx
sudo apt-get install python3 etc
```


to create an environment run
```python
python3 -m venv environment_name
```



### How to install


```python

""" python3 -m venv environment_name """
source  environment_name/bin/activate
pip3 install -r requirements.txt
```


It is possible for Pillow to give you an error in ubuntu saying cairo is not installed same applies on windows as well. In windows install a library given on github.com while on ubuntu install the other libraries as well.

For scalablity avoid using an install as a database, proxy server and for storing media files as this won't work when trying to scale

__It is always a good idea to separate required packages based on specific modes e.g production modes and testing/development modes__

```python

django_proj/django_project/settings/dev.py
django_proj/django_project/settings/prod.py
```

### How to unistall a specific package

```python
 pip3 unistall -r package_name
```
### How to configure nginx

To run nginx on ubuntu you need to install it first
#### Installing nginx

```bash

sudo apt-get install nginx
```
#### Setup nginx

to setup i

### How to configure gunicorn