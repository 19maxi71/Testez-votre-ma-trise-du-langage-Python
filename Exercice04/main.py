class MyClass:
    
    def __init__(self, full_name):
        self.full_name = full_name
    
    def display_name(self):
        print("Le nom complet est :", self.full_name)

class OtherClass:
    def __init__(self, first_name, name):
        self.first_name = first_name
        self.name = name
    
    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.name}")

# # Instructions - Exercice 4

# Vous avez reçu un fichier Python contenant plusieurs classes et fonctions, mais il ne suit pas les règles de style PEP 8. Votre tâche consiste à examiner le code et à corriger toutes les violations des règles PEP 8.

# Si vous voulez, vous pouvez vérifier votre code avant de le soumettre grâce à l’onglet “Tests”, dans le menu “Tools” en bas à gauche de votre écran.