import pygame
pygame.init()
from board import Board
from chessEngine import call_the_expert
from config import *


# Initialise Screen
screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption('Chess Game');


# Initialise Chessboard
p2 = 'w';
if p1 == 'w': p2 = 'b';


def main():
    bb = Board(p1,p2);
    bb.draw(screen);
    txt = "";

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                pygame.quit();
                exit();

            if event.type == pygame.MOUSEBUTTONDOWN:
                if players > 0:
                    x,y = pygame.mouse.get_pos();
                    row = y // block;
                    col = x // block;
                    bb.select(row, col, screen);

        st = bb.checkmate();
        if st>0:           
            if st == 1:
                txt = "CHECKMATE";
            elif st == 2:
                txt = "STALEMATE";
            elif st == 3:
                txt = "DRAW";

            txt = font.render(txt, True, gameover_color);
            rect = txt.get_rect();
            rect.center = (screen_width//2, screen_height//2);
            screen.blit(txt, rect);
            pygame.display.update();
            pygame.time.delay(new_game_time_delay);
            main();
            # pygame.quit();
            # exit();
                
        if players==1 and bb.chance == p2:
            call_the_expert(bb, screen);
        elif players==0:
            call_the_expert(bb, screen);

        pygame.time.delay(tick_speed);


main();


# Things To Do:
# Add start page - choose white/black
# Add en passant move
# Add end page - ask to play again or quit
# Make pieces rescalable to change size of board easily
# if no capture for 50 moves - draw
# MAKE A FUCKING CHESS ENGINE ALREADY GODDAMMIT





            



