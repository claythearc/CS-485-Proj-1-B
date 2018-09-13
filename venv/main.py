#Python 3.6.5
#Project Part B
#Clayton A Turner
from math import floor

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

a = 43  # type: int
n = 307  # type: int
b = 140  # type: int
m = 20  # type: int
inv = 115
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

