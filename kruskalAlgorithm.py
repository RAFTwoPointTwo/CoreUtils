P = 0
T = set()
aretes_ = []
Sommets = set()
edge_list = []
weight_list = []
n = 0
E = []

def edge_collector(degres):
    print("\n")
    global edge_list
    global weight_list
    edge_number = (degres) // 2
    for i in range(1 , edge_number +1):
        print(f"\n * Entrez les sommets de l'arête {i} :")
        s1 = int(input("\t Sommet 1 :"))
        s2 = int(input("\t Sommet 2 :"))
        while s1 < 0 or s2 < 0:
            print("\nEntrée(s) invalide(s) ! Veuillez entrer des nombres représentant les sommets .\n")
            s1 = int(input("\t Sommet 1 :"))
            s2 = int(input("\t Sommet 2 :"))
        p = int(input(" - Quel est son poids ? : "))
        while p < 0:
            print("\nEntrée invalide ! Veuillez entrer un poids positif .\n")
            p = int(input(f" - Poids de l'arête {i}  : "))
        edge = ()
        edge = edge + (s1,)
        edge = edge + (s2,)
        edge_list.append(edge)
        weight_list.append(p)
    combine = list(zip(edge_list , weight_list))
    combine.sort(key =lambda x : x[1])
    edge_list , weight_list = zip(*combine)
    edge_list = list(edge_list)
    weight_list = list(weight_list)
    global P
    for i in weight_list:
        P += i
    return edge_list

def T_invalide():
    if len(T) == n-1:
        return 1
    return 0

def create_ens_sommets(ens_aretes):
    global Sommets
    for i in ens_aretes:
        for j in i:
            Sommets = Sommets | {j}

def ensembles_in_T(edge):
    global T
    global E
    stocker = set()
    ens_T = set()
    count = 1
    if T != set():
        for i in T:
            for j in i:
                ens_T = ens_T | {j}
        for j in edge:
            if j not in ens_T:
                count *= 1
            else:
                count = 0
        if count:
            for i in edge:
                stocker = stocker | {i}
            E.append(stocker)
        modif = set()
        mod = set()
        for b in E:
            for l in edge:
                if l in b:
                    mod = b
                    for r in edge:
                        modif = modif | b | {r}
            if modif != set():
                break
        if mod != set() and modif != set():
            E.remove(mod)
            E.append(modif)
        E_temp = E
    #Homogénéisation
        for k in E:
            stock = set()
            for i in k:
                for l in E:
                    if i in l:
                        stock = stock | l
                        E_temp.remove(l)
            E_temp.append(stock)
        E = E_temp
    else:
        for i in edge:
            stocker = stocker | {i}
        E.append(stocker)

def in_same_ens(edge):
    global E
    first_ = 0
    second_ = 0
    collector = []
    for i in edge:
        collector.append(i)
    for j in E:
        if collector[0] in j and collector[1] in j:
            first_ = 1
            second_ = 1
            break
    if first_ and second_:
        return 1
    return 0

def create_cycle(edge):
    global T
    if T != set() and in_same_ens(edge):
        return 1
    return 0

def check_cycle(edges):
    indice = 0
    global T
    global weight_list
    global P
    for i in edges:
        if T == set():
            print(f"\n L'arête {i} n'engendre pas de cycle \n")
            ensembles_in_T(i)
            T = T | {i}
            continue
        if T != set():
            if create_cycle(i):
                print(f"\n L'arête {i} engendre un cycle \n")
                P = P - weight_list[indice]
                indice += 1
            else:
                print(f"\n L'arête {i} n'engendre pas de cycle \n")
                ensembles_in_T(i)
                T = T | {i}
                indice += 1
                if T_invalide():
                    break

def algorithme():
    global n
    global aretes_
    global T
    print("\n")
    print("\n Bienvenue dans mon programme simulant l'algorithme de Kruskal . Veuillez suivre les étapes qui vous seront demandées . \n")
    vertex_deg = int(input("* Entrez la somme des degrés du graphe : "))
    while vertex_deg < 0:
        print("\n  Entrée invalide ! Entrez un nombre strictement positif pour la somme des degrés .\n")
        vertex_deg = int(input("* Somme des degrés du graphe : "))
    aretes_ = edge_collector(vertex_deg)
    create_ens_sommets(aretes_)
    n = len(Sommets)
    print("\n ::: Résultats issus des itérations ::: \n")
    check_cycle(aretes_)
    print("\n")
    print(f"\n Ensemble des sommets du graphe : {Sommets} \n")
    print(f"L'arbre formé à partir de ce graphe est composé des arêtes : \n")
    print(T)

algorithme()