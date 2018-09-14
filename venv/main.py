# Python 3.6.5
# Project Part B
# Clayton A Turner

from math import floor, ceil, sqrt
import time
import timeit
def mulinv(a: int, b: int, debug: bool = False):
    # initialize other variables
    q = 0
    x = 0
    y = 1
    yl = 1
    xl = 1
    # loop through the operations
    while b != 0:
        q = a//b
        a,b = b, a%b
        x,xl = xl-q*x, x
        y,yl = yl-q*y, y
        if debug:
            # debug flag to print result of the operations
            print(f" a: {a} b: {b} x: {x} y: {y} q: {q} xl: {xl} yl: {yl}")
    return xl


def main():
    a = int(input("Input Value of A: "))  # type: int
    n = int(input("Input Value of N: "))  # type: int
    b = int(input("Input Value of B: "))  # type: int
    # m = ceiling of the square root of m
    m = ceil((sqrt(n)))  # type: int
    print(f"Ceiling of Sqrt(n): {m}")
    # now we need the LNR of a^m mod n
    LNR = pow(a, m, n)
    print(f"LNR: {LNR}")
    # now we want the modular inverse of the lnr

    inv = mulinv(LNR, n)
    print(f"Modular Invese: {inv}")
    Idx_List = []  # type: list(int)
    # Problem looks like A^x is congruent to b mod n

    # Build the list of A^i mod n for i = [0, m)
    for i in range(0, m):
        Idx_List.append(pow(a, i, n))
    Idx_List.sort()  # sort the list
    print(f"Sorted Array: {Idx_List}")
    # Here we take b * (a inverse)^i mod n and find i
    # By taking the Array above, and seeing if the item exists in the table.

    idx = False
    for i in range(0, m):
        # solve the equation for B * (a^-1)^i
        temp = (b * (inv**i)) % n
        first = 0
        last = len(Idx_List)
        # binary search. loop through, move midpoint to middle each orientation, if it's less check the bottom half
        # if it's more, check the top half. repeat until you're out of list or it's found
        while (first <= last) and (not idx):
            mid = (first+last)//2
            if Idx_List[mid] == temp:
                idx = True
            else:
                if temp < Idx_List[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        if idx:
            print(f"The Answer is: {i} Giving us {b}*{inv}^{i} \n")
            break


if __name__ == "__main__":
    timenow = time.process_time()
    walltime = time.time()
    try:
        main()
    except IndexError:
        print("Not found.")
    timeafter = time.process_time()
    wallafter = time.time()
    print("Process took: {}".format(timeafter - timenow))
    print("Wall Time: {}".format(wallafter - walltime))
