TaskManagement
------------------------------
A task management system for user. 

Live
------------------------------
**TaskManagement** is live on [https://taskmanagement-astikanand.herokuapp.com](https://taskmanagement-astikanand.herokuapp.com)


Features
------------------------------
* User can create the task by clicking on `Create New Task`.
* User can view all the tasks on the portal by clicking on `All Tasks`.
* User can also see tasks created by them by clicking on `My Tasks`.
* User can view the task detail by clicking on `View Detail` on task panel.
* User can edit the tasks created by them by clicking on `Edit This Task` on task detail page.
* User can delete the tasks created by them by clicking on `Delete This Task` on task detail page.
* Proper errors like 400, 403, 404 and 500 error are shown if any violations.
* User can create new account or login to existing account.


Validations
------------------------------
* User need to login to `Create New Task` and will be directed to login page on clicking `My tasks` if not logged in.
* User need to login to  see `My tasks` and will be directed to login page on clicking `Create New Task` if not logged in.
* User can `Edit` or `Delete` only the tasks that is created by them.



Preview
------------------------------

![TaskManagement Home page](https://imgur.com/a/MxdEJ)

.. image:: https://raw.githubusercontent.com/agusmakmun/django-markdown-editor/master/__screenshot/martor-preview-result.png


Requirements
------------------------------

* ``Django>=1.10.1``
* ``django-widget-twaeaks>=1.4.0``


Installation
------------------------------

1. Download or clone the repository.

    $ git clone https://github.com/astikanand/TaskManagement.git

2. Install dependencies by going into the project directory

    $ pip install -r requirements.txt
    
3. Change `Debug` mode on localhost

    Debug = True

4. Migrate the changes to database and run the server

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py collectstatic
    $ python manage.py runserver

5. Open your browser and hit [localhost:8000](http://localhost:8000/) 
    

