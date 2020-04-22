board=[" " for i in range(9)]
def print_board():
 row1="				| {} | {} | {} |".format(board[0],board[1],board[2])
 row2="				| {} | {} | {} |".format(board[3],board[4],board[5])
 row3="				| {} | {} | {} |".format(board[6],board[7],board[8])
 print()
 print(row1)
 print(row2)
 print(row3)
 print()
def move(icon):
 if icon=='X':
  number=1
 elif icon=='O':
  number=2
 print("Your turn player{}".format(number))
 choice=int(input("enter position 1-9:"))
 if board[choice-1]==" ":
  board[choice-1]=icon
 else:
  print("That place is already taken,you have only one chance more for a new position")
  choice=int(input("enter position"))
  if board[choice-1]==" ":
   board[choice-1]=icon 
  else:
   print("You loose your turn player {}".format(number))
def victory(icon):
 if(board[0]==icon and board[1]==icon and board[2]==icon) or\
   (board[3]==icon and board[4]==icon and board[5]==icon) or\
   (board[6]==icon and board[7]==icon and board[8]==icon) or\
   (board[0]==icon and board[3]==icon and board[6]==icon) or\
   (board[1]==icon and board[4]==icon and board[7]==icon) or\
   (board[2]==icon and board[5]==icon and board[8]==icon) or\
   (board[0]==icon and board[4]==icon and board[8]==icon) or\
   (board[2]==icon and board[4]==icon and board[6]==icon):
  print_board()
  return True 
 else:
  return False
while True:
 print_board()
 move("X")
 print_board()
 if victory("X"):
  print("X wins!!!!")
  break
 move("O")
 if victory("O"):
  print("O wins!!!")
  break
