import random as r
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice 
from partie_1 import Bateau,peut_placer,place,place_ale,eq,genere_grille,affiche
from partie_2 import nbconfigs_bateau,liste_configs_bateau,nbConfigs,nb_generations,genere_grille_liste,approximer
from partie_3 import Bataille,JoueurAleat,JoueurHeuri,jouerAleat,histoJouerAleat,histoJouerHeuri,JoueurProba
from time import perf_counter as clock

def Sondeur(p_priori, p_reelle, ps):
    trouve = False
    case_sondee = [0,0]
    c = 0 #Nombre de sondes effectuées avant de détecter le sous-marin
    liste_pos = []                  #Liste des cases de la grille, indexée par leur ordre (G à D puis H à B)
    for i in range (p_reelle.shape[0]):
        for j in range (p_reelle.shape[1]):
            liste_pos.append(i*(p_reelle.shape[1]) + j+1)
            
    liste_p_reelle = []             #Liste des probas de chaque case de contenir l'objet
    for i in range (0,p_reelle.shape[0]):
        for j in range (0,p_reelle.shape[1]):
            liste_p_reelle.append(p_reelle[i][j])
    
    rang_obj = choice(liste_pos, 1, liste_p_reelle) #Index de la case contenant le sous-marin
    pos_obj =(rang_obj-1)//p_reelle.shape[1],(rang_obj%p_reelle.shape[1]-1)%p_reelle.shape[1] #Coordonnées de la case
        
    while trouve == False :   #Tant que l'on a pas trouvé l'objet   
    
        for i in range(p_priori.shape[0]):          #On stocke la case ayant la proba la plus haute
            for j in range(p_priori.shape[1]):
                if p_priori[i][j] > p_priori[case_sondee[0]][case_sondee[1]]:
                    case_sondee[0]=i
                    case_sondee[1]=j
        pik = p_priori[case_sondee[0]][case_sondee[1]] #Valeur de la proba de la case
        c+=1                                         #On sonde la case 
        if (case_sondee[0]==pos_obj[0]) and (case_sondee[1]==pos_obj[1]): #Cas où la case contient l'objet
            if r.random() <= ps:    #Si detection, on retourne le nombre de sondes
                trouve = True
            else:                   #Sinon, mise a jour des probas
            
                nvproba = (pik - pik*ps)/(1 - pik*ps)   #Nouvelle proba de la case sondee
                delta = pik - nvproba                   #Diff entre l'ancienne et la nouvelle proba
                for i in range(p_priori.shape[0]):      #MAJ de toutes les probas sauf celle de la case
                    for j in range(p_priori.shape[1]):
                        p_priori[i][j] = p_priori[i][j]/(1-delta)
                p_priori[case_sondee[0]][case_sondee[1]] = nvproba #MAJ de la proba de la case sondee
        else: #Cas où la case ne contient pas l'objet
        
            nvproba = (pik - pik*ps)/(1 - pik*ps)   
            delta = pik - nvproba                   
            for i in range(p_priori.shape[0]):     
                for j in range(p_priori.shape[1]):
                    p_priori[i][j] = p_priori[i][j]/(1-delta)
            p_priori[case_sondee[0]][case_sondee[1]] = nvproba 
    return c

priori = np.array([[.01 for i in range (10)] for j in range (10)])
reel = np.array([[.01 for i in range (10)] for j in range (10)])
ps = 0.5
s = 0
for i in range(1,501):
    s+= Sondeur(priori, reel, ps)
print(s/500)
