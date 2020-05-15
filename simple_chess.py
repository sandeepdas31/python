import chess

board=chess.Board()
print(board.legal_moves)
print(board)
flag=0

for i in range (1,76):
  a=str(input("Enter value: "))
  board.push_san(a)
  print(board)

  moves=board.is_seventyfive_moves()
  if(moves==True):
    Print("75 Moves over")
    print("Game Draw")
    break

  stale=board.is_stalemate()
  if (stale==True):
    Print("Stale")
    print("Its a draw")
    break

  insuf=board.is_insufficient_material()
  if(insuf==True):
    print("insufficient material")
    print("Its a draw")
    break

  tcheck=board.is_check()
  if(tcheck==True):
    flag=flag+1
    if(flag==5):
      break


  check=board.is_checkmate()
  if(check==True):
    print("Checkmate")
    print("Game over")
    break

  over=board.is_game_over()
  if(over==True):
    print("Game over")
    break

print(board)