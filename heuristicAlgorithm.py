rapport_list = []
poids = []
valeurs = []
objets = []
objets_tries = []
P = 0
V = 0
took = []
p_max = 0
def collector():
    global rapport_list
    global poids
    global valeurs
    global objets
    global p_max
    print("\n")
    p_max = int(input("Quel est le poids maximal de vote sac ? : "))
    n = int(input("Combien d'objets sont à évaluer ? : "))
    print("\n Entrez les poids et valeurs des objets : \n")
    for i in range(n):
        print(f"\n Objet {i + 1} : \n")
        p = int(input("Poids : "))
        v = int(input("Valeur : "))
        poids.append(p)
        valeurs.append(v)
        objets.append((p , v))
        took.append(0)
        r = v / p
        rapport_list.append(r)
def iterations():
    global P
    global took
    global V
    global rapport_list
    global objets
    global objets_tries
    objets_tries = objets
    combine = list(zip(rapport_list, objets_tries))
    combine.sort(key=lambda x: x[0])
    combine.reverse()
    rapport_list, objets_tries = zip(*combine)
    rapport_list = list(rapport_list)
    objets_tries = list(objets_tries)
    for i in objets_tries:
        if ((P + i[0]) <= p_max):
            took[objets.index(i)] = 1
            P += i[0]
            V += i[1]

def algorithme():
    print("\n Bonjour , et bienvenue dans mon programme simulant la méthode heuristique pour le PROBLEME DU SAC A DOS de la Recherche Opérationnelle . \n")
    collector()
    iterations()
    print("\n")
    print("| NB : Les objets pris dans le sac ont le bool << 1 >> , et les objets laissés ont le bool << 0 >> ! | \n\n Ainsi , les résultats issus des itérations révèlent : \n")
    print("| | | | | |")
    j = 0
    for i in took:
        print(f"Objet {j + 1} : {i}")
        j += 1
    print("| | | | | |")
    print("\n")
    print("Au total , les objets pris dans le sac sont :")
    print("\n")
    for i in range(len(took)):
        if took[i] == 1:
            print(f"► Objet {i + 1} \n")
    print(f"Poids total des objets pris dans le sac : P = {P}")
    print(f"Valeur totale des objets pris dans le sac : V = {V}")

algorithme()