# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:00:30 2022

@author: owner
"""

#make list of names >4
names = ["Jason", "Monde", "Riley", "Scott"]

#if more than 3 people in a room print message saying the room is crowded
def isCrowded(people):
    if  people > 3:
        print("The room is crowded")
    else:
        print("The room is not very crowded")
    
isCrowded(len(names))

names.pop(0)
names.pop(0)
#print(names)

isCrowded(len(names))