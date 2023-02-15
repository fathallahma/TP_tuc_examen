## Groupe :
Fathallah Mohamed Amine 
Amrouni Liza
Bouchikhi Youssef


## Préparer son environnement

Installer le paquet virtualenv

> pip install virtualenv

Créer l'environnement virtuel

> python -m virtualenv venv

Activer l'environnement virtuel

> Linux/Mac : source venv/bin/activate
> Windows : ./venv/Scripts/activate.ps1

Si sur windows vous ne pouvez exécuter le script en .ps1, ouvrer un powershelle en admin et exécuter
> set-executionpolicy unrestricted

Installer les paquets

> pip install -r requirements.txt

## Démarrer l'application

> uvicorn main:app
> --reload # pour développer (recharge automatique l'application à chaque changement d'un fichier)

Exécuter dans le dossier application

## Pytest

> python -m pytest

## Coverage

> coverage run -m pytest --profile # remplace la commande python
> coverage html # génère le rapport en html

Exécuter à la racine du dossier

## Locust

> locust # nécessite d'avoir un fichier locustfile.py dans le dossier où la commande est exécuté
> locust --config=.locust.conf

## Pylint

> pylint application/ tests/
