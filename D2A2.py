# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 07:37:43 2022

@author: owner
"""

#bullet point number one
mylist = [1, "one", 1.000]
print(mylist)
print("\n")

#bullet point number two
yourlist1 = [1, 2]
yourlist2 = [1, 1, yourlist1]

print(yourlist2[2][1])
print("I have a nested list [1,1[1,2]], how to grab the value of 2 from the list." + 
      " You would treat it as a 2d array instead of a 1d array. \n")

#bullet point number 3
Ist = ['a','b','c']
print(Ist[1:])
print("lst=['a','b','c'] What is the result of lst[1:]?" + 
      "You would get everything after the second value stored in the list.\n")


#bullet point number 4
weekdays = {
    "Monday": 1,
    "Tuseday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
    }

print(weekdays)

#bullet point number 5
print("\nD={‘k1’:[1,2,3]} what is the output of d[k1][1]" + 
      "It would print out 2 if both were D or both were d. As it is right now it wouldn't work.")
D={
   "k1":[1,2,3]
   }
print(D["k1"][1])
print("\n")


#bullet point number 6
print("Can you create a list [1,[2,3]] into a tuple? "
      + "Yes you can with casting.")
list = [2,3]
list = [1,list]

print(tuple(list))
print("\n")

#bullet point number 7
print("With a single set function can you turn the word ‘Mississippi’ to distinct character word." + 
      " No you can't set does not work with strings. That is, if you save it as a string.\n")

#bullet point number 8
Ist.append("X")
print("Can you add an element ‘X’ to the above created set? " +
      "Yes you can if you use the append function.")
print(Ist)
print("\n")

#bullet point number 9

    #question one
        #	Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
        #between 2000 and 3200 (both included).
        #	The numbers obtained should be printed in a comma-separated sequence on a single line.
        #	Hints: 
        #	Consider use range(#begin, #end) method



    #question 2
        #Write a program which can compute the factorial of a given numbers.
        # results should be printed in a comma-separated sequence on a single line.
        
        
    #question 3
        #With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
        #such that is an integral number between 1 and n (both included). 
        #and then the program should print the dictionary.



    #question 4
        #Write a program which accepts a sequence of comma-separated numbers from console 
        #and generate a list and a tuple which contains every number.
        
        
    #question 5
        #Define a class which has at least two methods:
            #getString: to get a string from console input
            #printString: to print the string in upper case.
            #Also please include simple test function to test the class methods.

