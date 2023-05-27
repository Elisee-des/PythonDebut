
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom ? ")
    return nom

def demander_age():
    age = 0
    while age == 0:
        age_str = input("Quel est votre age ? ")
        try:
            age = int(age_str)
        except:
            print("ERREUR: Vous devez entrez un chiffre.")
        return age

nom_utlisateur = demander_nom()

age_demander = demander_age()


print("Vous vous appelz " + nom_utlisateur + ", votre age est " + str(age_demander) + ".")
print("L'annee prochain vous aurez " + str(age_demander+1) + " ans")
