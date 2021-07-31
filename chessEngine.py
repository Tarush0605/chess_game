import random
import time
from config import *

# order - king, queen, rook, knight, bishop, pawn
score = [100000, 900, 500, 300, 300, 100];

def call_the_expert(bb, screen):
    time.sleep(computer_delay_time);
    board = bb.board;
    color = bb.chance;
    all_moves = bb.k1.gimme_moves(board, color);

    if len(all_moves)==0:
        return;

    sc = 0;
    m = [];
    for move in all_moves:
        p = board[move[1][0]][move[1][1]];
        if p != 0:
            if score[p.index] > sc:
                m = [];
                sc = score[p.index];
                m.append(move);
            elif score[p.index] == sc:
                m.append(move);
        else:
            if sc==0:
                m.append(move);
    
    # print(m);
    move = random.choice(m);
    # print(move);

    bb.make_a_move(move, screen);
    return;

