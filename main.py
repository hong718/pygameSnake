import pygame
import sys
import os
import random
from snake import snake
from button import Button

pygame.init()
width = 480
rows = 20
dis = width // rows
screen = pygame.display.set_mode((width,width))
clock = pygame.time.Clock()

# pause menu button
button_large_img = pygame.transform.scale(pygame.image.load(os.path.join('game_assets', 'button.png')), (200,50))
button_small_img = pygame.transform.scale(pygame.image.load(os.path.join('game_assets', 'button.png')), (100,50))
large_text_font = pygame.font.Font(os.path.join('game_assets', 'Boba.otf'), 30)
small_text_font = pygame.font.Font(os.path.join('game_assets', 'Boba.otf'), 25)
collide_text = large_text_font.render('You collided  with yourself. Restart?', True, (255, 255, 255))
yes_text = small_text_font.render('Yes!', True, (255, 255, 255))
no_text = small_text_font.render('No!', True, (255, 255, 255))
menu_text = small_text_font.render('Back to menu!', True, (255, 255, 255))

# button
button_yes = Button(button_small_img, yes_text)
button_no = Button(button_small_img, no_text)
button_menu = Button(button_large_img, menu_text)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = snake((255, 0, 0), (10, 10))
        self.snack_pos = (random.randint(0,19), random.randint(0,19))
        self.genSnack = False
        self.isCollide = False
        self.click = 5
        self.isRun = True
        self.pause = False
        self.isMenu = False

    def drawGrid(self, rows, width):
        '''
        draw the grid line
        :param rows: int
        :param width: int
        :return: None
        '''
        dis = width // rows
        x = 0
        y = 0
        for i in range(rows):
            x += dis
            y += dis
            pygame.draw.line(screen, (255,255,255), (x, 0), (x, width), 1)
            pygame.draw.line(screen, (255,255,255), (0, y), (width, y), 1)

    def addSnack(self):
        '''
        add a snack in random position
        :return: None
        '''
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        self.snack_pos = (x, y)

    def Collide(self):
        '''
        check whether the snake ran into itself
        :return: bool
        '''
        for cube in self.snake.body[1:]:
            if self.snake.body[0].pos == cube.pos:
                return True
        return False

    def Pause(self):
        '''
        pause the game when a snake ran into itself
        :return: None
        '''
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_yes.click(pos[0], pos[1], 180, 240, 1):
                        self.pause = False
                    if button_no.click(pos[0], pos[1], 300, 240, 1):
                        pygame.quit()
                        sys.exit()
                    if button_menu.click(pos[0], pos[1], 240, 240 + button_small_img.get_height(), 1):
                        self.pause = False
                        self.isRun = False
                        self.isMenu = True


                self.screen.blit(collide_text, (240 - collide_text.get_width() // 2, 240 - collide_text.get_height() ))
                button_yes.draw(self.screen, 180, 240)
                button_no.draw(self.screen, 300, 240)
                button_menu.draw(self.screen, 240, 240 + button_small_img.get_height())

                pygame.display.flip()
                clock.tick(15)

    def clear(self):
        '''
        clear the snake when the player goes back to menu
        :return: None
        '''
        self.snake.body.clear()
        self.snake.turn_pos.clear()
        self.isRun = False
        self.isMenu = False

    def run(self, level):
        while self.isRun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        # check whether it walks the opposite direction
                        # check whether there are any turns
                        if self.snake.body[0].dir_x == 1:
                            self.pause = True
                            self.Pause()
                            if self.isMenu:
                                self.clear()
                                break
                            else:
                                self.snake.reset((10,10))
                        self.snake.turn([-1, 0])
                        self.snake.dir_x = -1
                        self.snake.dir_y = 0
                    if event.key == pygame.K_d:
                        if self.snake.body[0].dir_x == -1:
                            self.pause = True
                            self.Pause()
                            if self.isMenu:
                                self.clear()
                                break
                            else:
                                self.snake.reset((10,10))
                        self.snake.turn([1, 0])
                        self.snake.dir_x = 1
                        self.snake.dir_y = 0
                    if event.key == pygame.K_w:
                        if self.snake.body[0].dir_y == 1:
                            self.pause = True
                            self.Pause()
                            if self.isMenu:
                                self.clear()
                                break
                            else:
                                self.snake.reset((10,10))
                        self.snake.turn([0, -1])
                        self.snake.dir_x = 0
                        self.snake.dir_y = 1
                    if event.key == pygame.K_s:
                        if self.snake.body[0].dir_y == -1:
                            self.pause = True
                            self.Pause()
                            if self.isMenu:
                                self.clear()
                                break
                            else:
                                self.snake.reset((10,10))
                        self.snake.turn([0, 1])
                        self.snake.dir_x = 0
                        self.snake.dir_y = -1

            if self.isRun:
                # draw the screen
                self.screen.fill((0, 0, 0))
                screen.blit(screen, (0,0))
                self.drawGrid(rows, width)

                # draw the snack
                if self.genSnack:
                    self.addSnack()
                    self.genSnack = False
                pygame.draw.rect(self.screen, (0, 255, 255), (self.snack_pos[0] * dis, self.snack_pos[1] * dis, dis, dis))


                # check the level
                if len(self.snake.body) // 5 >= level:
                    level += 1

                self.snake.move()

                # check whether it collides with the snack
                if self.snake.body[0].pos == self.snack_pos:
                    self.genSnack = True
                    self.snake.addCube()

                # check whether it collides with itself
                self.isCollide = self.Collide()
                if self.isCollide:
                    self.pause = True
                    self.Pause()
                    if self.isMenu:
                        self.clear()
                        break
                    else:
                        self.snake.reset((10,10))
                    self.isCollide = False


                # draw the snake
                self.snake.draw(screen)

                pygame.display.flip()
                self.click = 2 + level * 3
                clock.tick(self.click)

