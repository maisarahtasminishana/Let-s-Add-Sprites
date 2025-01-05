import pygame 
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My First Game Screen ")

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(50,0,0),pygame.Rect(320,240,60,60))   
    pygame.display.flip()