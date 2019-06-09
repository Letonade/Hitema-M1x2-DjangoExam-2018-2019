# Hitema-M1x2-DjangoExam-2018-2019

Calculette 

La calculette est accesible sur le lien suivant:
http://127.0.0.1:8000/core/calcul/
apres avoir lance le serveur avec la commande 
 python manage.py runserver
dans le dossier du projet qui s'appel calc

Fonctionnement de la calculatrice

appuier sur sur les chiffre pour cree le premier chiffre
(exemple on appuie sur 4 ensuite sur 5 ça nous fait un chiffre 45)
quand on a choisit un chiffre on doit choisire une opperation add, substract, multiply ou divide
quand on a choisit l'opertion on fait le deuxieme chiffre
quand on a 2 chiffre et une opperation on peut soit faire equal pour faire l'operation ou de choisire une deuxieme operation
si on a choisit equal :
la calculette fait l'opertation et affiche le resultat comme le premier chiffre
si on choisit la deuxieme operation:
la calculette fait l'opertation et affiche le resultat comme le premier chiffre et l'operation

chaque calcul est enregister et on affiche chaque calcul dans la liste en bas

a chaque moment on peut apuuier sur CE qui va vider le calculatrice(mais pas les enregistrements)

chaque operation peut etre accesible via des urls et fera la meme chose que si on la faisait sur calculatrice.

