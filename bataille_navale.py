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



# Convention: (0,0) en haut a gauche , sens vers la droite en bas
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
    if (not 0<=c1<=10) and (not 0<=c2<=10) :
        return False #origine du bateau pas dans la grille
    if direction==1:
        if not c2+bateau.taille<=10:
            return False #fin du bateau pas dans la grille
        for i in range(c2,c2+bateau.taille):
            if not 0<=grille[c1][i]<=10 or grille[c1][i]!=0:
                return False #totalite du bateau pas dans la grille
            if grille[c1][i]!=0:
                return False #case deja occupee, le bateau ne peut etre place
    else: #idem que precedent mais pour vertical
        if not c1+bateau.taille<=10:
            return False 
        for i in range(c1,c1+bateau.taille):
            if not 0<=grille[i][c2]<=10 or grille[i][c2]!=0:
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
    lim=10-bateau.taille #le bateau ne pourra pas etre place si il commence apres cette limite
    c1=r.randint(0,10-lim)
    c2=r.randint(0,10-lim)
    d=r.randint(1,2)
    #on donne des valeurs aleatoires aux coordonnes de position d'un bateau et à sa direction
    while not peut_placer(grille,bateau,(c1,c2),d):
        c1=r.randint(0,lim)
        c2=r.randint(0,lim)
        d=r.randint(1,2)
    place(grille,bateau,(c1,c2),d)

def eq(grilleA,grilleB):
    if grilleA.shape!=grilleB.shape and grilleA.any()==grilleB().any(): 
        #On teste l'egalite des tailles des grilles, puis l'egalite de chaque element de la grille
        return True
    return False

def genere_grille():
    grille=np.zeros((10,10))
    for i in range(1,6):
        bato=Bateau(i)
        place_ale(grille,bato)
    return grille        


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
            iDirec=?
            direc=pos_heuri[iDirec]
            if 0<=posRacine[0]+direc[0]<=9 and posRacine[1]+direc[1]<=9:
                self.coup=(posRacine[0]+direc[0],posRacine[1]+direc[1])
            if coup pas bon:
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
    

    
histoJouerAleat()
