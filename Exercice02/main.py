# Considérons un dictionnaire qui contient des informations sur des étudiants et leurs notes dans différentes matières.

# Écrivez un programme Python qui effectue les actions suivantes :
# - Demander à l'utilisateur de saisir le nom d'un étudiant avec le message suivant : “Entrez le nom de l’étudiant :  ”
# - Afficher les notes de cet étudiant dans chaque matière “<nom de la matière> : <note>”, précédées par le message “Notes de <nom de l’étudiant> :  ”. Si l’étudiant n’existe pas, afficher exactement le message suivant : "L'étudiant <nom de l’étudiant> n'existe pas dans la liste."
# - Calculer la moyenne des notes de cet étudiant et l'afficher comme suit : “Moyenne de <nom de l’étudiant> : <moyenne>”

students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

def main():
    student_name = input("Entrez le nom de l’étudiant : ")
    if student_name in students:
        print(f"Notes de {student_name} : ")
        for subject, grade in students[student_name].items():
            print(f"{subject} : {grade}")
        average = sum(students[student_name].values()) / len(students[student_name])
        print(f"Moyenne de {student_name} : {average}")
    else:
        print(f"L'étudiant {student_name} n'existe pas dans la liste.")

start= main()