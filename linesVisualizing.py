import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
from time import sleep
import sys

a_list = []
b_list = []
y_list = []
x = np.linspace(-10 , 10 , 100000)
def lines():
    global a_list
    global b_list
    global y_list
    print("\n")
    d = int(input("Entrez le nombre de droites :"))
    print("\n Renseignez le coefficient directeur (a) et l'ordonnée à l'origine (b) de chaque droite: \n")
    for _ in range(d):
        print("\n")
        a = float(input(f"Coefficient directeur de la droite no{_ + 1} : "))
        a_list.append(a)
        b = float(input(f"Ordonnée à l'origine de la droite no{_ + 1} : "))
        b_list.append(b)
        y = a * x + b
        y_list.append(y)
    print("\n")
    print("Equations des droites entrées : ")
    for _ in range(d):
        print("\n")
        if a_list[_] == 1:
            if b_list[_] == 0:
                print(f"Equation de la droite no{_ + 1} : y = x")
                continue
            if b_list[_] < 0:
                print(f"Equation de la droite no{_ + 1} : y = x {b_list[_]}")
                continue
            print(f"Equation de la droite no{_ + 1} : y = x + {b_list[_]}")
            continue
        if a_list[_] == -1:
            if b_list[_] == 0:
                print(f"Equation de la droite no{_ + 1} : y = -x")
                continue
            if b_list[_] < 0:
                print(f"Equation de la droite no{_ + 1} : y = -x {b_list[_]}")
                continue
            print(f"Equation de la droite no{_ + 1} : y = -x + {b_list[_]}")
            continue
        if a_list[_] == 0:
            if b_list[_] == 0:
                print(f"Equation de la droite no{_ + 1} : y = 0")
                continue
            if b_list[_] < 0:
                print(f"Equation de la droite no{_ + 1} : y = {b_list[_]}")
                continue
            print(f"Equation de la droite no{_ + 1} : y = {b_list[_]}")
            continue
        if b_list[_] == 0:
            print(f"Equation de la droite no{_ + 1} : y = {a_list[_]}x")
            continue
        if b_list[_] < 0:
            print(f"Equation de la droite no{_ + 1} : y = {a_list[_]}x {b_list[_]}")
            continue
        print(f"Equation de la droite no{_ + 1} : y = {a_list[_]}x + {b_list[_]}")

def show():
    cmap = get_cmap("tab10")
    for _ in range(len(a_list)):
        color = cmap(_ % cmap.N)
        plt.plot(x, y_list[_], label=f'y = {a_list[_]}x + {b_list[_]}', color = color)
    plt.xlabel('x')
    plt.ylabel('y', rotation = 0)
    plt.legend()
    plt.show()

lines()

print("\n")
print("::: Chargement de la représentation :::")
print("\n")
for i in range(5 , -1 , -1):
    sys.stdout.write(f"\r Loading ...   {i}")
    sys.stdout.flush()
    sleep(1)

show()