import sys
import random
from array import *

tic_table = [[1,2,3],[4,5,6],[7,8,9]]

def print_tic_table():
    for x in tic_table:
        for y in x:
            print (y, end = " ")
        print()  
    print("------------")  


def update_tic_table(pos, val):
    p = pos
    for x in range(0,3):
        for y in range(0,3):
            if int(p) == tic_table[x][y]:
                tic_table[x][y] = val    
           
def main_loop():
    player = ["X","O"]
    win = False
    turn = 0

#randomly pick first player
    n = random.randint(0, 1)
    
    print("Tic Tac Tok game")
    while win != True:
        
        print(player[n] + " player's turn, Enter position number: ")
        input = sys.stdin.readline()
        
        print("Playing ------")  

        update_tic_table(input,player[n])
 
        if check_winner(player[n]) == True:
            win = True
            print_tic_table()
            break

#switch turn
        if n == 0:
            n = 1
        else:
            n = 0 

        print_tic_table()
        turn = turn + 1

#no one wins        
        if turn > 8:
            win = True
            break


def check_winner(val):
    T = tic_table
    
    if (T[0][0] == val and T[0][1] == val and T[0][2] == val) or \
        (T[1][0] == val and T[1][1] == val and T[1][2] == val) or \
        (T[2][0] == val and T[2][1] == val and T[2][2] == val):
        print("Across done! Winner is " + val)
        #T[0][0] = '\u0336'.join(T[0][0]) + '\u0336'
        return True
    if (T[0][0] == val and T[1][0] == val and T[2][0] == val) or \
        (T[0][1] == val and T[1][1] == val and T[2][1] == val) or \
        (T[0][2] == val and T[1][2] == val and T[2][2] == val):
        print("Down done! Winner is " + val)
        return True
    if (T[0][0] == val and T[1][1] == val and T[2][2] == val) or \
        (T[0][2] == val and T[1][1] == val and T[2][0] == val):
        print("Diagonal done! Winner is " + val)
        return True
    
print_tic_table()
main_loop()



