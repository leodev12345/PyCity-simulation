import pygame
import time
import array as arr


pygame.init()

win = pygame.display.set_mode((1000,1000))

pygame.display.set_caption("City Game")

help_manual = input("Village = 10*10 ,Town = 15*15 ,City = 25*25 , Custom = unknown*unknown a\, Please enter your choise: ")

if help_manual == "Village":
    X = 10
    Y = 10
elif help_manual == "Town":
    X = 15
    Y = 15
elif help_manual == "City":
    X = 25
    Y = 25
else:
    X =int(input())
    Y =int(input())

m = [[0] * Y for i  in range(X)]

display_width = 1000
display_height = 1000

Sum1 = int(0)
Sum2 = int(0)

m[0][0] = 0

money = 20000

width = round(display_width/X)
height = round(display_height/Y)
width2 = 50
height2 = 50
vel = 200
vel2 = 300
run = True

win.fill((0, 0, 0))

for x in range(0,X*width,width):
    for y in range(0,Y*height,height):
        pygame.draw.rect(win, (255, 0, 0),(x, y, width-2, height-2))




 

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    mouse = pygame.mouse.get_pos()
    pygame.display.update()
    keys = pygame.key.get_pressed()
    stuppos = round(mouse[0]//width)
    redpos = round(mouse[1]//height)
    
    if keys[pygame.K_r]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_r]:
            if (money>100):
                if (m[stuppos][redpos] == 0):
                    pygame.draw.rect(win, (0, 255, 0),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-100
                    print(money)
                    m[stuppos][redpos] = 1
                else:
                    print("You don't have enough money or that place is already filled with something")


    if keys[pygame.K_c]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_c]:
            if (money>100):
                if (m[stuppos][redpos] == 0):
                    pygame.draw.rect(win, (0, 0, 255),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-100
                    print(money)
                    m[stuppos][redpos] = 2
                else:
                    print("You don't have enough money or that place is already filled with something")

    if keys[pygame.K_i]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_i]:
            if (money>100):
                if (m[stuppos][redpos] == 0):
                    pygame.draw.rect(win, (255, 255, 0),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-100
                    print(money)
                    m[stuppos][redpos] = 3
                else:
                    print("You don't have enough money or that place is already filled with something")

    if keys[pygame.K_f]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_f]:
            if (money>400):
                if (m[stuppos][redpos] == 0):
                    pygame.draw.rect(win, (220, 50, 0),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-400
                    print(money)
                    m[stuppos][redpos] = 4
                else:
                    print("You don't have enough money or that place is already filled with something")

    if keys[pygame.K_p]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_p]:
            if (money>400):
                if (m[stuppos][redpos] == 0):
                    pygame.draw.rect(win, (120, 0, 200),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-400
                    print(money)
                    m[stuppos][redpos] = 5
                else:
                    print("You don't have enough money or that place is already filled with something")

    if keys[pygame.K_e]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_e]:
            if (money>10):
                if (m[stuppos][redpos] == 1 or m[stuppos][redpos] == 2 or m[stuppos][redpos] == 3 or m[stuppos][redpos] == 4 or m[stuppos][redpos] == 5):
                    pygame.draw.rect(win, (255, 0, 0),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-10
                    print(money)
                    m[stuppos][redpos] = 0
                else:
                    print("You don't have enough money or that place is already erased")
    
    if (m[stuppos][redpos] == 1):
        for z in range(0,60001,1):
            if (z==60000):
                money = money+10
                print(money)
     






    


    
    pygame.display.update()

pygame.quit()




