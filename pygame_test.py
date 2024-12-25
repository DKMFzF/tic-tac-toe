import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Графическое окно через Pygame')

app = True

while app:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app = False

pygame.quit()
