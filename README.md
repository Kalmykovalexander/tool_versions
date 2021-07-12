Requirements:

  Python 3.9.0
  Django 3.2.5
  Django REST Framework 3.12.4


Installation:

1) Install Python Requirements
   
   $pip install -r requirements.txt
   
2) Run commands:

   - Create initial database sqlite:
     $python manage.py makemigrations
     $python manage.py migrate
    
    - Create user:
    $ python manage.py createsuperuser
   
3) Run the Server

   $python manage.py runserver
   
   
Links API:

Admin panel:
  http://127.0.0.1:8000/admin

List all objects
  http://127.0.0.1:8000/api/tools/all/

Create object
  http://127.0.0.1:8000/api/tools/tool/create/

Retrieve, update, delete object (pk = id object)
  http://127.0.0.1:8000/api/tools/tool/detail/pk/

