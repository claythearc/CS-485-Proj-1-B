# Python 3.6.5
# Project Part B
# Clayton A Turner

from math import floor, ceil, sqrt
import time
import random

class HashTable:
    """Class for holding the hash table."""
    def __init__(self):
        """Initialize a dictionary as our base data structure.
            Not using the hash style of dictionaries per se, it's just the best assosciation
            of Key & Value.
         """
        self.values = dict()

    def append(self,value: str):
        """Append a value to our dictionary.
        Get the MD5 hash of the value to be inserted. Sets that as the key
         and the plaintext value as the value. If the key already exists, it raises a Key Error."""
        key = hash(value)
        if key in self.values.keys():
            pass
        self.values[key] = value

    def __str__(self):
        """Function for overriding the string output, outputs as { x, y, z}"""
        temp = []
        for k,v in self.values.items():
            temp.append(v)
        temp = "{ " + ", ".join(str(value) for value in temp) + " }"
        return temp

    def get(self, value):
        """Gets the value assosciated with the key. Sanity check basically."""
        value = hash(value)
        return self.values[value]

    def __contains__(self, item):
        """Overrides the X in Y declaration. Basically checks if the hash exists as a key"""
        item = hash(item)
        return self.values.get(item, False)
    
    
    def hash(self, value):
        templist = str(value)
        templist = list(templist)
        temp = 0
        for item in templist:
            temp += (temp ** item) + 1

def mulinv(a: int, b: int, debug: bool = False):
    """Function to calculate the multiplicative inverse."""
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
    Hashes = HashTable()
    for i in range(0, m):
        Hashes.append(pow(a, i, n))
    print(f"Hash Table: {Hashes}")
    # Here we take b * (a inverse)^i mod n and find i
    # By taking the Array above, and seeing if the item exists in the table.

    for i in range(0, m):
        # solve the equation for B * (a^-1)^i
        temp = (b * (inv**i)) % n
        # Due to the override of __contains__ I can check membership through temp in hashes.
        if temp in Hashes:
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
