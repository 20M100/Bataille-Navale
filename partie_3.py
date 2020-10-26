# -*- coding: utf-8 -*-
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
        self.coule=0
        
    def reset(self):
        self.grille=np.zeros((10,10))
        
    def joue(self,position):
        self.coule=0 #Si la fonction est appelee, alors on est au coup suivant, on reinitialise coule
        x,y=position[0],position[1]
        
        if self.grille[x][y]!=0.0:
            idBat=self.grille[x][y]
            self.grille[x][y]=9.0
            coule=True
            if x+1<=9:
                if self.grille[x+1][y]==idBat:
                    coule=False
            if x-1>=0:
                if self.grille[x-1][y]==idBat:
                    coule=False
            if y+1<=9:
                if self.grille[x][y+1]==idBat:
                    coule=False
            if y-1>=0:
                if self.grille[x][y-1]==idBat:
                    coule=False
            #Si aucun de ces tests n'est verifie, alors la case touchee est la derniere contenant l'id de ce bateau : il est coulé
            if coule:
                self.coule=idBat
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
        self.nbCoups=0
        for i in range(10): #Ces boucles imbriquées permettent de remplir le tableau 'coups' avec tous les coups jouables
            for j in range(10):
                self.coups.append((i,j))


    def genere_coup(self):

        if len(self.coups)>0:
            x=r.randint(0,len(self.coups)-1)
            self.coup=self.coups[x]
            self.coups.remove(self.coup)
            
    def jouer(self,jeu):
        while not jeu.victoire():
            self.genere_coup()
            jeu.joue(self.coup)
            self.nbCoups+=1
        coups=self.nbCoups
        return coups
        
        
            

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
        
    
  
    def genere_coup_heuri(self,jeu,prec):
        for pos in self.pos_heuri:
            x,y=prec[0]+pos[0],prec[1]+pos[1]
            if 0<=x<=9 and 0<=y<=9:
                self.coup=(x,y)
                if self.joues[10*x+y]==0: #Si coups[x]=(i,j) , on a x=10*i+j
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
   
            

class JoueurProba:
    def __init__(self):
        self.coup=(-1,-1)
        self.coups=[]
        for i in range(10):
            for j in range(10):
                self.coups.append((i,j))
        self.joues=[]
        self.bateauxGrille=[1,2,3,4,5] #Contient les identifiants des bateaux initialement sur la grille
                
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
                    self.place_2(grille2, bateau, (i,j), 1)            
                    placements+=1
                if peut_placer(grille_placements, bateau, (i,j), 2):
                    self.place_2(grille2, bateau, (i,j), 2)
                    placements+=1
    
        grille2/=placements*bateau.taille
        return grille2*100 #Retourne proba en pourcentages
    
    def grilleProba(self): #grille des probas qu'un bateau soit sur telle case qd elle est appelee
        placements=np.zeros((10,10))
        if len(self.joues)>0:
            print(self.joues[-1])
        else:
            print("[]")
        for el in self.joues:
            x,y=el[0],el[1]
            placements[x][y]=1

        print(placements)
        #placements[i][j] = 0 si la case (i,j) est jouable (=vide), 1 sinon
        grille=np.zeros((10,10))
        for idBat in self.bateauxGrille:
            bat=Bateau(idBat)
            grille=grille+self.probaPlacements(bat,placements)
        for el in grille:
            for y in el:
                print(round(y,1),end="  ")
            print()
        for _ in range(5):
            print()
        return grille/len(self.bateauxGrille)
            
    def probaMax(self,grille): #grille a 2 dimensions
        maxi=grille[0][0]
        idMaxi=(0,0)
        for i in range(len(grille)):

            for j in range(len(grille[i])):
                if grille[i][j]>maxi:        
                    maxi=grille[i][j]
                    idMaxi=(i,j)

        return idMaxi
        
        
    def jouer(self,jeu):
        cpt=0
        while not jeu.victoire():
            probas=self.grilleProba()
            idMaxi=self.probaMax(probas)
#            if cpt==4:
#                print("CPT ",cpt)
#                probas[1][2]=8.8
#                for x in probas:
#                    for y in x:
#                        print(round(y,1),end="  ")
#                    print()
#                print(idMaxi)
#
#            if cpt==5:
#                print("CPT ",cpt)
#                probas[1][2]=8.8
#                for x in probas:
#                    for y in x:
#                        print(round(y,1),end="  ")
#                    print()
#                print(idMaxi)
            self.coup=idMaxi
            self.coups.remove(self.coup)
            self.joues.append(self.coup)
            jeu.joue(self.coup)

            if jeu.coule!=0:
                self.bateauxGrille.remove(jeu.coule)
            cpt+=1
            
        return cpt
        
            

                
                    
                    
jeu=Bataille()
joueur=JoueurProba()
t=joueur.jouer(jeu)
print(t)


 
        
