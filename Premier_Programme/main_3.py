
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom ? ")
    return nom


def demander_age(nom_personne):
    age = 0
    while age == 0:
        age_str = input(nom_personne + ", Quel est votre age ? ")
        try:
            age = int(age_str)
        except:
            print("ERREUR: Vous devez entrez un chiffre.")
        return age


nom_utlisateur = demander_nom()
nom_utlisateur2 = demander_nom()

age_demander = demander_age(nom_utlisateur)
age_demander2 = demander_age(nom_utlisateur2)


print("Vous vous appelz " + nom_utlisateur + ", votre age est " + str(age_demander) + ".")
print("L'annee prochain vous aurez " + str(age_demander+1) + " ans")
