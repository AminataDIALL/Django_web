## Documentation:
Commencer par télécharger le project

##Image Docker:
Placer vous sur la racine du project 'django_project'
### Lancer le contenneur docker:
* docker-compose up --build
### Assurez-vous de faire la migration vers la base de donnée:

* docker-compose run web python manage.py makemigrations
* docker-compose run web python manage.py migrate 

### Créer un  admin
* docker-compose run web python manage.py createsuperuser

### Relancer le contenneur docker:
* docker-compose up

Accéder à l'application via : http://127.0.0.1:8000/
Accéder à la page admin : http://127.0.0.1:8000/admin

Créer un utilisateur
Retrouner à la page d'accueil de l'application et connectez-vous avec vos identifiants
