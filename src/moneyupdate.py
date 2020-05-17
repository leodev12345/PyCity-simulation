import pygame

up=0
umoney=0
mwin=0
def update():
    if umoney>=100 and umoney<1000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 20, 20))
    if umoney>=10 and umoney<100:
        pygame.draw.rect(mwin, (86, 213, 47),(740, 50, 20, 20))
    if umoney>=1000 and umoney<10000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 40, 20))
    if umoney>=10000 and umoney<100000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 60, 20))
    if umoney>=100000 and umoney<1000000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 80, 20))
    if umoney>=1000000 and umoney<10000000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 100, 20))
    if umoney>=10000000 and umoney<100000000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 120, 20))
    if umoney>=100000000 and umoney<1000000000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 140, 20))
    if umoney>=1000000000 and umoney<10000000000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 100, 20))
    if umoney>=10000000000 and umoney<100000000000:
        pygame.draw.rect(mwin, (86, 213, 47),(760, 50, 100, 20))

    if umoney>=100 and umoney<1000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 20, 20))
    if umoney>=10 and umoney<100:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 20, 20))
    if umoney>=1000 and umoney<10000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 40, 20))
    if umoney>=10000 and umoney<100000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 60, 20))
    if umoney>=100000 and umoney<1000000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 80, 20))
    if umoney>=1000000 and umoney<10000000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 100, 20))
    if umoney>=10000000 and umoney<100000000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 120, 20))
    if umoney>=100000000 and umoney<1000000000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 140, 20))
    if umoney>=1000000000 and umoney<10000000000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 100, 20))
    if umoney>=10000000000 and umoney<100000000000:
        pygame.draw.rect(mwin, (86, 213, 47),(735, 90, 100, 20))
    
        

        
