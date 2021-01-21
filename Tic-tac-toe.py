# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:27:19 2020

@author: ranas
"""
board=[" " for x in range(10)]
def printBoard(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |   ")
    print("-----------")
    
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |   ")
    print("-----------")
    
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |   ")


def insertLetter(letter,pos):
    board[pos]=letter
    
def spaceIsFree(pos):
    return board[pos]==" "

def isBoardFull(board):
    if board.count(" ")>1:
        return False
    else:
        return True
    
def isWinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l) or (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or (b[2]==l and b[5]==l and b[8]==l) or (b[3]==l and b[6]==l and b[9]==l) or 
    (b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l))
    
def playerMove():
    run=True
    while (run):
        move=input("Enter the position(1-9):")
        try:
            move=int(move)
            if (move>0 and move<10):
                if spaceIsFree(move):
                    run=False
                    insertLetter("X",move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Enter a valid character!")
        except:
            print("Please type a number")
            
def comMove():
    possibleMoves=[x for x, letter in enumerate(board) if letter==" " and x!=0]
    move=0
    if len(possibleMoves)!=0:
        for let in ["O","X"]:
            for i in possibleMoves:
                boardCopy=board[:]
                boardCopy[i]=let
                if isWinner(boardCopy,let):
                    move=i
                    return move
        cornersOpen=[]
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
        
        if len(cornersOpen)>0:
            move=selectRandom(cornersOpen)
            return move
        
    
        if 5 in possibleMoves:
            move=5
            return move
        
        edgesOpen=[]
        for i in possibleMoves:
            for i in [2,4,6,8]:
                edgesOpen.append(i)
                
        if len(edgesOpen)>0:
            move=selectRandom(edgesOpen)
    else:
        return move
        
def selectRandom(list):
    import random
    ln=len(list)
    r=random.randrange(0,ln)
    return list[r]

def main():
    print("Welcome to the game!")
    printBoard(board)
    while not(isBoardFull(board)):
    
        if not(isWinner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("You lose")
            break
        if not(isWinner(board,"X")):
            move=comMove()
            if move==0:
                print("")
            else:
                insertLetter("O",move)
                print("Computer placed an O on position: ",move)
                printBoard(board)
        else:
            print("You win!!")
            break
    if isBoardFull(board):
        print("Tie game")
        
        
while True:
    main()
    x=input("Do you want to play again?(Y/N)")
    if x=='Y':
        board=[" " for x in range(10)]
        print("-----------------")
        main()
    elif x=='N':
        break
    else:
        print("Wrong input!")
        print("Game crashing.......")
        break
                
    
