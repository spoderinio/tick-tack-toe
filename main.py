a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "

continue_playing = True


def player1():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, continue_playing
    if continue_playing == False:
        return continue_playing
    us1_inp = input("Player1(X): Please make your move: ").lower()
    if us1_inp != "a1" and us1_inp != "a2" and us1_inp != "a3" and us1_inp != "b1" and us1_inp != "b2" and us1_inp != "b3" and us1_inp != "c1" and us1_inp != "c2" and us1_inp != "c3":
        print("Sorry that was an invalid input, please try again")
        us1_inp = input("Player1(X): Please make your move: ").lower()
    if us1_inp == "a1":
        if a1 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            a1 = "X"
    elif us1_inp == "a2":
        if a2 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            a2 = "X"
    elif us1_inp == "a3":
        if a3 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            a3 = "X"
    elif us1_inp == "b1":
        if b1 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            b1 = "X"
    elif us1_inp == "b2":
        if b2 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            b2 = "X"
    elif us1_inp == "b3":
        if b3 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            b3 = "X"
    elif us1_inp == "c1":
        if c1 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            c1 = "X"
    elif us1_inp == "c2":
        if c2 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            c2 = "X"
    elif us1_inp == "c3":
        if c3 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            c3 = "X"


def player2():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, continue_playing
    if continue_playing == False:
        return continue_playing
    us2_inp = input("Player2(O): Please make your move: ").lower()
    if us2_inp != "a1" and us2_inp != "a2" and us2_inp != "a3" and us2_inp != "b1" and us2_inp != "b2" and us2_inp != "b3" and us2_inp != "c1" and us2_inp != "c2" and us2_inp != "c3":
        print("Sorry that was an invalid input, please try again")
        us2_inp = input("Player2(O): Please make your move: ").lower()
    if us2_inp == "a1":
        if a1 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            a1 = "O"
    elif us2_inp == "a2":
        if a2 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            a2 = "O"
    elif us2_inp == "a3":
        if a3 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            a3 = "O"
    elif us2_inp == "b1":
        if b1 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            b1 = "O"
    elif us2_inp == "b2":
        if b2 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            b2 = "O"
    elif us2_inp == "b3":
        if b3 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            b3 = "O"
    elif us2_inp == "c1":
        if c1 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            c1 = "O"
    elif us2_inp == "c2":
        if c2 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            c2 = "O"
    elif us2_inp == "c3":
        if c3 != " ":
            print("Sorry that is not allowed.")
            continue_playing = False
            return continue_playing
        else:
            c3 = "O"


def check_p1():
    global continue_playing
    if a1 == "X" and a2 == "X" and a3 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif b1 == "X" and b2 == "X" and b3 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif c1 == "X" and c2 == "X" and c3 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif a1 == "X" and b1 == "X" and c1 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif a2 == "X" and b2 == "X" and c2 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif a3 == "X" and b3 == "X" and c3 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif a1 == "X" and b2 == "X" and c3 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing
    elif a3 == "X" and b2 == "X" and c1 == "X":
        print("Player 1 wins")
        continue_playing = False
        return continue_playing


def check_p2():
    global continue_playing
    if a1 == "0" and a2 == "0" and a3 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif b1 == "0" and b2 == "0" and b3 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif c1 == "0" and c2 == "0" and c3 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif a1 == "0" and b1 == "0" and c1 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif a2 == "0" and b2 == "0" and c2 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif a3 == "0" and b3 == "0" and c3 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif a1 == "0" and b2 == "0" and c3 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing
    elif a3 == "0" and b2 == "0" and c1 == "0":
        print("Player 2 wins")
        continue_playing = False
        return continue_playing


def display_board():
    board = f"""
   1   2   3
   --------- 
a  {a1} | {a2} | {a3}
   --------- 
b  {b1} | {b2} | {b3}
   --------- 
c  {c1} | {c2} | {c3}"""
    print(board)


def play_game():
    display_board()
    player1()
    check_p1()
    display_board()
    player2()
    check_p2()


while continue_playing:
    play_game()
