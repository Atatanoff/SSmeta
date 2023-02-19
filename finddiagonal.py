
def diag(n):
    d = int(n*(n-3)/2)
    p = [chr(i+65) for i in range(n)]
    lst = []
    indx2 = 1
    for i in range(d):
        indx1 = i%n
        if indx1 == 0: indx2+=1
        lst.append(p[indx1]+p[indx2])
        indx2+=1
        indx2%=n
    return lst
