import sys
from MT_Config import *

def main():
    question = sys.argv[1] 

    if question == "q1":
        print("\nQuestion 1 : Proposer une structure de donn ees MT (une classe en Python) pour repr ́esenter une machine de Turing. Donner une deuxieme structure Configuration qui permet de representer la configuration d’une machine de Turing.")
        
        # MT Defintion d'une MT
        nb_rubans = 1
        I = 'q0'
        F = 'qAccept'
        Transitions = {('q0',('1',)):('q1',('-',),('<',)), 
                       ('q1',('_',)):('qAccept',('_',),('-',))}
        
        Machine_test = MT(nb_rubans,I,F,Transitions)

        print(f"\nMachine  de Turing de test créée : ")
        print(f"- nb rubans : {Machine_test.k} ruban")
        print(f"- État initial : {Machine_test.I}")
        print(f"- État final : {Machine_test.F}")

       # Configuration
        rubans_test = ["101"]
        tetes_test = [0]

        Config_test = Configuration(rubans_test, tetes_test, Machine_test.I)

        print(f"\nConfiguration :")
        print(f"- État courant : {Config_test.state}")
        print(f"- Contenu ruban(s) : {Config_test.rubans[:]}")
        print(f"- Position de(s) tête(s) : {Config_test.tete}")
    

    if question == "q2":
        print("\nQuestion 2 :  fonction qui initialise une instance de la structure MT depuis un fichier\nfonction qui cr ́ee la configuration initiale `a partir du mot d’entr ́ee et de la machine\n")
        nom_fichier = "divisible_par_3.txt"

        mot = "101"
        machine = charge_fichier(nom_fichier)
        Config = Configuration_Initiale(machine, mot)
        
        print(f"nb de rubans de la Machine chargée : {machine.k} rubans")
        print(f"État de départ : {Config.state}")
        print(f"Contenu des rubans : {Config.rubans}")
        print(f"Position des têtes : {Config.tete} \n")

    
    if question == "q3":
        print("\nQuestion 3 : Une fonction qui étant donnee une machine de Turing, lui fait éxecuter un pas de calcul\n")
        nom_fichier = "divisible_par_3.txt" 
        mot = "101" # 5 
        machine = charge_fichier(nom_fichier)
        Config = Configuration_Initiale(machine, mot)

        print(nom_fichier)

        print(f"\nNb rubans = {machine.k} rubans")
        print("Configuration AVANT UN PAS :")
        print(f"État de départ : {Config.state}")
        print(f"Contenu des rubans : {Config.rubans}")
        print(f"Position des têtes : {Config.tete}")

        Un_pas_de_Calcul(machine)
        print(f"\nConfiguration APRÈS UN PAS : ")
        print(f"État suivant : {Config.state}")
        print(f"Contenu des rubans : {Config.rubans}")
        print(f"Position des têtes : {Config.tete}")
    
    if question == "q4":
        print("\nQuestion 4 : Ecrire une fonction qui prend comme argument un mot et une machine de Turing et qui simule le calcul de la machine sur le mot jusqu’a atteindre l’ ́etat final \n")
        nom_fichier = "divisible_par_3.txt" #tester avec 11 (3) pour avoir ACCEPT 
        entree = "11"
        machine = charge_fichier(nom_fichier)

        print("Entrée : " , entree)

        config_finale = Execution_complete(machine, entree)
        print(f"{config_finale}\n")

    if question == "q5":
        print("\nQuestion 5 : Faire une fonction qui permet d’afficher les configurations de la machine au fur et a mesure de son fonctionnement\n")
        nom_fichier = "divisible_par_3.txt" #tester avec 11 (3) pour avoir ACCEPT 
        entree = "11"

        machine = charge_fichier(nom_fichier)

        print(Configuration_Machine(machine,entree))

    if question == "q6_1":
        # Comparaison d’entiers : `a partir d’une entr ́ee x#y o`u x et y repr ́esentent des entiers en binaire, s’arrˆeter si x < y et boucler `a l’infini sinon
        print("\nQuestion 6_1 : Donner des machines de Turing qui r ́ealisent les fonctions suivantes et testez les avec votre simulateur")
        nom_fichier = "MT1.txt"
        mot = "10#100"
        print(nom_fichier, mot)
        machine = charge_fichier(nom_fichier) 

        retour = Execution_complete(machine,mot)
        print(retour)

    if question == "q6_2":
        # Recherche dans une liste : dans une entree de la forme x#w1#w2# . . . #wl, ou x et les wi sont des mots de {0, 1}∗, s’arreter si x = wi pour un des wi et boucler sinon
        print("\nQuestion 6_2 : Donner des machines de Turing qui r ́ealisent les fonctions suivantes et testez les avec votre simulateur")
        nom_fichier = "MT2.txt"
        mot = "1000#100#10#1000"
        print(nom_fichier, mot)
        machine = charge_fichier(nom_fichier) 

        retour = Execution_complete(machine,mot)
        print(retour)

    if question == "q6_3":
        # Multiplication en unaire : `a partir d’une entr ́ee 1n#1m, produire la sortie 1nm
        print("\nQuestion 6_3 : Donner des machines de Turing qui r ́ealisent les fonctions suivantes et testez les avec votre simulateur")        
        nom_fichier = "MT3.txt"
        mot = "11#111"
        print(nom_fichier, mot)
        machine = charge_fichier(nom_fichier) 

        retour = Execution_complete(machine,mot)

        ruban_resultat = retour.rubans[2]

        print("Résultat :", "".join(ruban_resultat).strip("_"))

    if question == "q7":
        print("\nQuestion 7 : Donner une fonction qui lit un fichier contenant une la description d’une machine dans le format de Turing Machine Simulator et qui produit le codage d'ecrit precedemment. \nQue faudrait-il faire si on veut pouvoir accepter n’importe quel alphabet de travail ? \n")
        nom_fichier = "MT1.txt"
        print("Code de la machine est :\n")
        code = Codage_Machine(nom_fichier)
        print(f"{code} \n")

    if question == "q8_1":
        # On ne peut pas utiliser nos MT de Q6 car elles ont plusieurs rubans. 
        # Tests avec MT à 1 Ruban : les MT test de la question Q9 (ou fichier palindrome.txt divisible_par_3.txt)
        print("\nQuestion 8_1 : Définir un codage binaire du format de machine de Turing, écrire une fonction qui convertit une description en chaîne en ce codage, puis afficher ce codage, sa version binaire et l’entier correspondant pour les machines données.")
        
        nom_fichier = "test_q9.txt"
        print("Machine :  \n")
        codage,codage_binaire,entier = Codage_Binaire(nom_fichier)
        print("Codage MT1 : ", codage)
        print("Codage binaire : ", codage_binaire)
        print("Interprétation entier : ", entier )

    if question == "q8_2":
        print("\nQuestion 8_2 : Définir un codage binaire du format de machine de Turing, écrire une fonction qui convertit une description en chaîne en ce codage, puis afficher ce codage, sa version binaire et l’entier correspondant pour les machines données.")
        nom_fichier = "test2_q9.txt"
        print("Machine :  \n")
        codage,codage_binaire,entier = Codage_Binaire(nom_fichier)
        print("Codage MT2 : ", codage)
        print("Codage binaire : ", codage_binaire)
        print("Interprétation entier : ", entier )
    
    if question == "q8_3":
        print("\nQuestion 8_3 : Définir un codage binaire du format de machine de Turing, écrire une fonction qui convertit une description en chaîne en ce codage, puis afficher ce codage, sa version binaire et l’entier correspondant pour les machines données.")
        nom_fichier = "test3_q9.txt"
        print("Machine :  \n")
        codage,codage_binaire,entier = Codage_Binaire(nom_fichier)
        print("Codage MT2 : ", codage)
        print("Codage binaire : ", codage_binaire)
        print("Interprétation entier : ", entier )

    if question == "q9_1":
        # MT qui change les 0 en 1 et les 1 en 0
        print("\nQuestion 9_1 : Donner la machine de Turing universelle `a trois rubans, qui prend sur son ruban d’entr ́ee < M > #x et qui simule M sur x. Simuler votre machine universelle sur un exemple de machine < M > de votre choix.")
        nom_fichier_uni = "test_q9.txt"
        nom_fichier = "MT_question9.txt"
        x = "110011"
        codage = Codage_Machine(nom_fichier_uni)

        entree = codage + "#" + x
        print("entree : ", entree)
        machine = charge_fichier(nom_fichier) 

        config_finale = Execution_complete(machine,entree)

        ruban_1 = config_finale.rubans[0]
        ruban_resultat = config_finale.rubans[1]

        print("resultat : ",ruban_resultat)
        print(ruban_1)

    if question == "q9_2":
        # Incrémentation binaire
        print("\nQuestion 9_2 : Donner la machine de Turing universelle `a trois rubans, qui prend sur son ruban d’entr ́ee < M > #x et qui simule M sur x. Simuler votre machine universelle sur un exemple de machine < M > de votre choix.")
        nom_fichier_uni = "test2_q9.txt"
        nom_fichier = "MT_question9.txt"
        x = "1011"
        codage = Codage_Machine(nom_fichier_uni)

        entree = codage + "#" + x
        print("entree : ", entree)
        machine = charge_fichier(nom_fichier) 

        config_finale = Execution_complete(machine,entree)

        ruban_1 = config_finale.rubans[0]
        ruban_resultat = config_finale.rubans[1]

        print(ruban_resultat)
        print(ruban_1)

    if question == "q9_3":
        # palindrome
        print("\nQuestion 9_3 : Donner la machine de Turing universelle `a trois rubans, qui prend sur son ruban d’entr ́ee < M > #x et qui simule M sur x. Simuler votre machine universelle sur un exemple de machine < M > de votre choix.")
        nom_fichier_uni = "test3_q9.txt"
        nom_fichier = "MT_question9.txt"
        x = "001"
        codage = Codage_Machine(nom_fichier_uni)

        entree = codage + "#" + x
        print("entree : ", entree)
        machine = charge_fichier(nom_fichier) 

        config_finale = Execution_complete(machine,entree)

        print("codage : ", codage)

        ruban_resultat = config_finale.rubans[1]
        print("\nruban_resultat : ", ruban_resultat)
    

    if question == "q10":
        print("\nQuestion 10 : Ajouter un ruban et la gestion d’un compteur `a votre machine universelle de fa ̧con `a obtenir une machine qui sur une entr ́ee < M > #x#n simule M sur l’entr ́ee x pendant n  ́etapes")
        nom_fichier_uni = "test3_q9.txt"
        nom_fichier = "MT_question10.txt"
        x = "01"
        codage = Codage_Machine(nom_fichier_uni)

        entree = codage + "#" + x + "#" +  "1111"
        print("entree : ", entree)
        machine = charge_fichier(nom_fichier) 

        config_finale = Execution_complete(machine,entree)

        ruban_resultat = config_finale.rubans[1]

        print(ruban_resultat)



    if question == "q11":
        print("\n Question 11 :  Pour les langages suivants, prouver s’ils sont d ́ecidables ou ind ́ecidables")
        print("\nLangage L1")
        print("L1 = { <M>#n | M s'arrête sur n en moins de n étapes }")
        print("Réponse : décidable \n")
        print("On a construit une MTU qui simule M sur l'entrée avec un compteur à un nombre d'étape limité determiné \n Puisque n est une valeur finie notre simulation va obligatoirement s'arrêter dans un temps fini M s'est arrêtée par acceptation ou alors nombre de tours ecoulés ")

        print("Langage L2")
        print("L2 = { <M>#n | M s'arrête sur les mots de taille n } ")
        print("Réponse : indécidable \n")
        print("Réduction au problème de l'arrêt : \n")
        print("Supposons par l'absurde qu'un décideur D2 existe pour L2.")
        print("On pourrait l'utiliser pour savoir si une machine M s'arrête sur un mot w")
        print("Pour cela, on crée une machine truquée M' qui ignore son entrée")
        print("et exécute systématiquement M sur w")
        print("Si on donne <M'>#n à D2, D2 dira OUI si M' s'arrête sur les mots")
        print("de taille n, ce qui équivaut à dire que M s'arrête sur w")
        print("D2 nous donnerait la solution au problème de l'arrêt, ce qui est")
        print("une contradiction mathématique absolue. L2 est donc indécidable\n")
        print("Langage L3")


        print("L3 = { <M>#x#y | M calcule la même chose sur les entrées x et y }")
        print("Réponse : indécidable \n ")
        print("Pour savoir si M fait 'la même chose' sur x et y on va comparer")
        print("les deux calculs, donc on doit les simuler jusqu'à leur terme.")
        print("Si M boucle à l'infini sur l'entrée x, tout algorithme de vérification")
        print("sera pris dans cette boucle infinie en tentant de la simuler et")
        print("ne pourra jamais rendre de réponse.")
        print("Puisqu'aucun algorithme ne peut garantir de répondre par OUI ou NON")
        print("dans un temps fini à 100%, L3 est indécidable.")



if __name__ == "__main__":
    main()


