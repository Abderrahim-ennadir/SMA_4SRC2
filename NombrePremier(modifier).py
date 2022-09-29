
#afficher les nombres premiers
min = int(input("Entrez le min : ")) #on choisis le chiffre min de notre intervale
max = int(input("Entrez le max : ")) #on choisis le chiffre max de notre intervale
for n in range(min,max + 1): #Pour un chiffre allant de notre variable min à max
   if n > 1: 
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
