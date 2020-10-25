import numpy as np
import matplotlib.pyplot as plt
import random as r

################
#   PARTIE 1   #
################


class Bateau:
    def __init__(self,nb):
        self.id=nb
        if nb==1:
            self.taille=5

        elif nb==2:
            self.taille=4

        elif nb==3:
            self.taille=3

        elif nb==4:
            self.taille=3

        elif nb==5:
            self.taille=2


# Convention: (0,0) en haut a gauche , sens vers la droite en bas (premier chiffre vertical, 2e horizontal)
# direction = 1 si position horizontale , 2 si verticale

def peut_placer(grille,bateau,position,direction):
    """   
    Parameters
    ----------
    grille : Array numpy à deux dimensions
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


grille=np.zeros((10,10))
def place(grille,bateau,position,direction):
    """
    Parameters
    ----------
    grille : Array numpy à deux dimensions
        La grille qui contiendra les tableaux
    bateau : Objet
        Bateau a placer
    position : tuple, 2 dimensions
        Positions x et y du point + haut + a gauche du bateau
    direction : int
        1 si horizontal , 2 vertical

    Returns
    -------
    Cette fonction renvoie l'array' 'grille' avec le bateau placé, si c'est possible

    """
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
    return grille
    
    

def place_ale(grille,bateau):
    """
    Parameters
    ----------
    grille : Array numpy à deux dimensions
        La grille qui contiendra les tableaux
    bateau : Objet
        Bateau a placer

    Returns
    -------
    L'array' 'grille' avec la bateau placé aléatoirement dessus

    """
    c1=r.randint(0,10)
    c2=r.randint(0,10)
    d=r.randint(1,2)
    #on donne des valeurs aleatoires aux coordonnes de position d'un bateau et à sa direction
    while not peut_placer(grille,bateau,(c1,c2),d):
        c1=r.randint(0,10)
        c2=r.randint(0,10)
        d=r.randint(1,2)
    grille=place(grille,bateau,(c1,c2),d)
    return grille

def eq(grilleA,grilleB):
    """
    Parameters
    ----------
    grilleA : Array numpy à deux dimensions
        Une grille de jeu
    grilleB : Array numpy à deux dimensions
        Une autre grille de jeu

    Returns
    -------
    bool
        True si les deux grilles sont égales (c'est a dire que pour x tq grilleA[i]=x et y tq grilleB[i]=y, on a pour tout i, x=y)

    """
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
    """
    Returns
    -------
    grille : Array numpy à deux dimensions
        Génère une grille de jeu correspondant à un placement valide de bateaux pour jouer a la bataille navale

    """
    grille=np.zeros((10,10))
    for i in range(1,6):
        bato=Bateau(i)
        place_ale(grille,bato)
    return grille       


def affiche(grille):
    """
    Parameters
    ----------
    grille : Array numpy à deux dimensions
        La grille de jeu

    Returns
    -------
    Image matplotlib
        Affiche l'image matplotlib correspondant à la grille de jeu 

    """
    return plt.imshow(grille)
