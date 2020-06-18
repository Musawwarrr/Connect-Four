import connectfour

#Displays the board of the game
def board(game_state: connectfour.GameState):
    column = connectfour.BOARD_COLUMNS
    row = connectfour.BOARD_ROWS
    
    for num in range(column):
        num = num + 1
        print(num, end = " ")
    print()
    
    board_change(game_state, 0, ".", 1, "R", 2, "Y")
    
    for p in zip(*game_state.board): 
        print(*p) 
    print()

    board_change(game_state, ".", 0, "R", 1, "Y", 2)

#Changes board for display
def board_change(game_state, a, new1, b, new2, c, new3):
    for m in game_state.board:
        for x,i in enumerate(m):
            if i == a:
                m[x]= new1
            elif i == b:
                m[x] = new2
            elif i == c:
                m[x] = new3

#Inputs if the user wants to drop or pop
def player_move(game_state, move, column):
    try:
        
        while True:
            try:
                print()
                if move == "D":
                    return connectfour.drop(game_state, column - 1)
                elif move == "P":
                    return connectfour.pop(game_state, column - 1)
            except ValueError:
                print('Column Number must be int between 0 and {}.\n'.format(connectfour.BOARD_COLUMNS - 1))

    
    except connectfour.InvalidMoveError:
        print("Invalid Move\n")
        return game_state
    except connectfour.GameOverError: 
        print("The Game is already over!")
        return game_state

#Tells that the game is over and who won 
def game_over(user):
    if user == connectfour.YELLOW:
        print ("Congratulations Red User! You have won the game!")
    elif user == connectfour.RED: 
        print("Congratulations Yellow User! You have won the game!")

#Choosing drop or pop
def d_or_p():
    while True:
        move = input("What would you like to do? D = drop, P = Pop.\n").strip().upper()
        if move == "D":
            return move
        elif move == "P":
            return move
        else:
            print("Invalid move, please choose a correct action.\n")
        print()
    
#Choosing Column
def col_num():
    column = int(input("In which column would you like to do that?\n"))
    return column






