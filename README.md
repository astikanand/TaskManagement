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
* Pagination to navigate between the pages 


Validations
------------------------------
* User need to login to `Create New Task` and will be directed to login page on clicking `My tasks` if not logged in.
* User need to login to  see `My tasks` and will be directed to login page on clicking `Create New Task` if not logged in.
* User can `Edit` or `Delete` only the tasks that is created by them.


Requirements
------------------------------

* ``Django>=1.10.1``
* ``django-widget-tweaks>=1.4.0``


Installation
------------------------------

1. Download or clone the repository.
    
    ```
    $ git clone https://github.com/astikanand/TaskManagement.git
    ```

2. Install dependencies by going into the project directory

    ```
    $ pip install -r requirements.txt
    ```
    
3. Change `Debug` mode on localhost

    ```
    Debug = True
    ```

4. Migrate the changes to database and run the server

    ```
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py collectstatic
    $ python manage.py runserver
    ```

5. Open your browser and hit [localhost:8000](http://localhost:8000/) 
    

Preview
------------------------------

**Home**

![TaskManagement Home Page](https://i.imgur.com/p0W0MUV.png)




**All Tasks**

![All Tasks](https://i.imgur.com/LKDCkgd.png)




**My Tasks**

![My Tasks](https://i.imgur.com/TNgMEix.png)





**Task detail**

![Task detail](https://i.imgur.com/vDTgUlZ.png)




**Create Task**

![Create Task](https://i.imgur.com/tmmRxq9.png)



**Edit Task**

![Edit Task](https://i.imgur.com/tsn793n.png)



**Delete Task**

![Delete](https://i.imgur.com/zE3ZYeG.png)




**Error Page**

![Error Page](https://i.imgur.com/Wou01d6.png)




**Admin Panel**

![Admin Panel](https://i.imgur.com/BNWeMCu.png)




