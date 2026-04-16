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
    etats = []
    etat_init = "" 
    accept_s = ""
    reject_s = ""
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
                parts_L1 = ligne.split(',')
                etat_courant = parts_L1[0]
                symboles_lus = tuple(parts_L1[1:]) # Prend tous sauf le premier élement de parts_L1
            
                nb_rubans = len(symboles_lus)

                # Ligne 2
                i += 1 
                ligne = lignes[i]
                parts_L2 = ligne.split(',')
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

    while True: 
        if machine.configuration.state == machine.F:
            return "ACCEPTER"
        retour = Un_pas_de_Calcul(machine)
        
        if retour is None:
            return "REJETER"

# Question 5 : 
        
def Configuration_Machine(machine,entrée):
    Configuration_Initiale(machine,entrée)

    while True:
        print(machine.configuration.ruban) 
        print(machine.configuration.tete) 
        print(machine.configuration.state) 

        if machine.configuration.state == machine.F:
            return "ACCEPTER"
        retour = Un_pas_de_Calcul(machine)
        
        if retour is None:
            return "REJETER"

# Question 6 :
        
