# Fonction decoupeChaine qui prend en paramètre 
# une string et renvoie la même string 
# dans laquelle les caractères successifs 
# non identiques sont séparés par un espace.

# Fonction pour envoyer chaque caractère d'une string dans un array en l'absence de séparateurs

def decoupeChaine(chaine):
    chaineSeparee = chaine[0]
    for i in range(1, len(chaine)):
        if chaine[i] != chaine[i-1]:
            chaineSeparee += " " + chaine[i]
        else:
            chaineSeparee += chaine[i]
    return chaineSeparee

print(decoupeChaine("aaabbcca"))

def decritChaine(chaine):
    # Compte les caractères identiques consécutifs
    nbIdentique = 0
    chaineSeparee = chaine[0]
    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i-1]:
            nbIdentique += 1
        else:
            chaineSeparee += str(nbIdentique) + chaine[i]
            nbIdentique = 0
    return chaineSeparee

print(decritChaine("aaabbcca"))