# E-commerce_Bendy
    Ce projet porte sur le développement d'un site Web virtuel "Site de commerce électronique" pour une marque du nom de <span>Bendi</span>. Ce site est plus particulièrement au profit des sénégalais. Il fournit à l'utilisateur une liste des différents produits disponibles à l'achat dans la boutique. Pour faciliter les achats en ligne, un panier d'achat est mis à la disposition de l'utilisateur. Après la sélection des produits, il est envoyé pour le processus de confirmation de la commande. Le système est mis en œuvre en utilisant le framework web Django de Python.

# Processus de lancement de l'application
    0- git clone https://github.com/maba-dev/E-commerce_Bendy.git
    1- cd ~/E-commerce_Bendy
    2- sudo apt install python3.8-venv
    3-  python3 -m venv env
    4- source env/bin/activate
    5- installation de django
    6- pip install django
    7-python manage.py runserver


# Page d'acceuil après l'exécution de la commande ``python manage.py runserver`` dans le terminale

   ![2022-07-11 (4)](https://user-images.githubusercontent.com/77069769/178287801-e2aecc81-8a10-4ef3-ae2c-e81b90be7717.png)

# création de projet dans Django
    django-admin startproject shop .
# création de l'application dans django
    python manage.py startapp store
# execution de l'application en local
    python manage.py runserver

# commandes de migration de ma base de données
    python manage.py makemigrations
    python manage.py migrate
# creation de user dans la page admin
    python3 manage.py createsuperuser


Author: Mamadou Cherif Ba(email: 2744@holbertonschool.com)
