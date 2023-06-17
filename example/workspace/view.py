from typing import List, Tuple
import pygame

class GameView:
    def __init__(self, board_size: Tuple[int, int], block_size: int):
        self.board_size = board_size
        self.block_size = block_size
        self.screen_size = (board_size[0]*block_size, board_size[1]*block_size)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Snake Game")
        self.font = pygame.font.SysFont("Arial", 20)

    def draw_board(self, snake_positions: List[Tuple[int, int]], food_position: Tuple[int, int], score: int):
        self.screen.fill((255, 255, 255))
        for pos in snake_positions:
            pygame.draw.rect(self.screen, (0, 255, 0), (pos[0]*self.block_size, pos[1]*self.block_size, self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (food_position[0]*self.block_size, food_position[1]*self.block_size, self.block_size, self.block_size))
        score_text = self.font.render("Score: " + str(score), True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()