from sys import stdout
from time import sleep
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def index_error_generator(word , index = None):
    if index is not None:
        before_chars = "".join([word[ind] for ind in range(index)])
        error_char = f"\033[31m{word[index]}\033[0m"
        after_chars = "".join([word[ind] for ind in range(index + 1, len(word))])
        word_with_index_error = before_chars + error_char + after_chars
        print(f"\n Indexation : {word_with_index_error} \n")
    else:
        print(f"\n Indexation : {word} \n")

def compare_words(word1 , word2):
    print("\n ::::: Analyse des mots ::::: \n")
    bar_length = 30
    for _ in range(len(word1)):
        if len(word1) >= len(word2):
            try:
                if word1[_] == word2[_]:
                    filled_length = int(bar_length * (_ + 1) / len(word1))
                    loading_tiles = "█" * filled_length
                    empty_tiles = " " * (bar_length - filled_length)
                    stdout.write(f"\r[{loading_tiles}{empty_tiles}] {_ + 1} / {len(word1)}")
                    stdout.flush()
                    sleep(0.01)
                else:
                    print("\n")
                    print(f"\n Une erreur est subvenue , au caractère : \033[31m {word1[_]} \033[0m ! \n")
                    print(f"\n \033[34m {word1[_]} \033[0m est \033[31m différent \033[0m de \033[34m {word2[_]} \033[0m \n")
                    index_error_generator(word1, _)
                    index_error_generator(word2, _)
                    sleep(1.2)
                    print(f"\n \033[34m {word1} \033[0m est \033[31m différent \033[0m de \033[34m {word2} \033[0m \n")
                    sleep(2)
                    return
            except IndexError:
                print("\n")
                print(f"\n Une erreur est subvenue , au caractère : \033[31m {word1[_]} \033[0m ! \n")
                print(f"\n \033[34m {word1} \033[0m est \033[31m plus long \033[0m que \033[34m {word2} \033[0m \n")
                index_error_generator(word1, _)
                index_error_generator(word2)
                sleep(1.2)
                print(f"\n \033[34m {word1} \033[0m est \033[31m différent \033[0m de \033[34m {word2} \033[0m \n")
                sleep(2)
                return
        else:
            print("\n")
            index = 0
            integral_is_same = True
            for charIndex in range(len(word1)):
                if word1[charIndex] != word2[charIndex]:
                    index = charIndex
                    integral_is_same = False
                    break

            effective_index = len(word1) if integral_is_same else index

            if not integral_is_same:
                print(f"\n Une erreur est subvenue , au caractère : \033[31m {word1[effective_index]} \033[0m ! \n")
                print(f"\n \033[34m {word1[effective_index]} \033[0m est \033[31m différent \033[0m de \033[34m {word2[effective_index]} \033[0m \n")
                index_error_generator(word1 , effective_index)
                index_error_generator(word2, effective_index)
                sleep(1.2)
                print(f"\n \033[34m {word1} \033[0m est \033[31m différent \033[0m de \033[34m {word2} \033[0m \n")
                sleep(2)
                return

            print(f"\n Une erreur est subvenue , au caractère : \033[31m {word2[effective_index]} \033[0m ! \n")
            print(f"\n \033[34m {word1} \033[0m est \033[31m plus court \033[0m que \033[34m {word2} \033[0m \n")
            index_error_generator(word1)
            index_error_generator(word2, effective_index)
            sleep(1.2)
            print(f"\n \033[34m {word1} \033[0m est \033[31m différent \033[0m de \033[34m {word2} \033[0m \n")
            sleep(2)
            return

    stdout.flush()
    print(f"\n\n Le test est effectif ! \033[34m {word1} \033[0m est \033[32m exactement le même \033[0m que \033[34m {word2} \033[0m \n\n")
    sleep(2)

def process():
    want_to_quit = False
    while not want_to_quit:
        clear_screen()
        print("\n Entrez les mots dont vous voulez tester l'exact ressemblance . \n")
        word1 = input("\n * Mot 1 : ").strip()
        word2 = input("\n * Mot 2 : ").strip()
        print()
        compare_words(word1 , word2)
        quit_programme = 0
        while quit_programme not in [1 , 2]:
            try:
                quit_programme = int(input("\n * Voulez vous quitter le programme ? : \n\n 1 - Quitter ? \n 2 - Continuer ? \n\n * Choix : "))
                want_to_quit = True if quit_programme == 1 else False
                if quit_programme not in [1, 2]:
                    print("\n ** Veuillez entrer une valeur parmi les propositions 1 et 2 ! **")
            except (TypeError , ValueError):
                print("\n ** Veuillez entrer une valeur parmi les propositions 1 et 2 ! **")
    print("\n \033[33m GoodBye ! \033[0m \n")
    input("\n Veuillez appuyer sur [ ENTER ] pour fermer la fenêtre . \n")


process()