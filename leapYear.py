def est_bissextile(n) :
    if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0) :
        return True
    return False

n_ = int(input("\n Entrez la valeur d'une année : \n *Année : "))
while n_ <= 0 :
    n_ = int(input("\n Entrée invalide ! \n Entrez une valeur positive et non nulle pour l'année . \n *Année : "))
if est_bissextile(n_) :
    print("\n Cette année est bissextile .")
else :
    print("\n Cette année n'est pas bissextile .")