import numpy as np

A = []
b = []
ei = [
    [1 , 0 , 0],
    [0 , 1 , 0],
    [0 , 0 , 1]
]
tab = [
    ['VB' , 'x' , 'y' , 'e1' , 'e2' , 'e3' , 'b' , 'q'],
    ['e1'],
    ['e2'],
    ['e3'],
    ['-Z']
]

def collector():
    global A
    global b
    global tab
    print("\n Quelle est l'expression de la fonction-objectif ? (Renseignez juste les coefficients de x et y) :  \n")
    co_x = int(input("* Coefficient de x : "))
    co_y = int(input("* Coefficient de y : "))
    tab[4].append(co_x)
    tab[4].append(co_y)
    for i in range(4):
        tab[4].append(0)
    print("\n !! NB !! \n Nous supposons que votre PL est composé de 3 contraintes .\n")
    print("\n Commençons par le remplissage de la matrice des contraintes (Matrice A). Renseignez les valeurs une à une par ligne .\n")
    for i in range(3):
        A_temp = []
        print(f"\n - Ligne {i + 1} : ")
        for j in range(2):
            v = int(input(f"\t Valeur {j + 1} : "))
            A_temp.append(v)
        A.append(A_temp)
    print("\n Passons à la matrice b . Renseignez les valeurs pour chaque contrainte .\n")
    for i in range(3):
        print(f"\n - Ligne {i + 1} : ")
        v = int(input(f"\t Valeur : "))
        b.append(v)
    print("\n\t\t\t\t ::: Matrice A ::: \n")
    for i in A:
        print("\n")
        for j in i:
            print(f"\t\t\t\t{j}", end='\t')
    print("\n")
    print("\n\t\t\t\t ::: Matrice b ::: \n")
    for i in b:
        print("\n")
        print(f"\t\t\t\t\t\t{i}")
    print("\n")
    print("\n\t\t\t\t ::: Matrice des variables d'écart ::: \n")
    for i in ei:
        print("\n")
        for j in i:
            print(f"\t\t\t\t{j}", end='\t')
    print("\n")
    print(f"\n ::: Fonction-objectif ::: \n\n F = ({co_x})x + ({co_y})y")
    print("\n Bien ! \n\n Maintenant , place aux résultats de l'algorithme : \n\n")
    create_tab()

def create_tab():
    global tab
    for i in A[0]:
        tab[1].append(i)
    for j in ei[0]:
        tab[1].append(j)
    tab[1].append(b[0])

    for i in A[1]:
        tab[2].append(i)
    for j in ei[1]:
        tab[2].append(j)
    tab[2].append(b[1])

    for i in A[2]:
        tab[3].append(i)
    for j in ei[2]:
        tab[3].append(j)
    tab[3].append(b[2])

    for i in range(1 , 5):
        tab[i].append('-')

def show_tab():
    global tab
    global simp
    print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ::: Tableau de simplexe no {simp} ::: \n")
    for i in tab:
        print("\n")
        for j in i:
            print(f"\t\t\t\t{j}", end='\t')
    print("\n")

def quotient():
    global tab_arr
    global tab
    indic_row = np.argmax(tab_arr[4 , 1 : 7]) + 1
    col_piv = tab_arr[1 : 4 , indic_row].tolist()
    b_list = tab_arr[1 : 4 , 6].tolist()
    q_list = []
    for i in range(len(b_list)):
        if col_piv[i] != 0:
            q = b_list[i] / col_piv[i]
            q = np.round(q , 1)
            q_list.append(q)
        else:
            q_list.append('-')
    q_arr = np.array(q_list)
    tab_arr[1 : 4 , 7] = q_arr
    tab = tab_arr.tolist()

def find_pivot():
    indic_row = np.argmax(tab_arr[4 , 1 : 7]) + 1
    indic_column = np.argmin(tab_arr[1 : 4 , 7]) + 1
    pivot = tab_arr[indic_column , indic_row]
    return pivot

def reducing():
    global tab_arr
    global tab
    indic_line = np.argmax(tab_arr[4 , 1 : 7]) + 1
    indic_col = np.argmin(tab_arr[1: 4, 7]) + 1
    pivot = find_pivot()
    tab_arr[indic_col , 1 : 7] /= pivot
    tab_arr[indic_col , 0] = tab_arr[0 , indic_line]
    tab = tab_arr.tolist()

def simplexe():
    global tab_arr
    global tab
    pivot_col = np.argmax(tab_arr[4, 1: 7]) + 1
    pivot_line = np.argmin(tab_arr[1: 4, 7]) + 1
    for i in range(1 , pivot_line):
        tab_arr[i , 1 : 7] = tab_arr[i , 1 : 7] - (tab_arr[i , pivot_col] * tab_arr[pivot_line , 1 : 7])
    for i in range(pivot_line + 1 , 5):
        tab_arr[i , 1 : 7] = tab_arr[i , 1 : 7] - (tab_arr[i , pivot_col] * tab_arr[pivot_line , 1 : 7])
    tab = tab_arr.tolist()

print("\n Bonjour , et bienvenue dans mon programme simulant la méthode de simplexe à 2 variables (x et y) de la Recherche Opérationnelle . \n")
collector()
tab_arr = np.array(tab , dtype = object)
simp = 1

def rounding():
    global tab_arr
    global tab
    for i in range(1 , 5):
        for j in range(1 , 7):
            tab_arr[i , j] = np.round(tab_arr[i , j] , 1)
    tab = tab_arr.tolist()

def algorithme():
    global simp
    global tab_arr
    global tab
    while not np.all(tab_arr[4 , 1 : 7] <= 0):
        quotient()
        rounding()
        show_tab()
        print(f"\n * Pivot = {find_pivot()} \n")
        reducing()
        simplexe()
        simp += 1
    print("\n")
    print("\n::: Solution optimale trouvée !! ::: \n")
    print("\n")
    q_list = ['-' , '-' , '-' , '-']
    q_arr = np.array(q_list)
    tab_arr[1 : 5 , 7] = q_arr
    tab = tab_arr.tolist()
    print(f"\n Voilà le dernier tableau de simplexe :\n")
    rounding()
    show_tab()
    print(f"\n \n \t \t \t →  La solution optimale est : Z_max = {-1 * tab_arr[4 , 6]} \n \n")


algorithme()