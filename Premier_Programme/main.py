
nom = input("Quel est ton nom ? ")
age = input("Quel est votre age ? ")
try:
    age_prochain = int(age) + 1
except:
    print("ERREUR: Vous devez entrez un chiffre.")
else:
    print("Vous vous appelz " + nom + ", votre age est " + str(age) + ".")
    print("L'annee prochain vous aurez " + age_prochain + "ans")
