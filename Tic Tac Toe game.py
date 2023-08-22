# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:50:51 2023

@author: hp
"""





class TicTacToe:
    def __init__(self,xState,zState):
        self.xState=xState
        self.zState=zState
        self.turn=1
    def make_board(self):
        zero='X'if self.xState[0] else ('O' if self.zState[0] else 0)
        one='X' if self.xState[1] else ('O' if self.zState[1] else 1)
        two='X' if self.xState[2] else ('O' if self.zState[2] else 2)
        three='X' if self.xState[3] else ('O' if self.zState[3] else 3)
        four='X' if self.xState[4] else ('O' if self.zState[4] else 4)
        five='X' if self.xState[5] else ('O' if self.zState[5] else 5)
        six='X' if self.xState[6] else ('O' if self.zState[6] else 6)
        seven='X' if self.xState[7] else ('O' if self.zState[7] else 7)
        eight='X' if self.xState[8] else ('O' if self.zState[8] else 8)
        
        
        
        print(f"{zero} | {one} | {two}")
        print(f"--|---|---")
        print(f"{three} | {four} | {five}")
        print(f"--|---|---")
        print(f"{six} | {seven} | {eight}")


    def play_game(self):
        while True:
            self.make_board()
            print("Welcome to Tic Tac Toe")
            if self.turn == 1:
                print("X's Chance.")
                x_value = int(input("Please enter value for xState: "))
                self.xState[x_value] = 1
            else:
                print("O's Chance.")
                z_value = int(input("Please enter value for zState: "))
                self.zState[z_value] = 1
            self.turn = 1 - self.turn

            if self.winner():# Check for a winner after each move
                break

    def winner(self):
        winning_positions = [[0, 1, 2], [0, 3, 6], [2, 5, 8], [6, 7, 8], [3, 4, 5], [0, 4, 8], [2, 4, 6], [1, 4, 7]]
        for win in winning_positions:
            if sum([self.xState[win[0]], self.xState[win[1]], self.xState[win[2]]]) == 3:
                print("X wins the match.")
                return True
            elif sum([self.zState[win[0]], self.zState[win[1]], self.zState[win[2]]]) == 3:
                print("O wins the match.")
                return True
        return False# no winner continue game

xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
obj = TicTacToe(xState, zState)
obj.play_game()
obj.make_board()
