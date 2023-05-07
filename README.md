# ChatApp  #

A small functional group message center application built using Django.
It has a REST API and uses WebSockets to notify clients of new messages.

## Technologies used ##
- Django
- Django Rest framework
- Django Channels

## Architecture ##
 - When a user logs in, user is reidrected to a page where user can either create a new group or join an existing one.
 - When a user selets a group to join, all messages in the group are queried from the database and loaded for the user.
 - When a user sends a message, the frontend sends the payload on active websocket connection.
   Django saves the message and notifies the users present in current group.
 - When the socket receives a new message, it loads the messages and appends it into the DOM so it becomes visible for the user.

### Database ###
MySQL database is used for this project.

## Run ##
1. Make sure `MySql` and `redis` is installed on the machine.

2. Install these system dependencies for python packages
```bash
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

3. Create and activate a virtualenv (Python 3)
```bash
$ virtualenv venv
$ source venv/bin/activate
```
4. Install requirements
```bash
pip install -r requirements.txt
```

5. Create a MySQL database and user to be used by the proejct

6. Make sure Redis server is running.

7. Create a copy of `.env.example` file and name it `.env`. Set correct value for each environment variable.

8. Run migration to setup database
```bash
pythnon manage.py migrate
```

9. Run tests
```bash
./manage.py test
```

10. Create admin user
```bash
./manage.py createsuperuser
```

11. Run development server
```bash
./manage.py runserver
```

12. Open `http://localhost:8000` in browser.
