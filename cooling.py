"""
File: cooling.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code will estimate the temperature of hot tea as each minute passes by.

"""

t = 0 #minutes
T_tea = 100 #degrees C
T_air = 20 #degrees C
k = 0.055

T_tea_str = raw_input ("Enter the initial tea temperature:")
T_tea= int(T_tea_str)

# T_tea = T_tea - k(T_tea - T_air) #After 1 min the tea temp will be k(T_tea-T_air) colder

T_air_str = raw_input ("Enter the room temperature:")
T_air = float(T_air_str)

mins_str = raw_input ("Enter the length of time (in minutes) for which the tea was cooling down:")
mins = float(mins_str)

t = 0

print "Time Temperature"

while t < 20:
    print "%3.1d   %4.1f"%(t, T_tea)
    T_tea -= k*(T_tea - T_air)
    t += 1

print "%3.1d   %4.1f"%(t, T_tea)
