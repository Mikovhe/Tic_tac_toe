def draw_board():
    "Drawing baord on the terminal"
    return "|---1---|---2---|---3---|\n|---4---|---5---|---6---|\n|---7---|---8---|---9---|"

def list_to_string(mylist):
    string = ''
    for s in mylist:
        string +=s

    return string

def check_winner(board):
    
    if (board[4] ==board[12]==board[20] or board[30]==board[38] ==board[46] or board[56]==board[64]==board[72]
            or board[4]==board[30]==board[56] or board[12]==board[38]==board[64] or board[20]==board[46]==board[72]
            or board[4]==board[38]==board[72] or board[20]==board[38]==board[56]):
        return True
    else:
        return False

def game():
    print("player 1 = 'X' and player 2 = 'O'")
    board = draw_board()
    
    board_dict = {'1':4,'2':12,'3':20,'4':30,'5':38,'6':46,'7':56,'8':64,'9':72}
    numbers = [1,2,3,4,5,6,7,8,9]
    play = 0
    while play<9:
        #player1
        print("player X")
        print(board)
        #play
        num = input("Player X select position\n")
        position = board_dict[str(num)]
        board = list(board)

        board[position] = 'X'
        
        if check_winner(board):
            print("player X wins")
            break

        play+=1
        if play ==9:
            print("No winner, this is a draw")
            break

        board = list_to_string(board)
        #player2
        print("player O")
        print(board)

        #play
        position = board_dict[str(input("Player O select position\n"))]
        board = list(board)

        board[position] = 'O'

        if check_winner(board):
            print("player O wins")
            break


        board = list_to_string(board) 
        print(board)
        
        play+=1

game()
