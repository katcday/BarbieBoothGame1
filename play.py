from xml.sax.handler import property_xml_string

import pygame
import game
from button import Button, ImageButton
import fonts

class Play:
    def __init__(self, screen, image):
        self.screen = screen
        self.doll = image
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.font = fonts.load_main_font(int(self.width/25))
        self.corner = Button("", 4*self.width/5,
                             self.height/12,
                             self.width/8, self.width/8, game.PINK, game.LIGHT_PINK)
        self.buttons = [ImageButton('images/arrow.png', 100, 100, True, 100), ImageButton('images/arrow.png', 500, 100, False, 100)]


        self.pop = False
        pop_width, pop_height = self.width / 2, self.height / 2
        pop_x = (self.width - pop_width) // 2
        pop_y = (self.height - pop_height) // 2
        self.popup = pygame.Rect(pop_x, pop_y, pop_width, pop_height)

        button_width, button_height = self.width/4, self.height/12
        button_x = pop_x + (pop_width - button_width) // 2

        self.finish = Button("finish", (self.width - button_width)/2,
                             2*self.height/5,
                             button_width, button_height, game.WHITE, game.LIGHT_PINK)
        self.resume = Button("resume", (self.width - button_width)/2,
                              self.height/2,
                               button_width, button_height, game.WHITE, game.LIGHT_PINK)



    def draw(self):
        self.screen.fill(game.BACKGROUND)

        ix = (self.width - self.doll.get_width()) / 2 
        iy = (self.height - self.doll.get_height()) / 2
        self.screen.blit(self.doll, (ix, iy))

        self.corner.draw(self.screen, self.font)

        if self.pop:
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            self.screen.blit(overlay, (0,0))

            self.finish.draw(self.screen, self.font)
            self.resume.draw(self.screen, self.font)

    def state(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if self.pop:
                if self.finish.clicked(pos):
                    return "end"
                elif self.resume.clicked(pos):
                    self.pop = False
            else:
                if self.corner.clicked(pos):
                    self.pop = True


        if self.pop:
            self.finish.collide(pygame.mouse.get_pos())
            self.resume.collide(pygame.mouse.get_pos())
        else:
            self.corner.collide(pygame.mouse.get_pos())

        return "play"
