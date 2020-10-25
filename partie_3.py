import numpy as np
import random as r 
import matplotlib.pyplot as plt
from partie_1 import genere_grille,Bateau,peut_placer,place


################
#   PARTIE 3   #
################



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
        self.coup=(-1,-1)
        self.coups=[]
        self.nbCoups=0
        self.joues=[0 for _ in range(100)] #Si joues[i] = 0 , alors le coup coups[i] n'a pas été joué
        self.pos_heuri=[(0,1),(0,-1),(1,0),(-1,0)] #garder cet ordre, permet de changer de sens avec i+=1
        for i in range(10): #on remplit 'coups' avec les 100 possibilites de coups
            for j in range(10):
                self.coups.append((i,j))
        #Si coups[x]=(i,j) , on a x=10*i+j
    
  
    def genere_coup_heuri(self,jeu,prec):
        for pos in self.pos_heuri:
            x,y=prec[0]+pos[0],prec[1]+pos[1]
            if 0<=x<=9 and 0<=y<=9:
                self.coup=(x,y)
                if self.joues[10*x+y]==0:
                    self.coups.remove(self.coup)
                    self.joues[10*x+y]=1
                    self.nbCoups+=1
                    if jeu.joue(self.coup):
                        return self.genere_coup_heuri(jeu,self.coup)
        return False
        

    def jouer(self,jeu):
        if jeu.victoire():
            coups=self.nbCoups
            return coups
        x=r.randint(0,len(self.coups)-1)
        self.coup=self.coups[x]
        x,y=self.coup[0],self.coup[1]
        self.coups.remove(self.coup)
        self.joues[10*x+y]=1
        self.nbCoups+=1
        if jeu.joue(self.coup):

            self.genere_coup_heuri(jeu,self.coup)

        return self.jouer(jeu)
   
            
            

        
def jouerHeuri():
    jeu=Bataille()

    joueur=JoueurHeuri()
    return joueur.jouer(jeu)


    



        
        
"""
Ces fonctions correspondent au main pour le joueur aléatoire
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



def histoJouerAleat(n=10000):
    coups=[]
    for _ in range(n):
        nb=jouerAleat()
        coups.append(nb)
    
    fig,ax = plt.subplots(1,1)
    ax.hist(coups, bins=101)
    ax.set_xticks([0,25,50,75,100])
    

    
def histoJouerHeuri(n=10000):
    """
    abscisse : nombre de coups
    ordonnee : nombre de fois ou x b de coup a ete joue pour finir la partie
    """
    coups=[]
    for _ in range(n):
        nb=jouerHeuri()
        coups.append(nb)
    
    fig,ax = plt.subplots(1,1)
    ax.hist(coups, bins=101)
    ax.set_xticks([0,25,50,75,100])








"""
Version proba simple
"""

class JoueurProba:
    def __init__(self):
        self.coup=(-1,-1)
        self.coups=[]
        for i in range(10):
            for j in range(10):
                self.coups.append((i,j))
        self.joues=[]
                
    def place_2(self,grille,bateau,position,direction):
        c1=position[0]
        c2=position[1]
        if direction==1:     
            for i in range(c2,c2+bateau.taille):
                grille[c1][i]+=1
        else:
            for i in range(c1,c1+bateau.taille):
                grille[i][c2]+=1
            
    def probaPlacements(self,bateau,grille): #On suppose que la grille est de taille 10
        """   
        Parameters
        ----------
        grille : Array numpy à deux dimensions
            La grille de jeu sur laquelle les probas de placement de 'bateau' sera calculée.
            Ne doit être spécifié que si l'on souhaite calculer la proba de placement sur une grille déjà en cours de partie
        bateau : Objet
            Bateau a placer
    
        Returns
        -------
        Array a 2 dimensions
            Grille contenant , pour chaque case, la proba qu'elle soit occupee par le bateau, pour le total des confs possibles
            
        """
        grille2=np.zeros((10,10))
        grille_placements=np.array([[grille[i][j] for i in range(10)] for j in range(10)])
        placements=0
    
        for i in range (0,10):    
            for j in range (0,10):
    
                if peut_placer(grille_placements, bateau, (i,j), 1):
                    place(grille_placements, bateau, (i,j), 1)
                    self.place_2(grille2, bateau, (i,j), 1)
                    grille_placements = np.array([[grille[i][j] for i in range(10)] for j in range(10)]) #On remet la grille a son état initial
                    placements+=bateau.taille
    
    
                if peut_placer(grille_placements, bateau, (i,j), 2):
                    place(grille_placements, bateau, (i,j), 2)
                    self.place_2(grille2, bateau, (i,j), 2)
                    placements+=bateau.taille
    
    
                grille_placements = np.array([[grille[i][j] for i in range(10)] for j in range(10)])
    
        grille2/=placements
        return grille2*100
    def genGrilleProba(self,bateau,imposs,touche=False): #imposs contient les cases ou chaque bateau peut pas etre
        coupPrec=self.coup
        if touche==False: #Le coup precendent n'a pas touché => les bateaux peuvent etre n'importe ou c'est possible
            grille=np.zeros((10,10))
            for coup in imposs:
                x,y=int(coup[0]),int(coup[1])
                grille[x][y]=1
        else: #Le coup prec a touché, on cherche seulement a proximite
            grille=np.ones((10,10))
            taille=bateau.taille
            x,y=coupPrec[0],coupPrec[1]
            for i in range(1,taille+1):
                #Que les cases autour d'un rayon inferieur a la taille du bateau peuvent etre bonnes
                if 0<=x+i<=9:
                    grille[x+i][y]=0
                if 0<=x-i<=9:
                    grille[x-i][y]=0
                if 0<=y+i<=9:
                    grille[x][y+i]=0
                if 0<=y-i<=9:
                    grille[x][y-i]=0
        #ici, on a une grille prete pour le calcul de proba
        test=self.probaPlacements(bateau,grille)
                
                    
                    
                
                
                
                
            
 
        