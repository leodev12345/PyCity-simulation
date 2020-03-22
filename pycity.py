import pygame
import time
import array as arr



pygame.init()

win = pygame.display.set_mode((850,700))
icon = pygame.image.load('images/icon.png')

pygame.display.set_caption("PyCity BETA 0.8")
pygame.display.set_icon(icon)
myfont = pygame.font.SysFont("arial", 20)

house = pygame.image.load('images/home.png')
house2 = pygame.image.load('images/home2.png')
house3 = pygame.image.load('images/home3.png')
park = pygame.image.load('images/park.png')
shop = pygame.image.load('images/shop.png')
factory = pygame.image.load('images/factory.png')
road = pygame.image.load('images/road.png')
picon = pygame.image.load('images/population.png')
micon = pygame.image.load('images/money.png')
print("====================")

help_manual = input("Village = 5*5 ,Town = 7*7 ,City = 10*10 ,Metropolis = 20*20,Megapolis = 25*25 Custom = custom*custom a\, Please enter your choise: ")


if help_manual == "Village":
    X = 5
    Y = 5
elif help_manual == "Town":
    X = 7
    Y = 7
elif help_manual == "City":
    X = 10
    Y = 10
elif help_manual == "Metropolis":
    X = 20
    Y = 20
elif help_manual == "Megapolis":
    X = 25
    Y = 25
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
print("Enter name for your city (14 char max):")
name=input()
if len(str(name))>14:
    print("Too long name! Please try again:")
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
landValue = 9
taxc=1000

width = round(display_width/X)
height = round(display_height/Y)
width2 = 50
height2 = 50
vel = 200
vel2 = 300
tax=0
house_big = pygame.transform.scale(house, (width-2,height-2))
house_big2 = pygame.transform.scale(house2, (width-2,height-2))
house_big3 = pygame.transform.scale(house3, (width-2,height-2))
park_big = pygame.transform.scale(park, (width-2,height-2))
shop_big = pygame.transform.scale(shop, (width-2,height-2))
factory_big = pygame.transform.scale(factory, (width-2,height-2))
road_big = pygame.transform.scale(road, (width-2,height-2))
run = True

win.fill((0, 0, 0))

for x in range(0,X*width,width):
    for y in range(0,Y*height,height):
        pygame.draw.rect(win, (86, 213, 47),(x, y, width-2, height-2))




pygame.draw.rect(win, (86, 213, 47),(700, 0, 150, 700))
win.blit(picon, (710, 90,20,20))
win.blit(micon, (710, 50,20,20))
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
    text = myfont.render(str(money), True, (0,0,0), (86, 213, 47))
    text2 = myfont.render(str(population), True, (0,0,0), (86, 213, 47))
    text3 = myfont.render(str(name), True, (0,0,0), (86, 213, 47))
    win.blit(text3, (720, 10))
    pygame.draw.line(win,(0,0,0),(700,35),(850,35))
    win.blit(text, (735, 50))
    win.blit(text2, (735, 90))
    tax=tax+1
    if tax==taxc:
        money=money+(income*10)
        taxc=taxc+1000
        
    if homes == homesc:
        homesc = homesc+10
        shopsc = shopsc+1
        pygame.draw.rect(win, (0, 0, 255),(720, 140, 20, 20))
    elif shops == shopsc:
        pygame.draw.rect(win, (86, 213, 47),(720, 140, 20, 20))
    elif shops>1 and shops == shopsc-1:
        pygame.draw.rect(win, (86, 213, 47),(720, 140, 20, 20))
    if shops!=0:
        if shopsc == shops:
            pygame.draw.rect(win, (139,69,19),(760, 140, 20, 20))
            shopsc = shopsc+1
        elif factories == shops:
            pygame.draw.rect(win, (86, 213, 47),(760, 140, 20, 20))
        elif shops>1 and shopsc-1 == shops:
            pygame.draw.rect(win, (139,69,19),(760, 140, 20, 20))


    if keys[pygame.K_r]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_r]:
            if (money>=100):
                if (m[stuppos][redpos] == 0):
                    if landValue>=0 and landValue<10:
                        win.blit(house_big, (stuppos*width, redpos*height,width-2, height-2))
                        money = money-100
                        population = population+10
                        homes = homes+1
                        income=income+1
                        m[stuppos][redpos] = 1
                    if landValue>=10 and landValue<20:
                        win.blit(house_big2, (stuppos*width, redpos*height,width-2, height-2))
                        money = money-200
                        population = population+100
                        homes = homes+1
                        landValue=landValue-1
                        m[stuppos][redpos] = 1
                        income=income+1
                    if landValue>=20:
                        win.blit(house_big3, (stuppos*width, redpos*height,width-2, height-2))
                        money = money-50
                        population = population+1000
                        homes = homes+1
                        landValue=landValue-1
                        m[stuppos][redpos] = 1
                        income=income+1
        
        
    if keys[pygame.K_c]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_c]:
            if (money>=100):
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
            if (money>=100):
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
            if (money>=10):
                if (m[stuppos][redpos] == 0):
                    win.blit(road_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-10
                    m[stuppos][redpos] = 4

    if keys[pygame.K_e]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_e]:
            if (money>=10):
                if (m[stuppos][redpos] == 1 or m[stuppos][redpos] == 2 or m[stuppos][redpos] == 3 or m[stuppos][redpos] == 4 or m[stuppos][redpos] == 5):
                    pygame.draw.rect(win, (0, 255, 0),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-10
                    m[stuppos][redpos] = 0
    
    if keys[pygame.K_p]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_p]:
            if (money>=50):
                if (m[stuppos][redpos] == 0):
                    win.blit(park_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-50
                    landValue=landValue+10
                    m[stuppos][redpos] = 4     






    


    
    pygame.display.update()

pygame.quit()            
