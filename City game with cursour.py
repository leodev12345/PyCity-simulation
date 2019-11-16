import pygame
import time
pygame.init()

win = pygame.display.set_mode((1000,1000))

pygame.display.set_caption("City Game")



x1 = 200
y1 = 100
x2 = 200
y2 = 100
x3 = 400
y3 = 100
x4 = 600
y4 = 100
x5 = 800
y5 = 100

money = 500



x = 200
y = 100

width = 100
height = 100
width2 = 50
height2 = 50
vel = 200
vel2 = 300
run = True

win.fill((0, 0, 0))
pygame.draw.rect(win, (255, 0, 0),(x1, y1, width, height))
pygame.draw.rect(win, (255, 0, 0),(x3, y3, width, height))
pygame.draw.rect(win, (255, 0, 0),(x4, y4, width, height))
pygame.draw.rect(win, (255, 0, 0),(x5, y5, width, height))
 
    
pygame.draw.rect(win, (255, 0, 0),(200, 300, width, height))
pygame.draw.rect(win, (255, 0, 0),(400, 300, width, height))
pygame.draw.rect(win, (255, 0, 0),(600, 300, width, height))
pygame.draw.rect(win, (255, 0, 0),(800, 300, width, height))

    

pygame.draw.rect(win, (255, 0, 0),(200, 500, width, height))
pygame.draw.rect(win, (255, 0, 0),(400, 500, width, height))
pygame.draw.rect(win, (255, 0, 0),(600, 500, width, height))
pygame.draw.rect(win, (255, 0, 0),(800, 500, width, height))

pygame.draw.rect(win, (255, 0, 0),(200, 700, width, height))
pygame.draw.rect(win, (255, 0, 0),(400, 700, width, height))
pygame.draw.rect(win, (255, 0, 0),(600, 700, width, height))
pygame.draw.rect(win, (255, 0, 0),(800, 700, width, height))





while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



        

    mouse = pygame.mouse.get_pos()
    pygame.display.update()
    keys = pygame.key.get_pressed()


   
    if x1+width > mouse[0] > x1 and y1+height > mouse[1] > y1:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(x1, y1, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(x1, y1, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(x1, y1, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(x1, y1, width, height))
            
        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(x1, y1, width, height))
        

    if x3+width > mouse[0] > x3 and y3+height > mouse[1] > y3:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(x3, y3, width, height))
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(x3, y3, width, height))
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(x3, y3, width, height))
        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(x3, y3, width, height))
        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(x3, y3, width, height))
        

    if x5+width > mouse[0] > x5 and y5+height > mouse[1] > y5:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(x5, y5, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(x5, y5, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(x5, y5, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(x5, y5, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(x5, y5, width, height))
        

            
    if x4+width > mouse[0] > x4 and y4+height > mouse[1] > y4:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(x4, y4, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(x4, y4, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(x4, y4, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(x4, y4, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(x4, y4, width, height))
        


    if 200+width > mouse[0] > 200 and 300+height > mouse[1] > 300:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(200, 300, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(200, 300, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(200, 300, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(200, 300, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(200, 300, width, height))
        

    if 400+width > mouse[0] > 400 and 300+height > mouse[1] > 300:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(400, 300, width, height))
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(400, 300, width, height))
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(400, 300, width, height))
        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(400, 300, width, height))
        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(400, 300, width, height))
        

    if 600+width > mouse[0] > 600 and 300+height > mouse[1] > 300:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(600, 300, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(600, 300, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(600, 300, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(600, 300, width, height))
            
        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(600, 300, width, height))
        
            
    if 800+width > mouse[0] > 800 and 300+height > mouse[1] > 300:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(800, 300, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(800, 300, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(800, 300, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(800, 300, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(800, 300, width, height))
        
   


    if 200+width > mouse[0] > 200 and 500+height > mouse[1] > 500:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(200, 500, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(200, 500, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(200, 500, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(200, 500, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(200, 500, width, height))
        

    if 400+width > mouse[0] > 400 and 500+height > mouse[1] > 500:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(400, 500, width, height))
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(400, 500, width, height))
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(400, 500, width, height))
        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(400, 500, width, height))
        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(400, 500, width, height))
        

    if 600+width > mouse[0] > 600 and 500+height > mouse[1] > 500:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(600, 500, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(600, 500, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(600, 500, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(600, 500, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(600, 500, width, height))
        
            
    if 800+width > mouse[0] > 800 and 500+height > mouse[1] > 500:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(800, 500, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(800, 500, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(800, 500, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(800, 500, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(800, 500, width, height))
        
   


    if 200+width > mouse[0] > 200 and 700+height > mouse[1] > 700:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(200, 700, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(200, 700, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(200, 700, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(200, 700, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(200, 700, width, height))
        

    if 400+width > mouse[0] > 400 and 700+height > mouse[1] > 700:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(400, 700, width, height))
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(400, 700, width, height))
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(400, 700, width, height))
        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(400, 700, width, height))
        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(400, 700, width, height))
        
        

    if 600+width > mouse[0] > 600 and 700+height > mouse[1] > 700:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(600, 700, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(600, 700, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(600, 700, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(600, 700, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(600, 700, width, height))
        
            
    if 800+width > mouse[0] > 800 and 700+height > mouse[1] > 700:
        if keys[pygame.K_r]:
            pygame.draw.rect(win, (0, 255, 0),(800, 700, width, height))    
           
        if keys[pygame.K_c]:
            pygame.draw.rect(win, (0, 0, 255),(800, 700, width, height))
          
        if keys[pygame.K_p]:
            pygame.draw.rect(win, (100, 0, 255),(800, 700, width, height))

        if keys[pygame.K_f]:
            pygame.draw.rect(win, (120, 0, 0),(800, 700, width, height))

        if keys[pygame.K_i]:
            pygame.draw.rect(win, (255, 255, 0),(800, 700, width, height))
        

    if 800 or 600 or 400 or 200+width > mouse[0] > 800 and 700 or 500 or 300 or 100+height > mouse[1] > 700:
        if keys[pygame.K_r]:
            print(money-10)

    








    pygame.display.update()





pygame.quit()
