# Epic Event


CRM, Organisation d'événements. 


## Prérequis
 - [Python > 3.7.2](https://www.python.org/downloads/)
 - [python-venv](https://docs.python.org/fr/3/library/venv.html)
 - [PostgreSQL](https://www.postgresql.org/)

## POSTGRESQL
- Apres avoir installer le [SGBD](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_de_base_de_donn%C3%A9es#cite_ref-fundamentals_2-9) PostgreSQL
sur votre machine
- Créez une base de données epic_event ou au nom de votre choix
- Notez bien que le nom doit correspondre au nom de la base déclarée dans le fichier .env (voir étape suivante)
- Les tables seront crées à l'étape de migration
  
## Installation
- Clonez/téléchargez ce projet
- Placez vous dans le répertoire `./project/django_epic_event/`
- Reportez-vous à la documentation [python-venv](https://docs.python.org/fr/3/library/venv.html)
  pour exécuter un environement virtuel.
- Lancez la commande `[PYTHON] -m pip install -r requirements.txt`
- Placez vous dans le répertoire epicEvent
- Rennomez le fichier `.env-template` en `.env` et apportez vos informations de base de données, votre clé de token JWT et votre endpoint de projet sentry
- Migrez la base de données avec la commande `[python] manage.py migrate`
- Vous pouvez également générer des données pour la base grâce à quelques outils dans `./fake_data`
- Démarrer le server web avec la commande `[python] manage.py runserver`
- La sortie de commande indique l'url de l'application (default: [http://127.0.0.1:8000/](http://127.0.0.1:8000/))
- Le backoffice d'admistration sera accessible à (admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/))

## FAKE DATA
- `generate.py` Génére entre 1 et 5 utilisateurs avec le rôle manager
- Pour chaques managers, entre 1 et 5 utilisateurs avec le rôle vendeur
- Pour chaques vendeurs, entre 1 et 5 clients.
- Pour chaques clients, entre 1 et 5 contrats.
- Pour chaques contrat, 1 evenement + 1 membre de support.
- La sortie est la creéation d'un fichier .sql par model
- `feed_database.sh` montre par exemple comment nourir la base de donées avec la commande en ligne postgres (`psql`) 

## POSTMAN
- Rendez-vous sur ma [collection postman](https://web.postman.co/workspace/epic_event_DAP_P12~f0477d25-96a0-4129-93e6-ed72ff569317/overview)
- Charger l'environement epic_env
- Parcourez les différentes routes pour essayer l'API

## PEP8
- [Documentation flake8 configuration](https://flake8.pycqa.org/en/latest/user/configuration.html)
- Reportez-vous à la documentation pour configurer flake8 pour les systèmes UNIX
-   ### TEXTE
    - Lancez la commande `[PYTHON] -m flake8 ./ > rapport_flake8.txt`
    - Vous obtiendrez un rapport flake8 dans le fichier rapport_flake8.txt
    - Ce fichier restera vide si aucune violation n'a été rencontrée
-   ### HTML
    - Lancez la commande `[PYTHON] -m flake8 --format=html --htmldir=flake-report`
    - Ouvrez le fichier `flake-report/index.html` dans un navigateur web.
    - Les erreurs seront explicitement indiquées
  
## Auteur
- [@SébastienLarcherLaffont](https://www.github.com/zionhigt)
- [@Leprojet sur github](https://github.com/zionhigt/Sebastian_Larcher-Laffont_DAP_P12)

  