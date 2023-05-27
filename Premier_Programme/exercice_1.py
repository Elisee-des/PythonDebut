
nom = ""
while nom == "":
    nom = input("Quel est ton nom ? ")


age = 0
while age == 0:
    age_str = input("Quel est votre age ? ")
    try:
        age = int(age_str)
    except:
        print("ERREUR: Vous devez entrez un chiffre.")

print("Vous vous appelz " + nom + ", votre age est " + str(age) + ".")
print("L'annee prochain vous aurez " + str(age+1) + " ans")
