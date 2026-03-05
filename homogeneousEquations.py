from math import sqrt

def solver(a , b , delta) :
    if delta == 0:
        s = (-b)/(2 * a)
        if s != 0 and s != 1:
            return f"(Ax + B)e({s}x)"
        if s == 0:
            return "Ax + B"
        if s == 1:
            return "(Ax + B)e(x)"
    if delta > 0:
        s1 = (-b - sqrt(delta))/(2 * a)
        s2 = (-b + sqrt(delta))/(2 * a)
        if s1 != 0 and s2 != 0 and s1 != 1 and s2 != 1:
            return f"Ae({s1}x) + Be({s2}x)"
        if s1 == 0 and s2 == 0:
            return "A + B"
        if s1 == 1 and s2 == 1:
            return "Ae(x) + Be(x)"
        if s1 == 0 and s2 == 1:
            return "A + Be(x)"
        if s1 == 1 and s2 == 0:
            return "Ae(x) + B"
        if s1 != 0 and s1 != 1 and s2 == 0:
            return f"Ae({s1}x) + B"
        if s1 != 0 and s1 != 1 and s2 == 1:
            return f"Ae({s1}x) + Be(x)"
        if s1 == 0 and s2 != 0 and s2 != 1:
            return f"A + Be({s2}x)"
        if s1 == 1 and s2 != 0 and s2 != 1:
            return f"Ae(x) + Be({s2}x)"
    if delta < 0:
        delta = -delta
        re = (-b)/(2 * a)
        im = (sqrt(delta))/(2 * a)
        if re != 0 and re != 1:
            return f"(Acos({im}x) + Bsin({im}x))e({re}x)"
        if re == 0:
            return f"Acos({im}x) + Bsin({im}x)"
        if re == 1:
            return f"(Acos({im}x) + Bsin({im}x))e(x)"

def process():
    print("\n L'equation differentielle que vous souhaitez resoudre est certainement de la forme : ay'' + by' + cy = 0 . ")
    print()
    print()
    print("Entrez les valeurs des coefficients : \n")
    a = float(input("\n * a = ? : "))
    print()
    b = float(input("\n * b = ? : "))
    print()
    c = float(input("\n * c = ? : "))
    print()
    while a == 0:
        print()
        print("Entrez une valeur non nulle de a !")
        print()
        print()
        print("Entrez les valeurs des coefficients : \n")
        a = float(input("\n * a = ? : "))
        print()
        b = float(input("\n * b = ? : "))
        print()
        c = float(input("\n * c = ? : "))
        print()
    delta_in = (b * b) - (4 * a * c)
    print(":::::ANALYSE DES DONNEES:::::")
    print()
    print()
    print("Les solutions de cette equation differentielle sont les fonctions y definies sur R par :")
    print()
    solve = solver(a , b , delta_in)
    print(f"\t y(x) =  {solve}")
    print()
    print("\t\t Avec A et B des constantes relles .")
    print()


process()