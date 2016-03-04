"""
File: sum_powers.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code will sum b^0 through b^n.

"""

n_str = input("Enter a number (this will be the exponent, cannot be 1.0): ")
n = float(n_str)

b_str = input("Enter another number (this will be the base):")
b = int(b_str)

#subtotal = 1 + int(b_str)**n
i = 0
total = 0

while i < n:
    #subtotal += i
    total += b**i
    i += 1

print "Your total equals %d" %total
#print ((b ** (n + 1) - 1)(b - 1)
print (b**(n+1)-1)/(b-1)
