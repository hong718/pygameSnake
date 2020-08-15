import pygame
import sys
import os
from main import Game
from button import Button
pygame.init()
width = 480
screen = pygame.display.set_mode((width,width))
clock = pygame.time.Clock()

# button and text
button_img = pygame.transform.scale(pygame.image.load(os.path.join('game_assets', 'button.png')), (150,75))
text_font = pygame.font.Font(os.path.join('game_assets', 'Boba.otf'), 35)
diff = text_font.render('Choose a difficulty', True, (255, 255, 255))
easy = text_font.render('Easy', True, (255, 255, 255))
medium = text_font.render('Medium', True, (255, 255, 255))
difficult = text_font.render('Difficult', True, (255, 255, 255))
snake = text_font.render('Pygame Snake', True, (0, 255, 0))

easy_button = Button(button_img, easy)
medium_button = Button(button_img, medium)
difficult_button = Button(button_img, difficult)
menu = True

while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # run the game with corresponding level when a button is clicked
            if easy_button.click(pos[0], pos[1], 240, 170, 1):
                g = Game(screen)
                g.run(1)
            elif medium_button.click(pos[0], pos[1], 240, 170, 2):
                g = Game(screen)
                g.run(2)
            elif difficult_button.click(pos[0], pos[1], 240, 170, 3):
                g = Game(screen)
                g.run(3)

    # draw the background
    screen.fill((0,0,0))
    screen.blit(screen, (0,0))

    # draw button
    easy_button.draw(screen,240, 170, 1)
    medium_button.draw(screen ,240, 170, 2)
    difficult_button.draw(screen, 240, 170, 3)

    # draw font
    screen.blit(snake, (240 - snake.get_width() // 2, 100))
    screen.blit(diff,(240 - diff.get_width() // 2, 170 +  button_img.get_height() * 3 + 20) )


    pygame.display.flip()
    clock.tick(10)
