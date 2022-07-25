#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:22:25 2022
Homework
@author: p_thongkumkoon
"""

name= input("What is your name?")
Stick = int(input("How many stick in the pile?"))
time = 0
while Stick > 0:
  A= int(input(name  + " How many stick you will take?"))
  if A > 2:
    print ("No you cannot take more than 2 sticks!")
    continue
  elif A < 1:
    print ("Noyou cannot take less than 1 stick!")
    continue
  elif A > Stick:
    print ("There are not enoughsticks to take")
  else:
    Stick = Stick - A
    print ("There are", Stick, "in the pile.")
    time = time + 1
print ("OK. There is no stick left in the pile. You spent", time, "times.")
    