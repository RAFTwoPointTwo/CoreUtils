def sort_array(tab):
    table_length = len(tab)
    for i in range(1 , table_length):
        k = i
        while k > 0 and tab[k - 1] > tab[k]:
            tab[k] , tab[k - 1] = tab[k - 1] , tab[k]
            k -= 1
    return tab