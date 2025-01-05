import pygame 
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding Image")

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(30,30,60,60))   
    pygame.draw.circle(screen,(0,250,0),(300,300),50)   
    pygame.draw.circle(screen,(0,0,250),(100,100),50,3)
    pygame.display.flip()