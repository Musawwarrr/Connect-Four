import connectfour
import backend

#Presents the welcome message 
def welcome():
    print("Welcome to Connect 4!")
    print ()

#Asks user if wants to change rows and column
def ask():
    inp = input("Would you like to change the number or rows and columns or play with the default number? C = Change, D = Don't change\n").strip().upper()
    if inp == "C":
        print()
        row()
        print()
        column()
        print() 
    elif inp == "D":
        pass
    else: 
        print()
        print("Invalid choice.")
        ask()

#User selects rows
def row():
    rows = int(input("How many rows would you like?\n"))
    connectfour.BOARD_ROWS = rows

#User selects rows
def column():
    columns = int(input("How many columns would you like?\n"))
    connectfour.BOARD_COLUMNS = columns


#Returns the turn 
def turn():
    return game_state.turn

#Looping of turns and the play of the game
def play_game():
    welcome()

    ask()

    game_state = connectfour.new_game()

    while True: 
        backend.board(game_state)

        if game_state.turn == connectfour.RED:
            print("Red user, it is your turn!\n")
        elif game_state.turn == connectfour.YELLOW:
            print("Yellow user, it is your turn!\n")
        print()
        
        move = backend.d_or_p()
        column = backend.col_num() 
        game_state = backend.player_move(game_state, move, column)
        win = connectfour.winner(game_state)
        if win != connectfour.NONE:
            backend.game_over(game_state.turn)
            backend.board(game_state)
            break 

#Continuing a game
def main():
    play_game()
    inp = input("Would you like to play a new game? Y = Yes, N = No.\n").strip().upper()
    if inp == "Y":
        print()
        main()
    elif inp == "N":
        exit()
    else:
        print("Please choose a correct option.\n")

if __name__ == "__main__":
    main()





