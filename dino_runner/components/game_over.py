from email.mime import image
import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.utils.constants import GAME_OVER

class Game_Over():

    def __init__(self):
        self.image = GAME_OVER
        self.image_rect = self.image.get_rect()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image_rect.x = 300
        self.image_rect.y = 200

    def update(self,user_input):
        if user_input[pygame.K_SPACE]:
           self.image.pop()
           self.game.playing = True

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image,self.image_rect)
    