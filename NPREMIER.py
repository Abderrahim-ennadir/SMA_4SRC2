Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
var i,j,nbdiviseur  <-0 : entiers;
Debut
               pour i de 1 à 100000 pas de 1 faire
        pour j de 1 à i pas de 1 faire
                si (i mod j = 0) alors
                  nbdiviseur<- nbdiviseur+1;

               fin si 
fin pour 
          fin pour
si (nbdiviseur<=2) alors
afficher ("les nombres premiers sont :",i);
finsi
fin