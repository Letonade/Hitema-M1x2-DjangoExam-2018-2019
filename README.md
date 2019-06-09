# Hitema-M1x2-DjangoExam-2018-2019

Calculette 

Apres avoir lancé le serveur avec la commande 
 python manage.py runserver
dans le dossier du projet qui nommé calc la calculatrice est alors accesible au lien suivant:
http://127.0.0.1:8000/core/calcul/

Fonctionnement de la calculatrice:

Une touche par chiffre, on créer un premier chiffre qui devient alors un nombre,
une fois le premier nombre saisi on utilise une touche d'opération (+,-,X,/),
on peut alors créer un second nombre,
il est alors possible d'utiliser égal ou une nouvelle opération,
égal éxécute l'opération et fait afficher la calculatrice le résultat, elle retourne à l'étape n'ayant qu'un nombre
une opération est un égal possédant un opérateur en plus.

Chaque calcul est enregistré puis affiché dans la liste au dessous.
A tout moment on peut utiliser la touche CE de la calculatrice afin de vider le buffer, l'historique est different du buffer.
Chaque operation posséde un lien permettant de remonter jusqu'à l'étape de calcul historisée.
