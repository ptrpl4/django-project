# creation

## create venv

`python3 -m venv env_name`

## install django in venv

`pip install django`

## create django project

`django-admin startproject project_name`

# using

## activate env 

`source env/bin/activate`

or setup IDE terminal & env

## start django

`python manage.py runserver`

## django create new app

`python manage.py startapp app_name`

# git init
```commandline
git init
git add .
git commit -m "commit name"
```
## commit
```commandline
add all staged files in commit
git commit -a -m "testing git changes"
```
## rm
```commandline
git rm filename
```
## rename
```commandline
$ git mv README.md README
# equal
$ mv README.md README
$ git rm README.md
$ git add README
```
## log
```commandline
# all commits order by desc
git log
# show patch -p or --patch
git log -p -2
# short changed info --stat
git log --stat
# change view for data --pretty
git log --pretty
# additional options for --pretty
git log --pretty=oneline
# another addotional opt. - =short, =full, =fuller
# time options
git log --since=2.weeks
# serach for string -S
git log -S function_name
# commits related to specific file -- path/to/file
git log -- path/to/file
# exclude merges --no-merges
git log --no-merges
```
## rename
```commandline
git rm filename
```
