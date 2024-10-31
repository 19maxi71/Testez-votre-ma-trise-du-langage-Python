name = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))


# Vous devez créer un programme Python qui affiche un message personnalisé en utilisant la méthode f-string. Le programme devra demander à l'utilisateur de saisir son nom et son âge, puis il affichera un message de salutation avec ces informations.
 
# Le message final devra avoir exactement la forme suivante : "Bonjour, je m'appelle `<`nom`>` et j'ai `<`age`>` ans."

def main():
    print(f"Bonjour, je m'appelle {name} et j'ai {age} ans.")

start= main()