"""
PROJET L3 INFO 20-21
Vincent + Francesco
Bataille navale
"""



"""
PARTIE 1
"""


import numpy as np
import matplotlib.pyplot as plt
import random as r 

# nomBateau(id)=taille

# porteAvion(1)=5
# croiseur(2)=4
# contreTorpilleur(3)=3
# sousMarin(4)=3
# torpilleur(5)=2

grille=np.zeros((10,10))
class Bateau:
    def __init__(self,nb):
        self.id=nb
        if nb==1:
            self.taille=5
            self.nom="Porte-avions"
        elif nb==2:
            self.taille=4
            self.nom="Croiseur"
        elif nb==3:
            self.taille=3
            self.nom="Contre-torpilleurs"
        elif nb==4:
            self.taille=3
            self.nom="Sous-marin"
        elif nb==5:
            self.taille=2
            self.nom="Torpilleur"


def affiche(grille):
    return plt.imshow(grille)



# Convention: (0,0) en haut a gauche , sens vers la droite en bas (premier chiffre vertical, 2e horizontal)
# direction = 1 si position horizontale , 2 si verticale

def peut_placer(grille,bateau,position,direction):
    """
    

    Parameters
    ----------
    grille : Tableau a 2 dimensions
        La grille qui contiendra les tableaux
    bateau : Objet
        Bateau a placer
    position : tuple, 2 dimensions
        Positions x et y du point + haut + a gauche du bateau
    direction : int
        1 si horizontal , 2 vertical

    Returns
    -------
    bool
        True si la position est valide, False sinon

    """
    c1=position[0]
    c2=position[1]
    if (not 0<=c1<10) or (not 0<=c2<10) :
        return False #origine du bateau pas dans la grille
    if direction==1:
        if not c2+bateau.taille<=10:
            return False #fin du bateau pas dans la grille
        for i in range(c2,c2+bateau.taille):
            if grille[c1][i]!=0:
                return False #case deja occupee, le bateau ne peut etre place
    else: #idem que precedent mais pour vertical
        if not c1+bateau.taille<=10:
            return False 
        for i in range(c1,c1+bateau.taille):
            if grille[i][c2]!=0:
                return False
    return True

def place(grille,bateau,position,direction):
    c1=position[0]
    c2=position[1]
    if not peut_placer(grille,bateau,position,direction):
        print("Le bateau ne peut être placé")
        return False

    if direction==1:     
        for i in range(c2,c2+bateau.taille):
            grille[c1][i]=bateau.id
    else:
        for i in range(c1,c1+bateau.taille):
            grille[i][c2]=bateau.id
    #On a place le bateau, en donnant a chacune des cases qui le compose son numero id
            
def place_ale(grille,bateau):
    c1=r.randint(0,10)
    c2=r.randint(0,10)
    d=r.randint(1,2)
    #on donne des valeurs aleatoires aux coordonnes de position d'un bateau et à sa direction
    while not peut_placer(grille,bateau,(c1,c2),d):
        c1=r.randint(0,10)
        c2=r.randint(0,10)
        d=r.randint(1,2)
    place(grille,bateau,(c1,c2),d)

def eq(grilleA,grilleB):
    if grilleA.shape!=grilleB.shape:
        #On teste l'egalite des tailles des grilles
        return False
    #Si tailles egales, on compare les elements deux a deux
    for i in range(0, grilleA.shape[0]-1):
        for j in range(0, grilleA.shape[1]-1):
            if grilleA[i][j] != grilleB[i][j]:
                return False
    return True

def genere_grille():
    grille=np.zeros((10,10))
    for i in range(1,6):
        bato=Bateau(i)
        place_ale(grille,bato)
    return grille       


"""
PARTIE 2
"""


""" QUESTION 2 """

#Version à peine utile pour une grille vide et un seul bateau
""" def nbconfigs_bateau2(bateau): #On suppose que la grille est de taille 10
    return 20*(10-bateau.taille+1) 
    #Pour une ligne/colonne donnée, il y a 10-bateau.taille+1 configs.
    #Il y a 20 lignes et colonnes, donc on multiplie par 20
"""

def nbconfigs_bateau(bateau): #On suppose que la grille est de taille 10
    lgrille = []
    grille = np.zeros((10,10))
    for i in range (0,10):      #On stocke toutes les grilles possibles dans une liste
        for j in range (0,10):
            if peut_placer(grille, bateau, (i,j), 1):
                place(grille, bateau, (i,j), 1)
                lgrille.append(grille)
                grille = np.zeros((10,10))
            if peut_placer(grille, bateau, (i,j), 2):
                place(grille, bateau, (i,j), 2)
                lgrille.append(grille)
                grille = np.zeros((10,10))
    return len(lgrille)

""" QUESTION 3 """


#Fonction ajoutée pas explicitement demandée ni interdite dans l'énoncé
def liste_configs_bateau(grille, bateau): #Renvoie la liste des configs du bateau sur la grille
    lgrille = []
    G = grille.copy()
    for i in range (0,10):
        for j in range (0,10):
            if peut_placer(grille, bateau, (i,j), 1):
                place(grille, bateau, (i,j), 1)
                lgrille.append(grille)
                grille = G.copy()
            if peut_placer(grille, bateau, (i,j), 2):
                place(grille, bateau, (i,j), 2)
                lgrille.append(grille)
                grille = G.copy()
    return lgrille

def nbconfigs_liste(liste):
    if len(liste) == 0 :
        return 1
    if len(liste) == 1 :
        return nbconfigs_bateau(liste[0]) #version 2 plus rapide mais peu utile
    liste_configs = liste_configs_bateau(np.zeros((10,10)), liste[0])
    for k in range (1, len(liste)):
        liste_cour = liste_configs.copy()
        liste_configs.clear()
        for i in range(0, len(liste_cour)):
            liste_configs += liste_configs_bateau(liste_cour[i], liste[k])
    return len(liste_configs)


""" QUESTION 4 """

def nb_genere(grille):
    res = 1
    rand = genere_grille()
    while not (eq(grille, rand)):
        res += 1
        rand = genere_grille()
    return res

""" Pour effectuer des tests
G = genere_grille()
s=0
affiche(G)
for i in range (1, 101):
    s += nb_genere(G)
print(s/100)
"""

""" QUESTION 5 """

def genere_grille_liste(liste): #Genere une grille aleatoire contenant les bateaux d'une liste donnee
    grille=np.zeros((10,10))
    for i in range(0,len(liste)):
        place_ale(grille,liste[i])
    return grille  

def approximer(liste):
    grille = genere_grille_liste(liste)
    res = 0
    for i in range (1,101):
        rand = genere_grille_liste(liste)
        s = 1        
        while not (eq(grille, rand)):
            rand = genere_grille_liste(liste)
            s += 1            
        res += s
    return res/100


""" PARTIE 3 """


# porteAv=Bateau(1)
# crois=Bateau(2)
# contreT=Bateau(3)
# sousM=Bateau(4)
# torp=Bateau(5)
class Bataille:
    def __init__(self):
        self.grille=genere_grille()
    def reset(self):
        self.grille=np.zeros((10,10))
    def joue(self,position):
        x,y=position[0],position[1]

        if self.grille[x][y]!=0.0:
            self.grille[x][y]=9.0
            return True
        return False
    def victoire(self):
        for x in self.grille:
            for y in x:
                if y not in [0,9]:
                    return False
        return True
class JoueurAleat:
    
    def __init__(self):
        self.coup=(r.randint(0,9),r.randint(0,9))
        self.coups=[]
        for i in range(10):
            for j in range(10):
                self.coups.append((i,j))


    def genere_coup(self):

        if len(self.coups)>0:
            x=r.randint(0,len(self.coups)-1)
            self.coup=self.coups[x]
            self.coups.remove(self.coup)
        else:
            print("Plus de coups")

class JoueurHeuri:
    
    def __init__(self):
        self.reussite=False
        self.coup=(r.randint(0,9),r.randint(0,9))
        self.coups=[]
        self.posRacine=(0,0) #a partir de la, on commence a exploiter le reste
        self.dir=0 #si 1, hor droite, -1 hor gauche, 2 vert bas , -2 vert hau
        self.pos_heuri=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(10):
            for j in range(10):
                self.coups.append((i,j))

    def coup(self):
        if not reussite:
            genere_coup_aleat()
        else:
            genere_coup_heuri()
    

    def genere_coup_aleat(self):
            x=r.randint(0,len(self.coups)-1)
            self.coup=self.coups[x]
            self.coups.remove(self.coup)


    def genere_coup_heuri(self):
            iDirec=1
            direc=pos_heuri[iDirec]
            if 0<=posRacine[0]+direc[0]<=9 and posRacine[1]+direc[1]<=9:
                self.coup=(posRacine[0]+direc[0],posRacine[1]+direc[1])
            """if coup pas bon:"""
            """
            On determine une direction (tester ttes direcs apres echecs precedents)
            On fait une racine qui correspond au premier succes, on la laisse tant que les 4 directions ont pas ete exploitees
            Apres avoir determine une direction, a chaque coup successif on met une racine temporaire
            Quand le coup devient plus bon, on va dans le sens oppose, a partir de la racine initiale
            On repete jusqua avoir isole les possibilites, et on revient en aleatoire
            """
            
        


    
def jouerAleat():
    jeu=Bataille()
    
    joueur=JoueurAleat()
    i=0
    while not jeu.victoire():
        joueur.genere_coup()
        jeu.joue(joueur.coup)
        i+=1
    return i


    
def histoJouerAleat():
    coups=[]
    for _ in range(100):
        nb=jouerAleat()
        coups.append(nb)
    
    fig,ax = plt.subplots(1,1)
    ax.hist(coups, bins=101)
    ax.set_xticks([0,25,50,75,100])
    

    
#histoJouerAleat()

