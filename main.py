#Global Variable


#game board
board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-",]

#If game_is_still_running
game_is_still_running = True

#Who won? or Tie?
winner = None


#Whos turn is it?
current_player = "X"

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
  display_board()

  while game_is_still_running:
    
    #handle a single turn of arbitrary player
    handle_turn(current_player)


    check_if_game_is_over()

    #switch from one player to other
    flip_player()

  #The Game has ended here
  if winner == "X" or winner == "O":
    print("Winner is "+ winner)

  elif winner == None:
    print("The Game is Tied!!")


def handle_turn(player):

  print( "Player " + player + "'s Turn")

  postition = input("Choose a postition from 1-9 \n")
  
  valid = False

  # this while loop is for stopping user from selecting a already taken place
  while not valid:

    # the input place should be between 1 to 9 ONLY!
    while postition not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      postition = input("Invalid Input, Please Choose a postition from 1-9 \n")

    # Our list starts from 0, So we have to substract 1
    postition = int(postition) - 1

    # If statement to stop from overridding the previous plays
    if board[postition] == "-":
      valid = True
    else:
      print("You cannot go there, Please select once again")
  
  
  board[postition] = player
  display_board()


def check_if_game_is_over():
  check_the_winner()
  check_if_tie()


#check for winner
def check_the_winner():

  #Set up the global variable (winner)
  global winner

  row_winner = check_rows()

  col_winner = check_cols()

  diagonals_winner = check_diagonals()

  if row_winner :
    #there was a winner
    winner = row_winner
  elif col_winner: 
    #there was a winner
    winner = col_winner

  elif diagonals_winner:
    #there is a winner
    winner = diagonals_winner
  
  else:
    #there was no winnner
    winner = None
  return

#check rows for winner
def check_rows():
  #Set up global variable (game_is_still_running)
  global game_is_still_running

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  #If any of the row finds a match, flag it as winner 
  if row_1 or row_2 or row_3:
    game_is_still_running = False

  # Return the Winner (X or O)
  if row_1:
    return board[0]
  
  if row_2:
    return board[3]

  if row_3:
    return board[6]

  return

#check columns for winner
def check_cols():
  #Set up global variable (game_is_still_running)
  global game_is_still_running

  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  
  #If any of the column finds a match, flag it as winner 
  if column_1 or column_2 or column_3:
    game_is_still_running = False

  # Return the Winner (X or O)
  if column_1:
    return board[0]
  
  if column_2:
    return board[1]

  if column_3:
    return board[2]
  return

#check the diagonal for winner
def check_diagonals():
  #Set up global variable (game_is_still_running)
  global game_is_still_running

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  
  #If any of the diagonal finds a match, flag it as winner 
  if diagonal_1 or diagonal_2 :
    game_is_still_running = False

  # Return the Winner (X or O)
  if diagonal_1:
    return board[0]
  
  if diagonal_2:
    return board[2]
  return

def check_if_tie():
  
  global game_is_still_running

  if "-" not in board:
    game_is_still_running = False
  return

 
def flip_player():
  
  # To Set the global variable
  global current_player

  # If the current_player is X, then make it O
  if current_player == "X":
    current_player = "O"
  
  # If current_player is O, then make it X
  elif current_player == "O":
    current_player = "X"
play_game()