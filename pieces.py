import pygame
pygame.init()
import copy
from config import *

B = [b_king, b_queen, b_rook, b_knight, b_bishop, b_pawn];
W = [w_king, w_queen, w_rook, w_knight, w_bishop, w_pawn];


class Piece:
    def __init__(self, row, col, color):
        self.row = row;
        self.col = col;
        self.color = color;
        self.asleep = True;
        self.is_selected = False;
        self.is_king = False;
        self.is_pawn = False;
        self.in_transition = False;


    def draw(self, screen):
        if(self.color == 'w'):
            img = W[self.index];
        else:
            img = B[self.index];

        row, col = self.row, self.col;
        rect = img.get_rect();
        rect.center = (col*block + block//2, row*block + block//2);
        screen.blit(img, rect);


    def draw_piece_in_motion(self, screen, x, y):
        if(self.color == 'w'):
            img = W[self.index];
        else:
            img = B[self.index];

        rect = img.get_rect();
        rect.center = (x,y);
        screen.blit(img, rect);



    def upd_pos(self, row, col):
        self.row = row;
        self.col = col;
        self.is_selected = False;
        self.asleep = False;



    def get_moves(self, board):
        moves = self.get_valid_moves(board);

        if moves is None:
            return moves;

        safe_moves = [];

        for move in moves:
            if self.safe_move(board, move):
                safe_moves.append(move);

        # Castling
        if self.is_king:    
            if self.asleep and not self.in_check:
                if board[self.row][7]!=0 and board[self.row][7].asleep and (self.row,5) in safe_moves and board[self.row][6] == 0:
                    if self.safe_move(board, (self.row,6)):
                        safe_moves.append((self.row,6));

                if board[self.row][0]!=0 and board[self.row][0].asleep and (self.row,3) in safe_moves and board[self.row][2] == 0 and board[self.row][1] == 0:
                    if self.safe_move(board, (self.row,2)):
                        safe_moves.append((self.row,2)); 

        return safe_moves;

    

    def safe_move(self, board, move):
        r,c = move;
        temp_board = copy.deepcopy(board);

        if (r,c) != (self.row, self.col):
            temp_board[r][c] = self;
            temp_board[self.row][self.col] = 0;

        for i in range(8):
            for j in range(8):
                if temp_board[i][j] == 0 or temp_board[i][j].color == self.color:
                    continue;

                enemy_moves = temp_board[i][j].get_valid_moves(temp_board);
                if enemy_moves is None:
                    continue;
                
                for rr,cc in enemy_moves:
                    if temp_board[rr][cc] != 0 and temp_board[rr][cc].is_king:
                        return False;
        return True;



    def get_all_moves(self, board, color):
        all_moves = [];
        
        for i in range(8):
            for j in range(8):
                if board[i][j]!=0 and board[i][j].color == color:
                    all_moves.extend(board[i][j].get_moves(board));
        return all_moves;


    def gimme_moves(self, board, color):
        all_moves = [];
        
        for i in range(8):
            for j in range(8):
                if board[i][j]!=0 and board[i][j].color == color:
                    moves = board[i][j].get_moves(board);
                    if moves is not None:
                        for move in moves:
                            all_moves.append(((i,j) , move));
        return all_moves;



class king (Piece):
    index = 0;

    def __init__(self, row, col, color):
        super().__init__(row, col, color);
        self.is_king = True;
        self.in_check = False;


    def get_valid_moves(self, board):
        r,c = self.row, self.col;
        moves = [];
        dirr = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)];

        for p in dirr:
            rr,cc = r+p[0], c+p[1];
            if rr<0 or rr>7 or cc<0 or cc>7:
                continue;

            ob = board[rr][cc];
            
            if ob!=0 and  ob.color == self.color:
                continue;
            moves.append((rr,cc));

        return moves;

    
    def check_check(self, board):
        if self.safe_move(board, (self.row, self.col)):
            self.in_check = False;
        else:
            self.in_check = True;
        return;



class queen (Piece):
    index = 1;

    def get_valid_moves(self, board):
        r,c = self.row, self.col;
        moves = [];
        dir_r = [1,0,-1,0, 1,1,-1,-1];
        dir_c = [0,1,0,-1, 1,-1,1,-1];
        
        for k in range(8):
            for i in range(1,8):
                rr = r + dir_r[k]*i;
                cc = c + dir_c[k]*i;
                if rr<0 or rr>7 or cc<0 or cc>7:
                    break;

                ob = board[rr][cc];                

                if ob==0:
                    moves.append((rr,cc));
                elif ob.color != self.color:
                    moves.append((rr,cc));
                    break;
                else:
                    break;
        return moves;



class rook (Piece):
    index = 2;

    def get_valid_moves(self, board):
        r,c = self.row, self.col;
        moves = [];
        dir_r = [1,0,-1,0];
        dir_c = [0,1,0,-1];
        
        for k in range(4):
            for i in range(1,8):
                rr = r + dir_r[k]*i;
                cc = c + dir_c[k]*i;
                if rr<0 or rr>7 or cc<0 or cc>7:
                    break;
                
                ob = board[rr][cc];                

                if ob==0:
                    moves.append((rr,cc));
                elif ob.color != self.color:
                    moves.append((rr,cc));
                    break;
                else:
                    break;
        return moves;



class knight (Piece):
    index = 3;

    def get_valid_moves(self, board):
        r,c = self.row, self.col;
        moves = [];
        dirr = [(2,1), (2,-1), (1,2), (-1,2), (-2,1), (-2,-1), (1,-2), (-1,-2)];

        for p in dirr:
            rr,cc = r+p[0], c+p[1];
            if rr<0 or rr>7 or cc<0 or cc>7:
                continue;

            ob = board[rr][cc];
            
            if ob!=0 and ob.color == self.color:
                continue;
            moves.append((rr,cc));

        return moves;



class bishop (Piece):
    index = 4;

    def get_valid_moves(self, board):
        r,c = self.row, self.col;
        moves = [];
        dir_r = [1,1,-1,-1];
        dir_c = [1,-1,1,-1];
        
        for k in range(4):
            for i in range(1,8):
                rr = r + dir_r[k]*i;
                cc = c + dir_c[k]*i;
                if rr<0 or rr>7 or cc<0 or cc>7:
                    break;

                ob = board[rr][cc];                

                if ob==0:
                    moves.append((rr,cc));
                elif ob.color != self.color:
                    moves.append((rr,cc));
                    break;
                else:
                    break;
        return moves;



class pawn (Piece):
    index = 5;

    def __init__(self, row, col, color):
        super().__init__(row, col, color);
        self.is_pawn = True;
        self.start_loc = row;

    def get_valid_moves(self, board):
        r,c = self.row,self.col;
        moves = [];
        
        # straight 1
        z=1;
        if self.start_loc == 6:
            z = -1;
        
        if r+z >= 0 and r+z < 8 and board[r+z][c] == 0:
            moves.append((r+z,c));

        # diagonal
        c = c+1;
        if r+z >= 0 and r+z < 8 and c >= 0 and c < 8 and board[r+z][c] != 0 and board[r+z][c].color != self.color:
            moves.append((r+z,c));
        c = c-2;
        if r+z >= 0 and r+z < 8 and c >= 0 and c < 8 and board[r+z][c] != 0 and board[r+z][c].color != self.color:
            moves.append((r+z,c));

        # straight 2
        c = c+1;
        if self.asleep:
            if r+2*z >= 0 and r+2*z < 8 and board[r+2*z][c] == 0 and board[r+z][c] == 0:
                moves.append((r+2*z,c));

        return moves;


    def check_pawn(self):
        r = self.row;
        return r==0 or r==7;            



        