# agilesw
Agile software for Agile practices

Software No. 1
Djangobased Todolist software available in the djangobase
There are many other features

How to utilize:
1. Clone the repository in your computer
2. Create a new djangobase project, create app_users, app_todolist
3. Copy the source to the target directory
4. Setup your database or leave as-is with dbsqlite3
5. pip install -r requirements.txt

This is basic django installation if you are new (on windows, similary you can translate to other OS)
On windows computer
1. after python is installed
2. pip install pipenv
3. mkdir django_dir
4. cd django_dir
5. pipenv shell
6. clone the repository under django_dir as reference
7. pip install django
8. django-admin startproject project_djangobase
9. python manage.py startapp app_users
10. python manage.py startapp app_todolist
11. copy the code from the reference djangobase to the corresponding project_djangobase, app_todolist, app_users
12. run the django server by: 
  python manage.py makemigrations 
  python manage.py migrate
  python manage.py runserver
