import pygame
from setting import *



def are0(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j]==0:
                return True
            
    return False


def find0(grid,l):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j]==0:
                l[0]=i 
                l[1]=j
                return True
    
    return False 




def randvalid(grid,i,j,el):
    for e in range(0,len(grid)):
            if grid[i][e] == el:
                return False
            
    return True

def coloanavalida(grid,i,j,el):

    for e in range(0,len(grid)):
            if grid[e][j]==el:
                return False
    
    return True 

def patratelvalid(grid,i,j,el):
    for k in range(0,3): 
        for h in range(0,3): 
            if(grid[k+i][h+j] == el): 
                return False
    return True


def cifravalida(grid,i,j,el):
    return randvalid(grid, i, j,el) and coloanavalida(grid, i, j,el) and patratelvalid(grid, i - i%3, j - j%3, el)
   
    
def afisare(grid):
    for elem in grid:
        print(elem)



def bkt(grid):
   
        
    l=[0,0]
    if not find0(grid,l):
        return True
        
    else:
        i = l[0]
        j = l[1]
        
        for el in range(1,10):
            if cifravalida(grid, i, j, el):
                grid[i][j] = el
                if bkt(grid):
                    return True
                
                grid[i][j]=0
                
    return False
            
    
    """
    if not are0(grid):
        afisare(grid)
        print("\n")
        print("\n")
    
    else:
        if are0(grid):
            i,j = find0(grid)
            for el in range(1,10):
                
                
                if cifravalida(grid,i,j,el):
                    print(grid)
                    grid[i][j] = el
                    bkt(grid[:])
                     
    """



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

bkt(copie_grid)
bkt(grid)
for row in range(9):
    for col in range(9):
        print(str(grid[row][col]), end = " ")
    print(" ")
print(" ")
print(" ")    
for row in range(9):
    for col in range(9):
        print(str(copie_grid[row][col]), end = " ")
    print(" ")

    
    

