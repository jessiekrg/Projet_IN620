# Projet_IN620
Binôme : 
Lina Berroug
Jessica Karega

Présentation du projet : 
Implémente un simulateur complet de Machines de Turing (MT) en Python

Fichiers : 
- main.py : Point d'entrée principal gérant les arguments de la ligne de commande.
- MT_Config.py : Cœur du simulateur (Classes MT/Configuration, parseur, logique de calcul).
- Makefile : Automatisation des tests pour chaque question du sujet.
- Machines de Turing (.txt) :
    * divisible_par_3.txt : Test de divisibilité binaire (issus du site)
    * MT1.txt à MT3.txt : Machines pour la Question 6 
    * MT_question9.txt / MT_question10.txt : Implémentations de la Machine Universelle.
    * test_q9.txt, test2_q9.txt, test3_q9.txt : Machines 1 ruban pour tester la MTU.

commandes : 
make q1 : Initialisation des structures de données MT et Configuration
make q2 : Chargement d'une machine depuis un fichier et configuration initiale
make q3 : Execution d'un pas de calcul unique
make q4 : Simulation complète d'un mot jusqu'à l'état final
make q5 : Affichage des configurations au fur et à mesure du fonctionnement
make q6_1 : Comparaison d'entiers binaires : s'arrête si x < y
make q6_2 : Recherche dans une liste : s'arrête si x = wi
make q6_3 : Multiplication unaire : produit 1n#1m -> 1nm
make q7 : Codage d'une MT 
make q8_1 / q8_2 / q8_3 : Codage binaire et interprétation entière d'une machine.
make q9_1 / q9_2 / q9_3 : Machine Universelle : simulation de <M>#x
make q10 : MTU avec Compteur : simulation limitée à n étapes
make q11 : Réponses théoriques sur la décidabilité (L1, L2, L3)