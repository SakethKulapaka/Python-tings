# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:44:23 2018

@author: saket
program : issa prime
"""
while True :
    try :
        n = int(input("Enter number : "))
    except ValueError :
        print("Enter a proper number!")
        continue
    if( n==0 or n==1 ) :
        print("Not a prime number")
    elif(n==2) :
        print("Issa prime!")
    else :    
        for i in range(2,n) :
            if(n%i == 0) :
                break
        if(i == n-1):
            print("Issa prime!")
        else :
            print("Not a prime number")    
    exit = input("Hit x to exit : ")
    if (exit == 'x' or exit == 'X') :
        break
    else:
        continue
