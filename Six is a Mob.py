# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:02:07 2022

@author: owner
"""

#make list of names >4
names = ["Jason", "Monde", "Riley", "Scott", "Dale", "Christopher", "Jessica", "Tanner"]

#if more than 3 people in a room print message saying the room is crowded
def isCrowded(people):
    if  people > 5:
        print("There is a mob in the room")
    elif people >=3:
        print("The room is not very crowded")
    elif people >=1:
        print("The room is not crowded")
    else:
        print("The room is empty")
    
isCrowded(len(names))

names.pop(0)
names.pop(0)
#print(names)

isCrowded(len(names))