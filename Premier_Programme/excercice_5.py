
def afficher_information_personne(nom_utlisateur, age_utilisateur):
    print("Vous vous appelz " + nom_utlisateur + ", votre age est " + str(age_utilisateur) + ".")
    print("L'annee prochain vous aurez " + str(age_utilisateur+1) + " ans")
    
    if age_utilisateur == 17:
        print("Vous etes presque majeur.")
    elif age_utilisateur == 0:
        print("Tout juste majeur.")
    elif age_utilisateur > 60:
        print("Vous etes major.")
    elif age_utilisateur >= 18:
        print("Vous etes majeur.")
    elif age_utilisateur < 10:
        print("Vous etes enfants.")
    else:
        print("Vous etes mineur.")


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

age_utilsateur = demander_age(nom_utlisateur)
age_utilsateur2 = demander_age(nom_utlisateur2)


afficher_information_personne(nom_utlisateur, age_utilsateur)
afficher_information_personne(nom_utlisateur2, age_utilsateur2)


