dev-start:
	python3 manage.py runserver --settings=config.settings.dev
dev-startapp:
	cd apps && python3 ../manage.py startapp $(app) --settings=config.settings.dev
dev-migrate:
	python3 manage.py migrate --settings=config.settings.dev
dev-makemigrations:
<<<<<<< HEAD
	python3 manage.py makemigrations --settings=config.settings.dev
=======
	python3 manage.py makemigrations  --settings=config.settings.dev
>>>>>>> a58535d880ded1170f6b82f98e17a08de7d7dff8
dev-shell:
	python3 manage.py shell --settings=config.settings.dev
dev-shell-plus:
	python3 manage.py shell_plus --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt
dev-test:
	python3 manage.py test --settings=config.settings.dev
dev-showm:
	python3 manage.py showmigrations  --settings=config.settings.dev

	
	
