import pygame

class Button():
    def __init__(self, img, text = None):
        self.img = img
        self.text = text



    def draw(self, win, x, y, index = 1):
        '''
        draw the button with corresponding index
        :param win: surface
        :param x: int
        :param y: int
        :param index: int
        :return: None
        '''
        win.blit(self.img, (x - self.img.get_width() // 2, y + self.img.get_height() * (index - 1)))
        if self.text:
            win.blit(self.text, (x - self.text.get_width() // 2, y + self.img.get_height() // 2 + self.img.get_height() * (index - 1) - self.text.get_height() // 2))

    def click(self, X, Y, x, y, index = 1):
        '''
        return true if a button is clicked
        :param X: mouse x
        :param Y: mouse y
        :param x: button x
        :param y: button y
        :param index: int
        :return: bool
        '''
        if X >= x - self.img.get_width() // 2 and X <= x  + self.img.get_width() // 2:
            if Y >= y + self.img.get_height() * (index - 1) and Y <= y + self.img.get_height() * (index):
                return True
        return False
