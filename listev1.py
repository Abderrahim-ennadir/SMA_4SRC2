# Script permettant d'encoder des valeurs dans une liste
# jusqu'à ce que l'utilisateur ne rentre plus de valeurs (ENTER)

#initialisation de la liste
liste = []
valeur = "start"

#boucle principale
while (valeur != ""): 
    print("Veuillez entrer une valeur :", end = " ") #tant que valeur n'est pas nul
    valeur = input() #incrément de la variable avec la valeur entrée
    liste.append(valeur) #incrément de la liste avec le contenu de la variable

#affichage de la liste
print(liste)
