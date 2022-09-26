from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Birds(Obstacle):

    def __init__(self, image):
        type = random.randint(0,1)
        super().__init__(image, type)
        self.rect.y = random.randint(100,300)