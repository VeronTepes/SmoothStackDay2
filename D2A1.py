# -*- coding: utf-8 -*-

import math
import re
"""
Spyder Editor

This is a temporary script file.
"""

#bullet point one
world = "Hello World"

print(world[7] + "\n")

#bullet point two
S = "Thinker"

print(S[2:5] + "\n")

print("S=’hello’,what is the output of h[1]: It will have an error. You are" +
      " Storing the variable in S, but trying to read from h.\n")

#bullet point three
print("S=’Sammy’ what is the output of s[2:]: You will also get an error." +
      " python is case sensitive. Therefore S and s are different variables." +
      " Though if both were S, it would return 'mmy'. \n")

#bullet point four
#word = "Mississippi"

#make it distinct character word. i.e. only can use a letter once.
#print(set(word) + "\n")

print("With a single set function can you turn the word ‘Mississippi’ to distinct character word." + 
      ": No you can't set does not work with strings. That is, if you save it as a string.")

#bullet point five, Palendrome.

quit = False
isPalendrome = True

while quit == False:
    #get input
    i=input("Please enter in the string you want to test if it's a Palendrome: ")
    
    #strip the input of whitespace and punctuation
    
    i = re.sub('\W+','', i)
    
    #is palendrome?
    pointer=len(i)/2
    pointer = math.floor(pointer)
    #print("Pointer: " + str(pointer))
    
    for letter in range(pointer):
        if i[letter] == i[((len(i)-1)-(letter))]:
            continue
        else:
            isPalendrome = False
            
    #output answer:
    if isPalendrome == True:
        print("Y\n")
    else:
        print("N\n")
    
    #again?
    again = input("Do you want to try a different string (y/n)? ")
    if( again == "Y" or again == "y"):
        quit = False
    else:
        quit = True
    
    

