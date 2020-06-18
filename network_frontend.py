import connectfour
import backend
import network_backend

host = 'www.ics.uci.edu'
port = 5151

#Ask user which host and port to connect
def ask_user():
    
    inp_host = input("Please specify the host server: ").strip()
    host = inp_host

    inp_port = int(input("Please specify the port: "))
    port = inp_host

#Gets username 
def username():
    username = input("Please enter a username. It cannot have any space.\n").strip()
    print()
    while True: 
        if ' ' not in username and len(username) > 0: 
            return username
        else:
            print("That is not a valid username, try again.\n")
    
#Sets everything up and connects to the server to start the game 
def set_up():

    ask_user()
    connection = network_backend.make_connection(host, port)
    username = username()

    try:
        network_backend.login(connection, username)
        print(network_backend.message_read(connection))
        network_backend.ask_AI(connection)
        print(network_backend.message_read(connection))
        game(connection)

    finally:
        network_backend.close_connection(connection)

#Plays the game 
def game(connection):

    game_state = connectfour.new_game()
    backend.board(game_state)

    while True: 

        game_state = turn_user(connection)
        backend.board(game_state)
        server_reply = network_backend.message_read(connection)

        if server_reply == "OKAY":
            game_state_2 = server_turn(connection)

            if game_state != game_state_2:
                game_state = game_state_2
            else: 
                print("The server has made an invalid move. The game will close.")
                break

            backend.board(game_state)

        elif server_reply == "WINNER_RED":
            backend.game_over(connectfour.RED)
            break
        elif server_reply == "WINNER_YELLOW":
            backend.game_over(connectfour.YELLOW)
            break

        server_reply = network_backend.message_read(connection)

        if server_reply == "READY":
            print()
            print("It is now your turn again!\n")
        elif server_reply == "WINNER_RED":
            backend.game_over(connectfour.RED)
            break
        elif server_reply == "WINNER_YELLOW":
            backend.game_over(connectfour.YELLOW)
            break 

#The user plays
def turn_user(connection):
    game_state = backend.player_move(game_state)
    send_turn_server(connection)

    return game_state
        
# Sends the users turn to the server    
def send_turn_server(connection):
    d_or_p = "Connectfour"
    
    if backend.d_or_p() == "D":
        d_or_p = "DROP"
    elif backend.d_or_p() == "P":
        d_or_p = "POP"
    
    column = backend.col_num()

    network_backend.message_send(connection, d_or_p + " " + str(column))


#Servers turn 
def server_turn(connection): 
    print()
    print("Its now the sever's turn!\n")

    move = network_backend.message_read(connection)
    move_and_column = move.split()
    server_move = move_and_column[0]
    column = move_and_column[1]

    try: 
        column = int(column)
    except ValueError: 
        return game_state   

    if server_move in ["DROP", "POP"]:
        if server_move == "DROP":
            server_move = "D"
            game_state = backend.player_move(game_state, server_move, column)
        elif server_move == "P":
            server_move = "P"
            game_state = backend.player_move(game_state, server_move, column) 
        return game_state
    else: 
        return game_state

def main():
    set_up()
    inp = input("Would you like to play a new game? Y = Yes, N = No.\n").strip().upper()
    if inp == "Y":
        print()
        main()
    elif inp == "N":
        exit()
    else:
        print("Please choose a correct option.\n")

if __name__ == '__main__':
    main()

    




