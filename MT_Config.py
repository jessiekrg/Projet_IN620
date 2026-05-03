#Q1
class Configuration:
    def __init__(self,rubans,tete,state):
        self.rubans = [list(r) for r in rubans] # Rubans = liste des rubans : de base c'est genre ["10", "__"] par exemple et là ca devient une [["1","0"], ["_","_"]]
        self.tete = list(tete) # Indices dans les ruban  (ex : [0,0] ) 
        self.state = state # Etat courant (c'est le nom genre "q0")

class MT:
    def __init__(self,k, I, F, transitions):
        self.k = k # Nombre de rubans 
        self.I = I
        self.F = F
        self.transitions = transitions # Dictionnaire { (etat courant , indice du symbole lu) : (etat suivant,)}
        self.configuration = None # Pour Q3


# Q2 Partie 1
def charge_fichier(fichier):
    """ Lit ficher"""
    # Initialisation 
    nb_rubans = 1 
    etat_init = "" 
    accept_s = ""
    transitions = {}

    with open(fichier, 'r') as f:
        lignes = [l.strip() for l in f if l.strip() and not l.strip().startswith('//')] #Liste de chacune des lignes descriptives (on fait abstraction des commentaires et sauts de lignes)

        # Parcours chacunes des lignes 
        i = 0
        while i < len(lignes):
            ligne = lignes[i]
            if ligne.startswith('init:'): # Etat Initial
                etat_init = ligne.split(':')[1].strip() # etat_init = q0
            elif ligne.startswith('accept:'): # Etat Accept
                accept_s = ligne.split(':')[1].strip()

            # Transitions : | qCopy,_,_ | qReturn,_,_,-,< |
        
            elif ',' in ligne: 
                # Ligne 1
                parts_L1 = [p.strip() for p in ligne.split(',')]
                etat_courant = parts_L1[0]
                symboles_lus = tuple(parts_L1[1:]) # Prend tous sauf le premier élement de parts_L1
            
                nb_rubans = len(symboles_lus)

                # Ligne 2
                i += 1 
                ligne = lignes[i]
                parts_L2 = [p.strip() for p in ligne.split(',')]
                etat_suivant = parts_L2[0]
                symboles_ecrit = tuple(parts_L2[1: 1 + nb_rubans])
                mouvements = tuple(parts_L2[1 + nb_rubans: 1 + 2 * nb_rubans])


                cle = (etat_courant, symboles_lus)

                transitions[cle] = (etat_suivant, symboles_ecrit, mouvements) 

            i += 1
        
    return MT(nb_rubans, etat_init, accept_s, transitions)

# Q2 Partie 2

def Configuration_Initiale(machine,entrée):

    # Initialisation des Rubans et des têtes 
    rubans_initiaux = [list(entrée)] # INITIALEMENT : le ruban 1 contient notre chaine et les autres (k rubans) sont tous vides (_)
    for i in range(1,machine.k):
        rubans_initiaux.append(['_'])
    
    tete_initales = [0] * machine.k # INITIALEMENT : les tête des rubans sont toutes postitionnée à l'indice 0

    # On stocke la configuration intiale dans une variable (stocke) = on creait l'objet configuration
    Ma_Configuration = Configuration(rubans_initiaux, tete_initales, machine.I)
    machine.configuration = Ma_Configuration # Pour Q3
    return Ma_Configuration # On retourne pour que main.py l'utilises

# Q3 Partie 2
def Un_pas_de_Calcul(machine):
    # Récupération de la configuration courante donc je récupère (l'état courant, symboles lus par rubans) 
    Etat_Courant = machine.configuration.state
    Symboles_lus = []
    nb_rubans = machine.k

    for i in range(0,nb_rubans):
        ruban_i = machine.configuration.rubans[i]
        Position_tete = machine.configuration.tete[i]
        Symboles_lus.append(machine.configuration.rubans[i][Position_tete])

    Symboles_lus_tuple = tuple(Symboles_lus) 
    cle = (Etat_Courant,Symboles_lus_tuple)

    print(f"DEBUG : État={Etat_Courant} | Lus={Symboles_lus_tuple}")
    
    # chercher dans le dictionnaire transitions { ()
    if cle in machine.transitions:
        (etat_suivant, symboles_ecrit, mouvements) = machine.transitions[cle]
    else:
        return 
    
    # Mettre a jour la configuration donc changer l'état (état suivant, symboles | écrire sur les rubans + deplacement des têtes)
    machine.configuration.state = etat_suivant

    for i in range(0,nb_rubans): # Je remplace chacun des symboles_lus du rubans par les symboles écrits 
        ruban_i = machine.configuration.rubans[i]
        Position_tete = machine.configuration.tete[i]
        machine.configuration.rubans[i][Position_tete] = symboles_ecrit[i]

        #déplacmement des têtes

        if mouvements[i] == '>':
            machine.configuration.tete[i] += 1
    
        elif mouvements[i] == '<':
            machine.configuration.tete[i] -= 1
    
        elif mouvements[i] == '-':
            machine.configuration.tete[i] += 0 # En vrai je peux enlever ca mais je prèfere garder pour garder une certaine uniformité

        if machine.configuration.tete[i] < 0:
            machine.configuration.rubans[i].insert(0, '_')
            machine.configuration.tete[i] = 0
        
        if machine.configuration.tete[i] == len(machine.configuration.rubans[i]):
            machine.configuration.rubans[i].append('_')

    nouvelle_config = machine.configuration
    return nouvelle_config

# Question 4 : 
def Execution_complete(machine,entrée):

    Configuration_Initiale(machine,entrée)
    tour = 0
    while True: 
        if machine.configuration.state == machine.F:
            print("ACCEPTER")
            return machine.configuration
        
        if machine.configuration.state == "q5":
            pos4 = machine.configuration.tete[3]

            if machine.configuration.rubans[3][pos4] == "1":
                tour += 1
                print("Tour", tour)
        
        retour = Un_pas_de_Calcul(machine)
        if retour is None: 
            print(f"BLOQUÉ à l'état : {machine.configuration.state}")
            return machine.configuration
        


# Question 5 : 
        
def Configuration_Machine(machine,entrée):
    Configuration_Initiale(machine,entrée)

    while True:
        print(machine.configuration.rubans) 
        print(machine.configuration.tete) 
        print(machine.configuration.state) 

        if machine.configuration.state == machine.F:
            return "ACCEPTER"
        retour = Un_pas_de_Calcul(machine)
        
        if retour is None:
            return None

# Question 7
        
def Codage_Machine(fichier):
    dic_etat = {} # on attribut pour chaque état de la MT un entier à partir du cpt
    cpt = 2
    resultat = [] #tableau qui regroupe toutes les transitions de la MT
    with open(fichier, 'r') as f:
        lignes = [l.strip() for l in f if l.strip() and not l.strip().startswith('//')]

        i = 0
        while i < len(lignes):
            ligne = lignes[i]
            if ligne.startswith('init:'): # Etat Initial
                etat_init = ligne.split(':')[1].strip() # etat_init = q0
                dic_etat[etat_init] = "0"
                i+=1 #On passe à la ligne suivante

            elif ligne.startswith('accept:'): # Etat Accept`
                accept_s = ligne.split(':')[1].strip()
                dic_etat[accept_s] = "1"
                i+=1 #On passe à la ligne suivante

            elif ',' in ligne:
                parts_L1 = ligne.split(',')
                etat_courant = parts_L1[0].strip()
                symbole_lu = parts_L1[1].strip()

                if symbole_lu == "_":
                    symbole_lu = "□"

                
                # Ajout dans le dictionnaire état Ligne 1
                if etat_courant not in dic_etat:
                    etat_binaire = bin(cpt)[2:] # cpt décimal --> en binaire
                    dic_etat[etat_courant] = etat_binaire
                    cpt += 1

                i+= 1

                # Ajout dans le dictionnaire état Ligne 1
                ligne = lignes[i]
                parts_L2 = ligne.split(',')
                etat_suivant = parts_L2[0].strip()
                symbole_ecrit = parts_L2[1].strip()
                direction = parts_L2[2].strip()

                if symbole_ecrit == "_":
                    symbole_ecrit = "□"
    

                if etat_suivant not in dic_etat:
                    etat_binaire = bin(cpt)[2:]
                    dic_etat[etat_suivant] = etat_binaire
                    cpt += 1
            
                code_etat_courant = dic_etat[etat_courant]
                code_etat_suivant = dic_etat[etat_suivant]

                resultat.extend([code_etat_courant,symbole_lu,symbole_ecrit,direction,code_etat_suivant]) #.extend() pour pouvoir ajouter plusieurs élements

                i+=1 
            else :
                i+= 1 # rajouté pour forcer le programme à ignorer les lignes non reconnues et à passer à la suivante
    
    chaine_finale = "|".join(resultat)

    return chaine_finale

# Question 8

def Codage_Binaire(fichier):
    tbl_binaire = []
    codage = Codage_Machine(fichier)

    # dictionnaire de correspondance pour que chaque caractère soit codé en un nombre a trois bits
    d_correspondance = {"0" : "000", "1" : "001", "|" : "011", "□" : "111", "#" : "010", "<" : "100", ">" : "101", "-" : "110"}


    for i in codage:
        tbl_binaire.append(d_correspondance[i])

    chaine_binaire = "".join(tbl_binaire)
    valeur_entiere = int(chaine_binaire, 2)

    return codage,chaine_binaire,valeur_entiere

# Question 9


def Machine_Turing(entree): # entrée qui aura la forme < M > #x
    """Machine de Turing universelle `a trois rubans, qui prend sur son ruban d’entr ́ee
    < M >#x et qui simule M sur x"""
    Parsing = entree.split("#")

    ruban1 = Parsing[0].split('|') # on crée un tableau à partir du ruban 1 pour pouvoir parcourir le ruban
    ruban2 = list(Parsing[1])  # entree est une chaine de caractère, on utilise une liste pour pouvoir la modifier
    etat_actuel = "0" # ruban 3
    cpt_ruban2 = 0


    while etat_actuel != "1" :

        transition_trouvee = False
        
        symbole_lu = ruban2[cpt_ruban2]

        for i in range(0,len(ruban1),5):
            if ruban1[i] == etat_actuel and ruban1[i+1] == symbole_lu:
                ecrit = ruban1[i+2]
                direction = ruban1[i+3]
                etat_suivant = ruban1[i+4]
                transition_trouvee = True
                break

        if not transition_trouvee:
            print("Erreur : La transition n'a pas été trouvé")
            break

        ruban2[cpt_ruban2] = ecrit

        if direction == ">":
            cpt_ruban2 += 1
            if cpt_ruban2 == len(ruban2):
                ruban2.append("_")
        if direction == "<":
            cpt_ruban2 -= 1
            if cpt_ruban2 < 0 :
                ruban2.insert(0, "_")
                cpt_ruban2 = 0

        etat_actuel = etat_suivant # Mise à jour du ruban 3
    
    return "".join(ruban2)




# Question 10


def Machine_Turing_Universelle_Compteur(chaine): # Format de l'entrée serait : < M >#x#n 
    
    Parties = chaine.split('#')

    # Je divise l'entrée en trois disctincte parties : le code de la MT, l'entrée, le nombre d'étapes durant laquelle la MTU simule 
    M_Ruban1 = Parties[0].split("|") 
    x_Ruban2 = list(Parties[1])
    Etat_Ruban_3 = "0"
    n_Ruban4 = int(Parties[2]) 


    etat_actuel = Etat_Ruban_3
    position_tete_lecture = 0
    compteur_n = 0
    transition_trouvee = False

    while (etat_actuel != "1") and (compteur_n < n_Ruban4):

        transition_trouvee = False
        symbole_lu = x_Ruban2[position_tete_lecture] 

        for i in range(0,len(M_Ruban1),5):

            if (M_Ruban1[i] == etat_actuel) and (M_Ruban1[i+1] == symbole_lu): # Si on trouve un correspondance de l'état actuel , symboles 
                # Récupération de ce qui doit être ecrits et le mouvement de la tête
                ecrit = M_Ruban1[i+2]
                direction = M_Ruban1[i+3]

                etat_actuel = M_Ruban1[i+4] # Mise à jour de l'état courant par l'état suivant 
                transition_trouvee = True 

                # Ecriture 
                x_Ruban2[position_tete_lecture] = ecrit

                # Mouvement de la tête de lecture
                if direction == ">":
                    position_tete_lecture += 1
                    if position_tete_lecture == len(x_Ruban2):
                        x_Ruban2.append("_")
            
                if direction == "<":
                    position_tete_lecture -= 1
                    if position_tete_lecture < 0 :
                        x_Ruban2.insert(0, "_")
                        position_tete_lecture = 0
                break
            
        if not transition_trouvee:
            print("Erreur : La transition n'a pas été trouvé")
            break

        
        compteur_n += 1
    
    return "".join(x_Ruban2)



                   


            

        



      
    



    
        
