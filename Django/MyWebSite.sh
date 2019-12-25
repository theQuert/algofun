# Lesson 1
pip install virtualenv
virtualenv MyWebSite		# Create virtual environment MyWebSite
source MyWebSite/bin/activate # Running in background
pip install django
django-admin startproject mysite # Create django project mysite
cd mysite
	# manage.py startapp creating app. Therefore, mymainsite is an app.
python manage.py startapp mymainsite	# Create app mymainsite 
	# Under mysite including:	1. __init__.py: module 2. settings.py: Templates, Databases, URLs settings 
	# 3. urls.py: URLs responses, and communicate with view. 4. wsgi.py

	# mymainsite is an app
	# mymainsite including: 1. models.py connect with migrations, creating tables, index settings, and other Databases settings.
	# 2. admin.py: Human-Machine Interface 3. views.py: Viewing through Https responses.

	# Migrate, to create tables Including 'admin', 'auth', 'contenttypes', and 'sessions'.
python manage.py migrate
	# runserver. Running on Web viewing.
python manage.py runserver

	# manage.py is used to manage django website settings
	# Directory 'mysite' would be created under mysite project
	# Inportant files: settings.py, urls.py and wsgi.py would be stored under dir:mysite
	# urls.py is used to point to each URL site.
	# settings.py is used to settings the whole site.
#---------------------------------------------------------------------------------------------------------------------------------

