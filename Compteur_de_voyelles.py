def compteur_de_voyelles(chaine):
    voyelles = ['a', 'i', 'e', 'o', 'y', 'u']
    c = 0
    for char in chaine:
        if char in voyelles:
            c += 1
    return c
