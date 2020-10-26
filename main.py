import random as r
import numpy as np
import matplotlib.pyplot as plt
from partie_1 import Bateau,peut_placer,place,place_ale,eq,genere_grille,affiche
from partie_2 import nbconfigs_bateau,liste_configs_bateau,nbConfigs,genere_grille_liste,approximer,nb_generations
from partie_3 import Bataille,JoueurAleat,JoueurHeuri,JoueurProba
from time import perf_counter as clock









################
#   PARTIE 2   #
################
    
"Question 2"
# sousMarin=Bateau(3)
# print(nbconfigs_bateau(sousMarin))

"Question 3"
# bat1,bat2,bat3=Bateau(5),Bateau(4),Bateau(3)
# liste=[bat1]
# print("Nombre de configs pour 1 bateau: ",nbConfigs(liste))
# liste=[bat1,bat2]
# print("Nombre de configs pour 2 bateaux: ",nbConfigs(liste))
# liste=[bat1,bat2,bat3]
# print("Nombre de configs pour 3 bateaux: ",nbConfigs(liste))



# def tpsExec(liste):
#     #Regarde cb de temps (en s) met la fonction f a s'executer
#     t1=clock()
#     nbConfigs(liste)
#     t2=clock()
#     return t2-t1
# temps=[]
# x=[1,2,3] 

# liste=[bat1]
# t=tpsExec(liste)
# temps.append(t)

# liste=[bat1,bat2]
# t=tpsExec(liste)
# temps.append(t)

# liste=[bat1,bat2,bat3]
# t=tpsExec(liste)
# temps.append(t)

# plt.plot(x,temps)
# plt.title("Temps d'exéc de nbConfigs en fn du nb de bateaux")
# plt.xlabel("Nb bateaux ")
# plt.ylabel("Temps d'execution (s)")
# plt.xticks([0,1,2,3])
# plt.show()
# plt.close()

"Question 5"

# bat1,bat2,bat3=Bateau(5),Bateau(4),Bateau(3)
# liste=[bat1]
# print("Nombre approximatif de configs pour 1 bateau: ",approximer(liste))
# liste=[bat1,bat2]
# print("Nombre approximatif de configs pour 2 bateaux: ",approximer(liste))
# liste=[bat1,bat2,bat3]
# print("Nombre approximatif de configs pour 3 bateaux: ",approximer(liste))
# def tpsExec(liste):
#     #Regarde cb de temps (en s) met la fonction f a s'executer
#     t1=clock()
#     approximer(liste)
#     t2=clock()
#     return t2-t1









################
#   PARTIE 3   #
################

"Version Aléatoire"

# def jouerAleat():
#     jeu=Bataille()
#     joueur=JoueurAleat()
#     return joueur.jouer(jeu)




# def histoJouerAleat(n=10000):
#     coups=[]
#     for _ in range(n):
#         nb=jouerAleat()
#         coups.append(nb)
    
#     fig,ax = plt.subplots(1,1)
#     ax.set_title("Nombre de fois où la bataille est gagnee en x coups aléatoires en fonction de x, pour n="+str(n)+" parties")
#     ax.hist(coups, bins=101)
#     ax.set_xticks([0,25,50,75,100])
    
# histoJouerAleat()

"Version heuristique"

def jouerHeuri():
    jeu=Bataille()
    joueur=JoueurHeuri()
    return joueur.jouer(jeu)

    
def histoJouerHeuri(n=10000):
    """
    abscisse : nombre de coups
    ordonnee : nombre de fois ou x nb de coups a ete joue pour finir la partie
    """
    coups=[]
    for _ in range(n):
        nb=jouerHeuri()
        coups.append(nb)
    
    fig,ax = plt.subplots(1,1)
    ax.set_title("Nombre de fois où la bataille est gagnee en x coups heuristiques en fonction de x, pour n="+str(n)+" parties")
    ax.hist(coups, bins=101)
    ax.set_xticks([0,25,50,75,100])
    
histoJouerHeuri()

"Version probabiliste simplifiée"