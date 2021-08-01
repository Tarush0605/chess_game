import pygame
pygame.init()
from pieces import rook
from pieces import knight
from pieces import bishop
from pieces import king
from pieces import queen
from pieces import pawn
from config import *


def draw_block(screen, row, col, color):
    x = col*block;
    y = row*block;
    pygame.draw.rect(screen, color, (x, y, block, block));


def draw_moves(screen, row, col, color, radius):
    x = col*block + block//2;
    y = row*block + block//2;
    pygame.draw.circle(screen, color, (x,y), radius);


def draw_square(screen, row, col, color):
    x = col*block;
    y = row*block;
    pygame.draw.rect(screen, color, (x, y, block, block), last_move_square_thickness);


def next_turn(chance):
    if chance == 'w':
        return 'b';
    else:
        return 'w';


def moveit_moveit(bb, screen, last_move, piece):
    timer = 0;
    (r1,c1) = last_move[0];
    (r2,c2) = last_move[1];
    piece.in_transition = True;
    
    while timer < animate_duration:
        timer += animation_speed;
        bb.draw(screen);
        y = (r1*block + block//2) + (r2-r1)*block*timer/animate_duration;
        x = (c1*block + block//2) + (c2-c1)*block*timer/animate_duration;
        piece.draw_piece_in_motion(screen, x, y);

        pygame.display.update();
        pygame.time.delay(animation_speed);
    
    piece.in_transition = False;
    return;



class Board:
    rows = cols = 8;

    def __init__(self, c2, c1):
        self.focus_square = (-1,-1);
        self.chance = 'w';
        self.board = [[0 for _ in range(self.rows)] for _ in range(self.cols)];
        self.last_move = ();

        self.board[0][0] = rook(0, 0, c1);
        self.board[0][1] = knight(0, 1, c1);
        self.board[0][2] = bishop(0, 2, c1);
        self.board[0][3] = queen(0, 3, c1);
        self.board[0][4] = king(0, 4, c1);
        self.board[0][5] = bishop(0, 5, c1);
        self.board[0][6] = knight(0, 6, c1);
        self.board[0][7] = rook(0, 7, c1);

        self.board[1][0] = pawn(1, 0, c1);
        self.board[1][1] = pawn(1, 1, c1);
        self.board[1][2] = pawn(1, 2, c1);
        self.board[1][3] = pawn(1, 3, c1);
        self.board[1][4] = pawn(1, 4, c1);
        self.board[1][5] = pawn(1, 5, c1);
        self.board[1][6] = pawn(1, 6, c1);
        self.board[1][7] = pawn(1, 7, c1);

        self.board[7][0] = rook(7, 0, c2);
        self.board[7][1] = knight(7, 1, c2);
        self.board[7][2] = bishop(7, 2, c2);
        self.board[7][3] = queen(7, 3, c2);
        self.board[7][4] = king(7, 4, c2);
        self.board[7][5] = bishop(7, 5, c2);
        self.board[7][6] = knight(7, 6, c2);
        self.board[7][7] = rook(7, 7, c2);

        self.board[6][0] = pawn(6, 0, c2);
        self.board[6][1] = pawn(6, 1, c2);
        self.board[6][2] = pawn(6, 2, c2);
        self.board[6][3] = pawn(6, 3, c2);
        self.board[6][4] = pawn(6, 4, c2);
        self.board[6][5] = pawn(6, 5, c2);
        self.board[6][6] = pawn(6, 6, c2);
        self.board[6][7] = pawn(6, 7, c2);

        self.k1 = self.board[0][4];
        self.k2 = self.board[7][4];



    def draw(self, screen):
        screen.fill(black);

        # Blocks
        for i in range(self.rows):
            for j in range(self.cols):
                if (i+j)%2 == 0:
                    color = light;
                else:
                    color = dark;

                if self.board[i][j] == 0 or self.board[i][j].in_transition:
                    draw_block(screen, i, j, color);
                    continue;
                
                # King in check
                if self.board[i][j].is_king:
                    if self.board[i][j].in_check:
                        color = in_check_color;

                # Focus square
                if (i,j) == self.focus_square:
                    color = focus_square_color;

                draw_block(screen, i, j, color);
                
                # Pieces   
                self.board[i][j].draw(screen);


        # All valid moves
        # all_moves = self.k1.get_all_moves(self.board, self.chance)
        
        # if all_moves is not None:
        #     for row,col in all_moves:
        #         draw_moves(screen, row, col, blue, 5);

        # Valid moves for focus square
        if self.focus_square != (-1,-1):
            r,c = self.focus_square;
            moves = self.board[r][c].get_moves(self.board);
            
            if moves is not None:
                for row,col in moves:
                    draw_moves(screen, row, col, focus_square_color, legal_move_radius);

        # Show Last Move
        if self.last_move is not None:
            for r,c in self.last_move:
                draw_square(screen, r, c, last_move_color);

        pygame.display.update();



    def select(self, row, col, screen):
        r,c = self.focus_square;
        if (r,c) == (-1,-1):
            if self.board[row][col] == 0:
                return;
            elif self.chance != self.board[row][col].color:
                return;
            else:
                self.board[row][col].is_selected = True;
                self.focus_square = (row,col);

        elif (r,c) == (row,col):
            self.board[r][c].is_selected = False;
            self.focus_square = (-1,-1);

        else:
            moves = self.board[r][c].get_moves(self.board);

            if (moves is None) or ((row,col) not in moves):
                self.board[r][c].is_selected = False;
                self.focus_square = (-1,-1);

                if self.board[row][col] == 0:
                    pass;
                elif self.board[row][col].color == self.board[r][c].color:
                    self.board[row][col].is_selected = True;
                    self.focus_square = (row,col);

            else:
                self.make_a_move([(r,c), (row,col)], screen);
        self.draw(screen);
                


    def make_a_move(self, move, screen):
        (r,c) = move[0];
        (row,col) = move[1];
        # Transition
        self.last_move = move;
        self.focus_square = (-1,-1);

        if transition_animation:
            self.board[r][c].in_transition = True;
            moveit_moveit(self, screen, self.last_move, self.board[r][c]);

        # Castling - rook movement
        if self.board[r][c].is_king and abs(col-c)==2:
            if(c>col):
                c1 = 0;
            else:
                c1 = 7;
            col1 = int((c+col)/2);
            self.board[row][col1] = self.board[row][c1];
            self.board[row][c1] = 0;
            self.board[row][col1].upd_pos(row,col1);                    
            
        # Normal
        self.board[row][col] = self.board[r][c];
        self.board[r][c] = 0;
        self.board[row][col].upd_pos(row,col);
        self.chance = next_turn(self.chance);

        # Pawn Promotion
        if self.board[row][col].is_pawn:
            if self.board[row][col].check_pawn():
                color = self.board[row][col].color;
                self.board[row][col] = queen(row, col, color);
        
        # Check if king is in check
        self.k1.check_check(self.board);
        self.k2.check_check(self.board);

        self.draw(screen);


    
    def checkmate(self):
        moves = self.k1.get_all_moves(self.board, self.chance);
        # print(moves);
        if moves is None or len(moves) == 0:
            if self.k1.color == self.chance:
                king = self.k1;
            else:
                king = self.k2;

            if king.in_check:
                return 1;
            else:
                return 2;

        c=0;
        for i in range(8):
            for j in range(8):
                if self.board[i][j]!=0:
                    c += 1;
        # print(c);
        if c==2:
            return 3;
        
        else:
            return 0;
    


                

                