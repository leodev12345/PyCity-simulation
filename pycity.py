import pygame
import time
import array as arr



pygame.init()

win = pygame.display.set_mode((700,700))
icon = pygame.image.load('images/icon.png')

pygame.display.set_caption("PyCity BETA 0.2")
pygame.display.set_icon(icon)
myfont = pygame.font.SysFont("arial", 20)

house = pygame.image.load('images/home.png')
shop = pygame.image.load('images/shop.png')
factory = pygame.image.load('images/factory.png')
road = pygame.image.load('images/road.png')
print("====================")

help_manual = input("Village = 5*5 ,Town = 7*7 ,City = 10*10 , Custom = unknown*unknown a\, Please enter your choise: ")


if help_manual == "Village":
    X = 5
    Y = 5
elif help_manual == "Town":
    X = 7
    Y = 7
elif help_manual == "City":
    X = 10
    Y = 10
else:
    X =int(input("Enter x:"))
    Y =int(input("Enter y:"))
print("====================")
print("Chose diffculty Easy - start with 20000 money Medium - start with 10000 money Hard - start with 1200 money")
diffculty = input()
if diffculty=="Easy":
    money = 20000
elif diffculty=="Medium":
    money = 10000
elif diffculty=="Hard":
    money = 1200
print("====================")
print("Enter name: for your city:")
name=input()

m = [[0] * Y for i  in range(X)]

display_width = 700
display_height = 700

Sum1 = int(0)
Sum2 = int(0)

m[0][0] = 0

population = 0
homes = 0
homesc = 10
shopsc = 0
shops = 0
income = 0
factories = 0

width = round(display_width/X)
height = round(display_height/Y)
width2 = 50
height2 = 50
vel = 200
vel2 = 300
house_big = pygame.transform.scale(house, (width-2,height-2))
shop_big = pygame.transform.scale(shop, (width-2,height-2))
factory_big = pygame.transform.scale(factory, (width-2,height-2))
road_big = pygame.transform.scale(road, (width-2,height-2))
run = True

win.fill((0, 0, 0))

for x in range(0,X*width,width):
    for y in range(0,Y*height,height):
        pygame.draw.rect(win, (0, 255, 0),(x, y, width-2, height-2))




 
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
    text = myfont.render("Money:" + str(money), True, (255, 255, 255), (0, 0, 0))
    text2 = myfont.render("Population:" + str(population), True, (255, 255, 255), (0, 0, 0))
    text3 = myfont.render(str(name), True, (255, 255, 255), (0, 0, 0))
    win.blit(text, (10, 10))
    win.blit(text2, (150, 10))
    win.blit(text3, (600, 10))
    money=money+(1*income)
    if homes == homesc:
        homesc = homesc+10
        shopsc = shopsc+1
        pygame.draw.rect(win, (0, 0, 255),(300, 10, 20, 20))
    elif shops == shopsc:
        pygame.draw.rect(win, (0, 255, 0),(300, 10, 20, 20))
    elif shops>1 and shops == shopsc-1:
        pygame.draw.rect(win, (0, 255, 0),(300, 10, 20, 20))
    if shops!=0:
        if shopsc == shops:
            pygame.draw.rect(win, (139,69,19),(350, 10, 20, 20))
            shopsc = shopsc+1
        elif factories == shops:
            pygame.draw.rect(win, (0, 255, 0),(350, 10, 20, 20))
        elif shops>1 and shopsc-1 == shops:
            pygame.draw.rect(win, (139,69,19),(350, 10, 20, 20))

    if keys[pygame.K_r]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_r]:
            if (money>100):
                if (m[stuppos][redpos] == 0):
                    win.blit(house_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-100
                    population = population+10
                    homes = homes+1
                    m[stuppos][redpos] = 1
        
    if keys[pygame.K_c]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_c]:
            if (money>100):
                if (m[stuppos][redpos] == 0):
                    win.blit(shop_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-100
                    shops = shops+1
                    income=income+1
                    m[stuppos][redpos] = 2

    if keys[pygame.K_i]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_i]:
            if (money>100):
                if (m[stuppos][redpos] == 0):
                    win.blit(factory_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-100
                    factories = factories+1
                    income=income+1
                    m[stuppos][redpos] = 3

    if keys[pygame.K_o]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_o]:
            if (money>10):
                if (m[stuppos][redpos] == 0):
                    win.blit(road_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-10
                    m[stuppos][redpos] = 4

    if keys[pygame.K_e]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_e]:
            if (money>10):
                if (m[stuppos][redpos] == 1 or m[stuppos][redpos] == 2 or m[stuppos][redpos] == 3 or m[stuppos][redpos] == 4 or m[stuppos][redpos] == 5):
                    pygame.draw.rect(win, (0, 255, 0),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-10
                    m[stuppos][redpos] = 0
    
     






    


    
    pygame.display.update()

pygame.quit()            
