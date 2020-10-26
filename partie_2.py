import numpy as np
from partie_1 import genere_grille,peut_placer,place,Bateau,eq,place_ale #Plus joli sinon plein de warnings

################
#   PARTIE 2   #
################


""" QUESTION 2 """

def nbconfigs_bateau(bateau): 
    lgrille = []
    grille = np.zeros((10,10)) #On suppose que la grille est de taille 10
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

def nbConfigs(liste):
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

def nb_generations(grille):
    grille_aleat = genere_grille()
    cpt = 1
    while not (eq(grille, grille_aleat)): #La fonction 'eq' teste l'égalité entre deux grilles
        cpt += 1
        grille_aleat = genere_grille()
    return cpt


""" QUESTION 5 """

def genere_grille_liste(liste): #Genere une grille aleatoire contenant les bateaux d'une liste donnee
    grille=np.zeros((10,10))
    for i in range(0,len(liste)):
        place_ale(grille,liste[i])
    return grille  

def approximer(liste,n=100):
    grille = genere_grille_liste(liste)
    res = 0
    for _ in range(n):
        rand = genere_grille_liste(liste)
        s = 1        
        while not (eq(grille, rand)):
            rand = genere_grille_liste(liste)
            s += 1            
        res += s
    return res/100



