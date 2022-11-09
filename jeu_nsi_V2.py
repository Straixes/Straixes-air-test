from random import *
import csv

score_j1 = 0
score_j2 = 0
def verfication(mot):
    global lettretire
    fichier=open("mots_francais.txt",'r',encoding='utf-8')
    mots=tuple(x[0] for x in csv.reader(fichier))
    fichier.close()
    lettreverifier=True
    for i in range(len(mot)):
        if not mot[i] in lettretire:
            lettreverifier=False
    if mot in mots and lettreverifier == True:
        return True
    else:
        return False
    
def jouer():
    global score_j1
    global score_j2
    #tirage
    global lettretire
    lettre=[chr(a)for a in range(97,123)]
    caracteres_speciaux=('é','è','ç','ê','û','î','ï')
    for a in range(len(caracteres_speciaux)):
        lettre.append(caracteres_speciaux[a])
    lettretire=[]
    
    for i in range(randint(7,10)):
        numero=randint(0,len(lettre)-1)
        while lettre[numero] in lettretire:
            numero=randint(0,25)
        lettretire.append(lettre[numero])
    print("les lettres tirées sont:",lettretire)

    #retirage
    
    retirage = str(input("Voulez vous retirer de nouvelles lettres ou voulez vous les garder ? r/g"))
    while retirage != 'r' and retirage != 'g':
        retirage = str(input("Voulez vous retirer de nouvelles lettres ou voulez vous les garder ? r/g, votre lettre précédente ne correspondait pas"))
    if retirage == 'r':
        jouer()
    
    #demande mot + verif
    
    mot_j1 = str(input("Quel est ton mot J1"))
    while verfication(mot_j1) == False:
        mot_j1 = str(input("mot invalide redonne un mot"))
    mot_j2 = str(input("Quel est ton mot J2"))
    while verfication(mot_j2) == False:
        mot_j2 = str(input("mot invalide redonne un mot"))
    nb_lettre_j1 = len(mot_j1)
    nb_lettre_j2 = len(mot_j2)
    
    #longueur mot verif
    
    if nb_lettre_j1 > nb_lettre_j2:
        score_j1 += 1
        print("j1 gagne")
    elif nb_lettre_j1 < nb_lettre_j2:
        score_j2 += 1
        print("j2 gagne")
    elif nb_lettre_j1 == nb_lettre_j2:
        print("egalité")

    #rejouer
        
    print("le score du j1 est", score_j1, "le score du j2 est", score_j2)
    rejouer = str(input("Voulez vous rejouer ? o/n"))
    while rejouer != 'o' and rejouer != 'n':
        rejouer = str(input("Voulez vous rejouer ? o/n, votre lettre précédente ne correspondait pas"))
    if rejouer == 'o':
        jouer()
    elif rejouer == 'n':
        print("fin de partie")
jouer()

    

    
