for i in range(2, 1001):
    premier = True

    for diviseur in range(2, i):
        if i % diviseur == 0:
            premier = False

    if premier:
        print(i)