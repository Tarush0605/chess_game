import pygame
pygame.init()


# initialise images
b_bishop = pygame.image.load('chess game/images/b_bishop.png');
b_pawn = pygame.image.load('chess game/images/b_pawn.png');
b_king = pygame.image.load('chess game/images/b_king.png');
b_queen = pygame.image.load('chess game/images/b_queen.png');
b_rook = pygame.image.load('chess game/images/b_rook.png');
b_knight = pygame.image.load('chess game/images/b_knight.png');
w_bishop = pygame.image.load('chess game/images/w_bishop.png');
w_pawn = pygame.image.load('chess game/images/w_pawn.png');
w_king = pygame.image.load('chess game/images/w_king.png');
w_queen = pygame.image.load('chess game/images/w_queen.png');
w_rook = pygame.image.load('chess game/images/w_rook.png');
w_knight = pygame.image.load('chess game/images/w_knight.png');


# Colors
light = (232, 235, 239);
dark = (125, 135, 150);
red = (255, 0, 0);
black = (0, 0, 0);
white = (255, 255, 255);
green = (144, 238, 144);
red = (255, 204, 203);
blue = (0, 0, 255);
purple = (128, 0, 128);


# Options
p1 = 'w';
players = 0;
transition_animation = False;


# Size
board_size = 640;
screen_size = (screen_width, screen_height) = (board_size, board_size);
block = board_size//8;


# Style
font = pygame.font.Font('freesansbold.ttf', 80);

gameover_color = black;
in_check_color = red;
focus_square_color = green;
last_move_color = purple;

last_move_square_thickness = 3;
legal_move_radius = 10;


# Speed
new_game_time_delay = 3000;
tick_speed = 50;


# animation/moves
animation_speed = 5;
animate_duration = 100;
computer_think_time = 0;


