import pygame
from dino_runner.components import game_over

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.game_over import Game_Over
from dino_runner.components.obstacles.obstacle_manager import ObstacleManger
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.game_over = Game_Over()
        self.obstacle_manager = ObstacleManger()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.count_score = 0
        pygame.mixer.music.load("dino_runner/assets/Other/sound_background.mp3")
        pygame.mixer.music.play(-1)

    def run(self):
        self.power_up_manager.reset_power_ups(self.points)
        
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.count_score += 1
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.score()
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score(self.screen,str(self.count_score),SCREEN_WIDTH // 2, 10)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
        self.player.check_invincibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_score(self,screen,text,x,y):
        BLACK = (0,0,0,0)
        font = pygame.font.SysFont("Arial",30)
        text_screen = font.render("Score: "+text, True, BLACK)
        text_rect = text_screen.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_screen,text_rect)