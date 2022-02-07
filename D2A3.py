# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:46:00 2022

@author: owner
"""

#Three is a Crowd part 1

#make list of names >4
names = ["Jason", "Monde", "Riley", "Scott"]

#if more than 3 people in a room print message saying the room is crowded
def isCrowded(people):
    if  people > 3:
        print("The room is crowded")

isCrowded(len(names))

names.pop(0)
names.pop(0)
#print(names)

isCrowded(len(names))


#Three is a crowd part 2

#see other program labled as such.


#six is a Mob

#see other program labled as such.