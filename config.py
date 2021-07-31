import pygame
pygame.init()


# Options
p1 = 'w';
players = 0;
transition_animation = True;

# main game
screen_size = (screen_width, screen_height) = (640, 640);
block = screen_width//8;
tick_speed = 50;
font = pygame.font.Font('freesansbold.ttf', 80);


# Colors
red = (255, 0, 0);
light = (232, 235, 239);
dark = (125, 135, 150);
black = (0, 0, 0);
white = (255, 255, 255);
green = (144, 238, 144);
red = (255, 204, 203);
blue = (0, 0, 255);
purple = (128, 0, 128);


# animation/moves
valid_move_radius = 10;
last_move_square_thickness = 3;
animation_speed = 5;
animate_duration = 100;
computer_delay_time = 0;


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