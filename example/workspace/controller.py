import pygame
from pygame.locals import *
from typing import Tuple

class GameController:
    def __init__(self):
        self.direction = "RIGHT"

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.direction != "LEFT":
                    self.direction = "RIGHT"
                elif event.key == K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif event.key == K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif event.key == K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
        return True