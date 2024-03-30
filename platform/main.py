import pygame

pygame.init()

win_w = 700
win_h = 500
fps = 60

window = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()
background = pygame.image.load("img/1212.png")
background = pygame.transform.scale(background,(win_w,win_h))


game = True
while game:
    window.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(fps)