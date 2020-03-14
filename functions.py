import pygame
from setting import *
from solver import *

pygame.font.init()
font = pygame.font.Font(None,40)






def draw_grid(grid,col_draw,row_draw):
    
    for row in range(9):
        for col in range(9):
            color =WHITE 
            
            
           
            pygame.draw.rect(screen,color,[(margin + width)*col+margin,(margin + height)*row +margin,width,height])
    if grid[row_draw][col_draw]==0:
        draw_current_rect(col_draw,row_draw)      
                
          

# restart and solve for draw test funtion

                
        
def draw_text(grid,enter,nr,col_draw,row_draw,restart,solve):
    for row in range(9):
        for col in range(9):
           
            text = font.render(str(grid[row][col]),True,BLACK)
            screen.blit(text,[(margin + width)*col+margin,(margin + height)*row +margin,width,height])
    
    if enter and grid[row_draw][col_draw]==0:
        #grid[row_draw][col_draw]=nr
        return False
   
            
           
        

def ver_poz_anterior(col,row):
    pos = pygame.mouse.get_pos()
    col_new = pos[0] // (width + margin)
    row_new = pos[1] // (height + margin) 
    if col_new == col and row_new == row:
        return 0
    else:
        return col_new,row_new
    
    
def draw_current_rect(col_draw,row_draw):
    pygame.draw.rect(screen,GREEN,[(margin + width)*col_draw+margin,(margin + height)*row_draw +margin,width,height])
    
    
    
def draw_restart():
    pygame.draw.rect(screen,GREEN,[50,450,100,50])
    text = font.render("Restart",True,BLACK)
    screen.blit(text,[50,450,100,50])
    return False    

def draw_solver():
    pygame.draw.rect(screen,GREEN,[200,450,105,50])
    text = font.render("  Solve",True,BLACK)
    screen.blit(text,[200,450,100,50])
    return False    

    
    
    
    