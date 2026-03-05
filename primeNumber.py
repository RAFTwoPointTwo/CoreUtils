def premier(num) :
    if num >= 2 :
        div = 0
        for i in range(2, n) :
            if num % i == 0 :
                div += 1
        if div == 0 :
            return 1
        else :
            return 0
    else :
        return 0

n = int(input("\n Entrez un entier positif pour vérifier s'il est premier : \n * n = ? : "))
while n < 0 :
    n = int(input("\n Entrée invalide ! \n Entrez un entier positif : \n *n = ? : "))
if premier(n) :
    print(f"\n Le nombre {n} est premier .")
else :
    print(f"\n Le nombre {n} n'est pas premier .")