def est_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False


for i in range (1, 21):
    if est_pair(i):
        print (i)