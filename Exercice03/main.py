words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

# Considérez une liste de mots. Vous devez créer une liste de compréhension qui contient des tuples de chaque mot et le nombre de voyelles qu'il contient. À la fin de votre programme, affichez cette nouvelle liste créée à partir de la liste de compréhension.
 
# Par exemple avec la liste suivante : ["openclassrooms", "developpeur", "algorithme"]
# vous devrez avoir comme résultat, cette liste : [('openclassrooms', 5), ('developpeur', 5), ('algorithme', 4)]
def main():
    vowels = "aeiouAEIOUyY"
    for word in words:
        result = (word, len([letter for letter in word if letter in vowels]))
        print(result)

start = main()