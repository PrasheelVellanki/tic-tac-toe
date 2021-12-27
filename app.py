#Preparing modules
import pygame
import sys
import numpy as npy
from pygame.constants import K_r

pygame.init()



player = 1
game_state = False

screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Tic-Tac-Toe")

Line = (0, 68, 102)
Background = (0, 85, 128)
spacing = 55
screen.fill(Background)


def draw_grid():
    pygame.draw.line(screen, Line, (230,0), (230,700), 15)
    pygame.draw.line(screen, Line, (460,0), (460,700), 15)
    pygame.draw.line(screen, Line, (0,230), (700,230), 15)
    pygame.draw.line(screen, Line, (0,460), (700,460), 15)

draw_grid()

b_rows = 3
b_cols = 3
board = npy.zeros((b_rows,b_cols))

def board_mark(row, col, player):
    board[col][row] = player

def is_available(row,col):
    return not board[col][row] != 0

def is_full():
    for row in range(b_rows):
        for col in range(b_cols):
            if is_available(row,col):
                return False
    return True
            

def x_o():
    if player == 1:
        pygame.draw.line(screen, (0, 204, 204), (set_row * 230 + spacing , set_col * 230 + spacing ),  (set_row * 230 + 230 - spacing , set_col * 230 + 230 - spacing), 20)
        pygame.draw.line(screen, (0, 204, 204), (set_row * 230 + spacing , set_col * 230 + 230 - spacing ),  (set_row * 230 + 230 - spacing , set_col * 230 + spacing), 20)

    elif player == 2:
        pygame.draw.circle(screen, (153, 204, 255), (set_row * 230 + 115 , set_col * 230 + 115), 60, 15) #line width 10
        

def win_result(set_col, player):

    for col in range(b_cols):
        if player == board[0][col] and player == board[1][col] and player == board[2][col]:
            draw_vert(set_col, player)
            return True

    for row in range(b_rows):
        if player == board[row][0] and player == board[row][1] and player == board[row][2]:
            draw_horizontal(row,player)
            return True

    if player == board[2][0] and player == board[1][1] and player == board[0][2]:
        draw_asc(row,player)
        return True

    if player == board[0][0] and player == board[1][1] and player == board[2][2]:
        draw_desc(row,player)
        return True
 
def game_reset():
    screen.fill(Background)
    draw_grid()
    global player, game_state
    player = 1
    for row in range(b_rows):
        for col in range(b_cols):
            board[row][col] = 0
    game_state = False



def draw_vert(set_row, player):
    pygame.draw.line(screen, (0,0,1), (set_row*230 + 115, 15), (set_row*230 + 115, 685), 15)
def draw_horizontal(row,player):
    pygame.draw.line(screen, (0,0,1), (15, set_col*230 + 115), (685, set_col*230 + 115), 15)
def draw_asc(row,player):
    pygame.draw.line(screen, (0,0,1), (15, 685), (685, 15), 15)
def draw_desc(row,player):
    pygame.draw.line(screen, (0,0,1), (15, 15), (685, 685), 15)
    

#Main loop

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_state:
            clickX = event.pos[0]
            clickY = event.pos[1]

            set_row = clickX // 230
            set_col = clickY // 230

            if is_available(set_row, set_col):
                if player == 1:
                    board_mark(set_row, set_col, player)
                    x_o()
                    if win_result(set_row, player):
                        game_state = True
                    player = 2
                elif player == 2:
                    board_mark(set_row, set_col, player)
                    x_o()
                    if win_result(set_row, player):
                        game_state = True
                    player = 1
                    
        pygame.display.update()        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_reset()
        





    


    