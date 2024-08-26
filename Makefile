mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

app:
	python3 manage.py startapp apps


user:
	python3 manage.py createsuperuser

run:
	python3 manage.py runserver
