# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:56:29 2020

@author: win 10
"""
# =============================================================================
# Theatre Square in the capital city of Berland has a 
# rectangular shape with the size n × m meters. 
# On the occasion of the city's anniversary, a decision was taken 
# to pave the Square with square granite flagstones. 
# Each flagstone is of the size a × a.
# What is the least number of flagstones needed to pave the Square? 
# It's allowed to cover the surface larger than the Theatre Square, 
# but the Square has to be covered. 
# It's not allowed to break the flagstones. 
# The sides of flagstones should be parallel to the sides of the Square.
# =============================================================================
def flagstones(m,n,a):
    c1=int(m/a)
    c2=int(n/a)
    if(m%a):
        c1=c1+1
    if(n%a):
        c2=c2+1
    return c1*c2
m=int(input())
n=int(input())
a=int(input())
print(flagstones(m,n,a))    