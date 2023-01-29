import random


def TicTacToe():
  'Simulates the game TicTacToe against a bot. Returns "win" , "draw" , loss  - depending on corresponding circumstance'
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

    # Collects each of the value in a row/collumn and stores it in a list used for checking for three in a row
    topRow = [cords[0],cords[1],cords[2]]
    middleRow = [cords[3],cords[4] , cords[5]]
    bottomRow = [cords[6],cords[7] , cords[8]]
    bottomDiagonal = [cords[6],cords[4] , cords[2]]
    topDiagonal = [cords[0] , cords[4] , cords[8]]
    leftCollumn = [cords[0] , cords[3] , cords[6]]
    middleCollumn = [cords[1] , cords[4] , cords[7]]
    rightCollumn = [cords[2] , cords[5] , cords[8]]

    # Visual representation of the playing board
    board = f"""
    {cords[0]}  I  {cords[1]}  I  {cords[2]}
   --- I --- I ---
    {cords[3]}  I  {cords[4]}  I  {cords[5]}
   --- I --- I ---
    {cords[6]}  I  {cords[7]}  I  {cords[8]}
    """

    # Checks for win, by removing duplicates and checking if theres only one left
    allRows = [topRow,middleRow,bottomRow,bottomDiagonal,topDiagonal,leftCollumn,middleCollumn,rightCollumn]
    for row in allRows:
        row = set(row)
        if not " " in row and len(row) == 1:
          if "X" in row:
            print("Grattis du vinna mkt bra")
            return True
          
          else:
            print("L bozo")
            return False

    
    # X's turn X is the player and requires input
    print(board)
    while True:

      # Gets input and checks if it is as expected
      while True:
        newMoveX = input("Vilken ruta vill du kryssa? Obs ett tal mellan 1 - 9 som numrerar rutorna höger->väntster ")
        try:
          newMoveX = int(newMoveX)
          if newMoveX in range(1,9):
            break
          
          else:
            print("Obs endast tal mellan 1 - 9")
        except:
          print("Obs endast tal mellan 1 - 9")
      newMoveX = newMoveX - 1
      if cords[newMoveX] == " ":
        cords[newMoveX] = "X"
        break
      print("Den rutan är redan tagen gubben, välj en ny")

    # O's turn, compleatly dicated by chance
    if " " in cords:
      # Randomizes a number until it has found an usable one with no letter assinged
      while True:
        newMoveO = random.choice(range(0,8))
        if cords[newMoveO] == " ":
          break
      cords[newMoveO] = "O"

  # Outside while loop -> whole board filled -> draw
  return "draw"  
  


def rockPaperScissor():
  playerInput = input("Vad väljer du?")
  botPick = random.choice(range(2))
  print(botPick)
  
  while True
    # Assignes a string based on the randomized number
    if botPick == 0:
      botPick = "sten"
    
    elif botPick == 1:
      botPick = "sax"

    elif botPick == 2:
      botPick = "påse"

    # Compares the bots choice and the player and checks for win conditions
    
    if botPick == "sten" and playerInput == "sax":
      
      rockPaperScissorResult = "win"
      return "win"




rockPaperScissor()
