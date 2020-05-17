import pygame
import time
import moneyupdate
import array as arr
import math



pygame.init()

win = pygame.display.set_mode((850,700))
icon = pygame.image.load('images/icon.png')

pygame.display.set_caption("PyCity BETA 1.5")
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
fire = pygame.image.load('images/fire.png')
police = pygame.image.load('images/police.png')
hospital = pygame.image.load('images/hospital.png')
prison = pygame.image.load('images/prison.png')
cityhall = pygame.image.load('images/cityhall.png')
mountain = pygame.image.load('images/mountain.png')
forest = pygame.image.load('images/forest.png')
lake = pygame.image.load('images/lake.png')
print("====================")

help_manual = input("Village = 5*5 ,Town = 7*7 ,City = 10*10 ,Metropolis = 20*20,Megapolis = 50*50 Custom = custom*custom a\, Please enter your choise: ")


if help_manual == "Village" or help_manual == "village" :
    X = 5
    Y = 5
elif help_manual == "Town" or help_manual == "town":
    X = 7
    Y = 7
elif help_manual == "City" or help_manual == "city":
    X = 10
    Y = 10
elif help_manual == "Metropolis" or help_manual == "metropolis":
    X = 20
    Y = 20
elif help_manual == "Megapolis" or help_manual == "megapolis":
    X = 50
    Y = 50
else:
    X =int(input("Enter x:"))
    Y =int(input("Enter y:"))
print("====================")
print("Chose diffculty Easy - start with 20000 money Medium - start with 10000 money Hard - start with 1200 money, Extreme - start with 100 money, Free start with infinite money")
diffculty = input()
if diffculty=="Easy" or diffculty=="easy":
    money = 20000
elif diffculty=="Medium" or diffculty=="medium":
    money = 10000
elif diffculty=="Hard" or diffculty=="hard":
    money = 1200
elif diffculty=="Extreme" or diffculty=="extreme":
    money = 100
elif diffculty=="Dev" or diffculty=="dev":
    money = 1000000000000000000000
elif diffculty=="Free" or diffculty=="free":
    money=0
    money=float(money)
    money=math.inf
    
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

edit = False
population = 0
homes = 0
homesf = 0
homesp = 0
homesc = 10
homescf = 20
homescp =20
shopsc = 0
shops = 0
income = 0
factories = 0
landValue = 9
taxc=1000
hospitals=0
pstations=0
fstations=0
policec=0
firec=0
hosc =  0
populationc=50000
prisons=0
prisonc=0
pstationsc=5
cityhalls=0
rate=0.01

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
fire_big = pygame.transform.scale(fire, (width-2,height-2))
police_big = pygame.transform.scale(police, (width-2,height-2))
hospital_big = pygame.transform.scale(hospital, (width-2,height-2))
prison_big = pygame.transform.scale(prison, (width-2,height-2))
cityhall_big = pygame.transform.scale(cityhall, (width-2,height-2))
mountain_big = pygame.transform.scale(mountain, (width-2,height-2))
forest_big = pygame.transform.scale(forest, (width-2,height-2))
lake_big = pygame.transform.scale(lake, (width-2,height-2))

run = True

win.fill((0, 0, 0))

for x in range(0,X*width,width):
    for y in range(0,Y*height,height):
        pygame.draw.rect(win, (86, 213, 47),(x, y, width-2, height-2))




pygame.draw.rect(win, (86, 213, 47),(700, 0, 150, 700))
win.blit(picon, (710, 90,20,20))
win.blit(micon, (710, 50,20,20))
text7 = myfont.render("Edit mode OFF", True, (255,0,0), (86, 213, 47))
win.blit(text7, (710, 280))
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    moneyupdate.update()
    moneyupdate.umoney=money
    moneyupdate.up=population
    moneyupdate.mwin=win
    mouse = pygame.mouse.get_pos()
    pygame.display.update()
    keys = pygame.key.get_pressed()
    stuppos = round(mouse[0]//width)
    redpos = round(mouse[1]//height)
    if diffculty=="free" or diffculty=="Free":
        text = myfont.render(str(money), True, (0,0,0), (86, 213, 47))
    elif diffculty!="free" or diffculty!="Free":
        text = myfont.render(str(int(money)), True, (0,0,0), (86, 213, 47))
    text2 = myfont.render(str(population), True, (0,0,0), (86, 213, 47))
    text3 = myfont.render(str(name), True, (0,0,0), (86, 213, 47))
    text4 = myfont.render(str(int(rate*100))+"%", True, (0,0,0), (86, 213, 47))
    text5 = myfont.render("Tax rate:", True, (0,0,0), (86, 213, 47))
    text6 = myfont.render("Edit mode ON  ", True, (34,139,34), (86, 213, 47))
    text7 = myfont.render("Edit mode OFF", True, (255,0,0), (86, 213, 47))
    win.blit(text3, (720, 10))
    pygame.draw.line(win,(0,0,0),(700,35),(850,35))
    win.blit(text, (735, 50))
    win.blit(text2, (735, 90))
    if cityhalls>0:
        win.blit(text4, (725, 250))
        win.blit(text5, (715, 230))
    tax=tax+1
    if cityhalls>0:
        if keys[pygame.K_LEFT] and rate>=0.0:
            rate=rate-0.01
        if keys[pygame.K_RIGHT] and rate<=0.20:
            rate=rate+0.01

    if population>=populationc and population<populationc+1000:
        populationc = populationc+50000
        hosc = hosc+1
        pygame.draw.rect(win, (255, 255, 255),(760, 170, 20, 20))
    elif hosc == hospitals:
        pygame.draw.rect(win, (86, 213, 47),(760, 170, 20, 20))

    if pstations == pstationsc:
        pstationsc = pstationsc+5
        prisonc = prisonc+1
        pygame.draw.rect(win, (90, 87, 87),(800, 170, 20, 20))
    elif prisons == prisonc:
        pygame.draw.rect(win, (86, 213, 47),(800, 170, 20, 20))




    if homesf == homescf:
        homescf = homescf+20
        firec = firec+1
        pygame.draw.rect(win, (255, 0, 0),(800, 140, 20, 20))
    elif fstations == firec:
        pygame.draw.rect(win, (86, 213, 47),(800, 140, 20, 20))


    if homesp == homescp:
        homescp = homescp+20
        policec = policec+1
        pygame.draw.rect(win, (0, 247, 255),(720, 170, 20, 20))
    elif pstations == policec:
        pygame.draw.rect(win, (86, 213, 47),(720, 170, 20, 20))

    if tax==taxc:
        money=money+rate*1000*income
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
        elif factories >= shops:
            pygame.draw.rect(win, (86, 213, 47),(760, 140, 20, 20))
        elif shops>1 and shopsc-1 == shops:
            pygame.draw.rect(win, (139,69,19),(760, 140, 20, 20))


    if keys[pygame.K_UP] and edit==False:
        edit=True
        win.blit(text6, (710, 280))
    if keys[pygame.K_DOWN] and edit==True:
        edit=False
        win.blit(text7, (710, 280))

    if keys[pygame.K_r]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_r]:
            if (money>=100):
                if (m[stuppos][redpos] == 0 or m[stuppos][redpos] == 17):
                    if landValue>=0 and landValue<10:
                        win.blit(house_big, (stuppos*width, redpos*height,width-2, height-2))
                        money = money-100
                        population = population+10
                        homes = homes+1
                        homesf = homesf+1
                        homesp = homesp+1
                        income=income+1
                        m[stuppos][redpos] = 6
                    if landValue>=10 and landValue<20 and money>=200:
                        win.blit(house_big2, (stuppos*width, redpos*height,width-2, height-2))
                        money = money-200
                        population = population+100
                        homes = homes+1
                        homesf = homesf+1
                        homesp = homesp+1
                        landValue=landValue-1
                        m[stuppos][redpos] = 7
                        income=income+1
                    if landValue>=20 and money >=500:
                        win.blit(house_big3, (stuppos*width, redpos*height,width-2, height-2))
                        money = money-500
                        population = population+1000
                        homes = homes+1
                        homesf = homesf+1
                        homesp = homesp+1
                        landValue=landValue-1
                        m[stuppos][redpos] = 8
                        income=income+1
        
        
    if keys[pygame.K_c]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_c]:
            if (money>=100):
                if (m[stuppos][redpos] == 0 or m[stuppos][redpos] == 17):
                    win.blit(shop_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-100
                    shops = shops+1
                    income=income+1
                    m[stuppos][redpos] = 16

    if keys[pygame.K_m] and edit==True:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_m]:
            if (m[stuppos][redpos] == 0):
                win.blit(mountain_big, (stuppos*width, redpos*height,width-2, height-2))
                m[stuppos][redpos] = 2
    if keys[pygame.K_l] and edit==True:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_l]:
            if (m[stuppos][redpos] == 0):
                win.blit(lake_big, (stuppos*width, redpos*height,width-2, height-2))
                m[stuppos][redpos] = 2
    if keys[pygame.K_f] and edit==True:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_f]:
            if (m[stuppos][redpos] == 0):
                win.blit(forest_big, (stuppos*width, redpos*height,width-2, height-2))
                m[stuppos][redpos] = 2
    if keys[pygame.K_w] and edit==True:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_w]:
            if (m[stuppos][redpos] == 0):
                pygame.draw.rect(win, (0, 0, 255),(stuppos*width, redpos*height, width-2, height-2))
                m[stuppos][redpos] = 2
    if keys[pygame.K_s] and edit==True:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_s]:
            if (m[stuppos][redpos] == 0):
                pygame.draw.rect(win, (242,209,107),(stuppos*width, redpos*height, width-2, height-2))
                m[stuppos][redpos] = 17

    if keys[pygame.K_i]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_i]:
            if (money>=100):
                if (m[stuppos][redpos] == 0 or m[stuppos][redpos] == 17):
                    win.blit(factory_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-100
                    factories = factories+1
                    income=income+1
                    m[stuppos][redpos] = 15

    if keys[pygame.K_o]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_o]:
            if (money>=10):
                if (m[stuppos][redpos] == 0 or m[stuppos][redpos] == 17):
                    win.blit(road_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-10
                    m[stuppos][redpos] = 4

    if keys[pygame.K_e]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_e]:
            if (money>=10):
                if (m[stuppos][redpos] == 1 or m[stuppos][redpos] == 2 or m[stuppos][redpos] == 3 or m[stuppos][redpos] == 4 or m[stuppos][redpos] == 5 or m[stuppos][redpos] == 6 or m[stuppos][redpos] == 7 or m[stuppos][redpos] == 8 or m[stuppos][redpos] == 9 or m[stuppos][redpos] == 10 or m[stuppos][redpos] == 11 or m[stuppos][redpos] == 12 or m[stuppos][redpos] == 13 or m[stuppos][redpos] == 14 or m[stuppos][redpos] == 15 or m[stuppos][redpos] == 16):
                    pygame.draw.rect(win, (86, 213, 47),(stuppos*width, redpos*height, width-2, height-2))
                    money = money-10
                    if m[stuppos][redpos] == 6:
                        population = population - 10
                        income=income-1
                        m[stuppos][redpos] = 0
                    elif m[stuppos][redpos] == 7:
                        population = population - 100
                        income=income-1
                        m[stuppos][redpos] = 0
                    elif m[stuppos][redpos] == 8:
                        population = population - 1000
                        income=income-1
                        m[stuppos][redpos] = 0
                    elif m[stuppos][redpos] == 9:
                        m[stuppos][redpos] = 0
                        landValue=landValue-10
                    elif m[stuppos][redpos] == 10:
                        m[stuppos][redpos] = 0
                        fstations=fstations-1
                    elif m[stuppos][redpos] == 11:
                        m[stuppos][redpos] = 0
                        pstations=pstations-1
                    elif m[stuppos][redpos] == 12:
                        m[stuppos][redpos] = 0
                        hospitals=hospitals-1
                    elif m[stuppos][redpos] == 13:
                        m[stuppos][redpos] = 0
                        prisons=prisons-1
                    elif m[stuppos][redpos] == 14:
                        m[stuppos][redpos] = 0
                        cityhalls=cityhalls-1
                    elif m[stuppos][redpos] == 15:
                        m[stuppos][redpos] = 0
                        factories = factories-1
                        income=income-1
                    elif m[stuppos][redpos] == 16:
                        m[stuppos][redpos] = 0
                        shops = shops-1
                        income=income-1
    if keys[pygame.K_p]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_p]:
            if (money>=50):
                if (m[stuppos][redpos] == 0 or m[stuppos][redpos] == 17):
                    win.blit(park_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-50
                    landValue=landValue+10
                    m[stuppos][redpos] = 9

                    
    if keys[pygame.K_f]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_f]:
            if (money>=500):
                if (m[stuppos][redpos] == 0):
                    win.blit(fire_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-500
                    fstations=fstations+1
                    m[stuppos][redpos] = 10

                    
    if keys[pygame.K_l]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_l]:
            if (money>=500):
                if (m[stuppos][redpos] == 0):
                    win.blit(police_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-500
                    pstations=pstations+1
                    m[stuppos][redpos] = 11


    if keys[pygame.K_h]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_h]:
            if (money>=500):
                if (m[stuppos][redpos] == 0):
                    win.blit(hospital_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-500
                    hospitals=hospitals+1
                    m[stuppos][redpos] = 12


    if keys[pygame.K_s]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_s]:
            if (money>=500):
                if (m[stuppos][redpos] == 0):
                    win.blit(prison_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-500
                    prisons=prisons+1
                    m[stuppos][redpos] = 13
    if keys[pygame.K_t]:
        stuppos = round(mouse[0]//width)
        redpos = round(mouse[1]//height)
        if keys[pygame.K_t]:
            if (money>=500):
                if (m[stuppos][redpos] == 0 or m[stuppos][redpos] == 17):
                    win.blit(cityhall_big, (stuppos*width, redpos*height,width-2, height-2))
                    money = money-500
                    cityhalls=cityhalls+1
                    m[stuppos][redpos] = 14






    


    
    pygame.display.update()

pygame.quit()            
