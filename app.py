import pygame
from setting import *
from functions import *
from solver import *


x=0
nr=0
solve = False
restart = False
done = False
enter = False
win = True

col_draw=0
row_draw =0

# clock
clock = pygame.time.Clock()


grid=       [[3,0,6,5,0,8,4,0,0], 
             [5,2,0,0,0,0,0,0,0], 
             [0,8,7,0,0,0,0,3,1], 
             [0,0,3,0,1,0,0,8,0], 
             [9,0,0,8,6,3,0,0,5], 
             [0,5,0,0,9,0,6,0,0], 
             [1,3,0,0,0,0,2,5,0], 
             [0,0,0,0,0,0,0,7,4], 
             [0,0,5,2,0,6,3,0,0]]


copie_grid= [[3,0,6,5,0,8,4,0,0], 
             [5,2,0,0,0,0,0,0,0], 
             [0,8,7,0,0,0,0,3,1], 
             [0,0,3,0,1,0,0,8,0], 
             [9,0,0,8,6,3,0,0,5], 
             [0,5,0,0,9,0,6,0,0], 
             [1,3,0,0,0,0,2,5,0], 
             [0,0,0,0,0,0,0,7,4], 
             [0,0,5,2,0,6,3,0,0]]


solved_grid = [[3,0,6,5,0,8,4,0,0], 
             [5,2,0,0,0,0,0,0,0], 
             [0,8,7,0,0,0,0,3,1], 
             [0,0,3,0,1,0,0,8,0], 
             [9,0,0,8,6,3,0,0,5], 
             [0,5,0,0,9,0,6,0,0], 
             [1,3,0,0,0,0,2,5,0], 
             [0,0,0,0,0,0,0,7,4], 
             [0,0,5,2,0,6,3,0,0]]


bkt(solved_grid)


pygame.init()


# >>>>> main  program >>>>>>>>>>
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # if i press exit program stops
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_v:
                done = True
            if event.key ==pygame.K_RETURN:
                enter= True
            if event.key ==pygame.K_1:
                nr=1
                print(nr)
            if event.key ==pygame.K_2:
                nr=2
                print(nr)
            if event.key ==pygame.K_3:
                nr=3
                print(nr)
            if event.key ==pygame.K_4:
                nr=4
            
            if event.key ==pygame.K_5:
                nr=5
            
            if event.key ==pygame.K_6:
                nr=6
            
            if event.key ==pygame.K_7:
                nr=7
            
            if event.key ==pygame.K_8:
                nr=8
            
            if event.key ==pygame.K_9:
                nr=9
                
            if event.key == pygame.K_s:
                solve = True
                print(grid)
                grid = copie_grid
                print(grid)
                bkt(grid)
                
            if event.key ==pygame.K_p:
                print(grid)
                # to shop current grid
            
            
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            if ((pos[0]>0 and pos[0]<400) and (pos[1]>0 and pos[1]<400)):
                col_draw = pos[0] // (width + margin)
                row_draw = pos[1] // (height + margin)
                
                if ver_poz_anterior(col_draw, row_draw)==0: # daca a mai fost inainte apasat
                    pass
                else:
                    col_draw,row_draw = ver_poz_anterior(col_draw, row_draw)
                print("click", pos,"coordinates: ",row_draw,col_draw, " val->",str(grid[row_draw][col_draw]));
            elif (pos[0]>50 and pos[0]<150) and (pos[1]>450 and pos[1]<500):
                restart=True
                #print(grid)
               
            
            elif (pos[0]>200 and pos[0]<300) and (pos[1]>450 and pos[1]<500):
                solve=True
                print(grid)
                
    #logic 
    
    
       
    #draaw  # order is important
    screen.fill(BLACK) # screen is white at first
    
    #draw the grid 
    draw_grid(grid,col_draw,row_draw)
    draw_restart()
    draw_solver()
    
    if draw_text(grid,enter,nr,col_draw,row_draw,restart,solve)==False:
        enter = False
        print(solved_grid[row_draw][col_draw])
        print(grid[row_draw][col_draw])
        if solved_grid[row_draw][col_draw] == nr:
            grid[row_draw][col_draw]=nr
            print("yep")
            font = pygame.font.Font(None,150)
            text_win = font.render("+",True,GREEN)
            screen.blit(text_win,[450,30,200,100])
            x=x+20;
        else:
            print("nope")
            font = pygame.font.Font(None,100)
            text_win = font.render("X",True,RED)
            screen.blit(text_win,[450,30,200,100])
            x=x+20;
    
    
    if restart ==True:
    
        for row in range(9):
            for col in range(9):
                grid[row][col] = copie_grid[row][col]
        
        
        restart = False
        print(grid)
    
    if solve ==True:
        bkt(grid)
        solve =False
    
    
    
    win = True
    for row in range(9):
        for col in range(9):
            if grid[row][col]!=solved_grid[row][col]:
                win =False
    
 
    if win ==True:
        pygame.draw.rect(screen, WHITE,[410,100,150,75])
        font = pygame.font.Font(None,30)
        text_win = font.render("WINNER",True,BLACK)
        screen.blit(text_win,[435,120,200,100])
   
    # after drawing
    
    clock.tick(30);  # frame rate
    pygame.display.flip() # update the screen 
     
     

            

pygame.quit()   