#Python 3.6.5
#Project Part B
#Clayton A Turner
from math import floor

def mulinv(a: int, b: int):
    #initialize other variables
    q = 0
    x = 0
    y = 1
    yl = 1
    xl = 1
    while b != 0:
        q = a//b
        a,b = b, a%b
        x,xl = xl-q*x, x
        y,yl = yl-q*y, y
    print(f" x: {x} y: {y} q: {q} xl: {xl} yl: {yl}")
    return xl

def calculate_lnr(a1, b1):
    a = int(a1)
    b = int(b1)
    q = a // b
    r = a - (q * b)
    return r

a = 43  # type: int
n = 307  # type: int
b = 140  # type: int
m = n-1  # type: int
inv = calculate_lnr(a, n)
inv = mulinv(inv, n)
print(inv)
Idx_List = []  # type: list(int)
#Problem looks like A^x is congruent to b mod n

#Build the list of A^i mod n for i = [0, m)
for i in range(0, m):
    Idx_List.append( pow(a,i,n) )
Idx_List.sort()  # sort the list
#Here we take b * (a inverse)^i mod n and find i
#By taking the Array above, and seeing if the item exists in the table.

idx = False
for i in range(0, m):
    temp = (b * (inv**i)) % n
    first = 0
    last = len(Idx_List)
    while (first <= last) and (not idx):
        mid = (first+last)//2
        if Idx_List[mid] == temp:
            idx = True
        else:
            if temp < Idx_List[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if(idx):
        print(f"The Answer is: {i} Giving us {b}*{inv}^{i} \n")
        break

