# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:20:04 2020

@author: win 10
"""

def conversion(coor):
    print(coor)
    row=0
    if(int(coor[1])>=0 and int(coor[1])<=9):
        for i in range(len(coor)-1):
            if((int(coor[i+1])>0) and (int(coor[i+1])<10)):
                row+=1
    print(row)
conversion('a34e2')