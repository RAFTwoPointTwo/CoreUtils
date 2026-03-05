def fact(num) :
    if num <= 1 :
        return 1
    return num * fact(num - 1)

def arrangement(p_, n_) :
    return fact(n_) // fact(n_ - p_)

n = int(input("\n Bienvenue dans le programme de détermination d'un arrangement de p éléments parmi n autres . \n Entrez la valeur de n : \n *n = ? :"))
p = int(input("\n Entrez la valeur de p : \n *p = ? :"))
while n <= 0 or p < 0 or n < p :
    print("\n Entrée(s) invalide(s) ! \n Entrez des valeurs positives pour les nombres . \n ( Avec n non nul , n supérieur ou égal à p )  .\n")
    n = int(input("*n = ? :"))
    p = int(input("*p = ? :"))
arr = arrangement(p, n)
print("\n")
print(f"L'arrangement de {p} éléments parmi {n} éléments est : A{n},{p} = {arr}")