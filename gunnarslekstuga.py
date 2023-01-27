import random
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
  # X's turn

  print(board)
  while True:
    newMoveX = input("Which you like change?")
    newMoveX = int(newMoveX)
    newMoveX = newMoveX - 1
    if cords[newMoveX] == " ":
      cords[newMoveX] = "X"
      break
    
    print("Already taken choose new")

  print(cords)
  print(board)

  if cords[0] == cords[1] == cords[2] or cords[3] == cords[4] == cords[5] or cords[6] == cords[7] == cords[8]:
    pass
  sleep(1)

  # O's turn
  print("O's turn")
  if " " in cords:
    while True:
      newMoveO = random.choice(range(0,8))
      if cords[newMoveO] == " ":
        break
    cords[newMoveO] = "O"
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



