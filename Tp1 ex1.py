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