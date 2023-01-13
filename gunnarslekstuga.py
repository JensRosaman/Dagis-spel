import random as r
import os
from time import sleep as sleep
one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "

cords = [one , two , three , four , five , six , seven , eight , nine]

board = f"""
  {cords[0]}  I  {cords[1]}  I  {cords[2]}
 --- I --- I ---
  {cords[3]}  I  {cords[4]}  I  {cords[5]}
 --- I --- I ---
  {cords[6]}  I  {cords[7]}  I  {cords[8]}
"""

while " " in cords:
  newMove = input("Which you like change?")
  newMove = int(newMove)
  newMove = newMove - 1
  cords[newMove] = "X"
  print(cords)
  board = f"""
  {cords[0]}  I  {cords[1]}  I  {cords[2]}
 --- I --- I ---
  {cords[3]}  I  {cords[4]}  I  {cords[5]}
 --- I --- I ---
  {cords[6]}  I  {cords[7]}  I  {cords[8]}
 """
  print(board)
  if cords[0] == cords[1] == cords[2] or cords[3] == cords[4] == cords[5] or cords[6] == cords[7] == cords[8]:
    pass
  sleep(2)



