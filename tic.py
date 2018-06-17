# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 14:56:56 2018

@author: saketh
Tic - Tac - Toe
"""

class game :
    
    board=[]
    over=0
    
    def __init__(self):
        self.board=[["-","-","-"],["-","-","-"],["-","-","-"]]
        self.over=1
        
    def disp_board(self) :
        i=0
        j=0
        while(i < 4) :
            print(" - - -"*3)
            if(i==3):
                break
            for j in range(0,3):
                print("| ",self.board[i][j]," ",end="")
            print("|")
            i=i+1;
                    
    def add(self, index, p) :
        try : 
           i=int(index[0])-1
           j=int(index[2])-1
           if i>2 or i<0 or j>2 or j<0 :
               return 0
        except ValueError :
            return 0
        except IndexError :
            return 0
        if(self.board[i][j] == "-") :            
            if(p==1) :
                self.board[i][j]="X"
                return 1

            else:
                self.board[i][j]="O"
                return 1
                
        else :
            print("Location already marked!")
            return 0
            
    def check_win(self) :
        for i in range(0,3) :
            j=0
            if(self.board[i][j]==self.board[i][j+1] and self.board[i][j]!='-' and self.board[i][j+1]!='-') :
                if(self.board[i][j+1]==self.board[i][j+2] and self.board[i][j+2]!='-') :
                    print("winner(row wise) : ",self.board[i][j])
                    self.over = 0
                else :
                    continue
            else :
                continue
        
        for j in range(0,3) :
            i=0
            if(self.board[i][j]==self.board[i+1][j] and self.board[i][j]!='-' and self.board[i+1][j]!='-') :
                if(self.board[i+1][j]==self.board[i+2][j] and self.board[i+2][j]!='-') :
                    print("winner(column wise): ",self.board[i][j])
                    self.over = 0
                else :
                    continue
            else :
                continue
    
        i=0
        while True :
            temp=self.board[i][j]
            i=i+1
            j=i
            if(i<3) :
                if(temp==self.board[i][j] and self.board[i][j]!="-") :
                    continue
                else:
                    break
            else :
                break
        if(i==3) :
            print("Winner(diagnol 1) : ",self.board[1][1])
            self.over = 0
        i=0
        j=2 
        while True :
            temp=self.board[i][j]
            i=i+1
            j=3-i-1
            if(i<3) :
                if(temp==self.board[i][j] and self.board[i][j]!="-") :
                    continue
                else:
                    break
            else :
                break
        if(i==3) :
            print("Winner(diagnol 2) : ",self.board[1][1]) 
            self.over = 0
            
g = game()
g.disp_board()
iter = 0
while g.over :
    
    while True :
        index = input("Player 1's turn. Enter : ")
        check = g.add(index,1)
        if(check == 1) :
            break
        
    g.disp_board()
    iter = iter + 1
    if(iter > 4) :
        g.check_win()
        if g.over==0 :
            break
    if(iter > 8) :
        g.over=0
        print("Tie!")
        break
    
    while True :
        index = input("Player 2's turn. Enter : ")
        check = g.add(index,2)
        if(check == 1) :
            break
    g.disp_board()
    iter = iter + 1
    if(iter > 4) :
        g.check_win()