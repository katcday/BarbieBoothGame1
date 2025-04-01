import pygame
import game
from button import Button
import random

class End:
    def __init__(self, screen, image):
        self.screen = screen
        self.image = image
        self.font = pygame.font.SysFont('arial', int(game.screen_width/25))
        self.words = ["Fabulous!", "Perfect!", "Awesome!", "Super!"]
        self.word = random.choice(self.words)

        self.width = game.screen_width
        self.height = game.screen_height
        button_width = game.screen_width/4
        button_height = game.screen_height/12

        self.email = Button("email", 3*self.width/4 - button_width/2,
                            self.height/2, button_width, button_height,
                            game.PINK, game.LIGHT_PINK)

        self.restart = Button("restart", 3*self.width/4 - button_width/2,
                            self.height/2 + 6*button_height/5, button_width, button_height,
                            game.PINK, game.LIGHT_PINK)

    def draw(self):
        self.screen.fill(game.WHITE)
        text = self.font.render(self.word, True, game.PINK)
        self.screen.blit(text, (3*self.width/4- text.get_width()//2, self.height/4))

        scale = 0.25
        iwidth = int(self.width * scale)
        iheight = int(self.width * scale)


        padding = self.width/50
        frame = iwidth + 2*padding
        framex = self.width/4 - frame/2
        framey = self.height/3 - frame/2

        ix = framex + padding
        iy = framex + padding

        pygame.draw.rect(self.screen, game.PINK, [framex, framey, frame, frame], 10)
        self.screen.blit(pygame.transform.scale(self.image, (iwidth, iheight)), (ix, iy))

        self.email.draw(self.screen, self.font)
        self.restart.draw(self.screen, self.font)

    def state(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart.clicked(pygame.mouse.get_pos()):
                return "start"

        self.restart.collide(pygame.mouse.get_pos())
        self.email.collide(pygame.mouse.get_pos())

        return "end"
