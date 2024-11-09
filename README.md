# Python
Exercice 2:
Given the grades obtained by a student in 5 subjects and their respective coefficients, write an algorithm that calculates the average grade of the student.
Exercice 2 :
Connaissant les notes obtenues par un élève dans 5 matières et leurs coefficients respectifs, écrire un algorithme qui permet de calculer la moyenne de l'élève.

Somme = 0 

for i in range(5):
 while True:
        N = float(input("Entrez la note : "))
        C = float(input("Entrez le coefficient : "))
        if 0 <= N <= 20 and 0 <= C <= 4:
            break
        print("Erreur : La note doit être entre 0 et 20, et le coefficient entre 0 et 4.")
  
 Somme += N*C

Moyen = Somme/2
print("Moyen est :",Moyen)
