from typing import List, Tuple
import random

class Snake:
    def __init__(self, start_pos: Tuple[int, int], length: int):
        self.positions = [start_pos]
        self.length = length
        self.direction = "RIGHT"

    def move(self):
        head_pos = self.positions[0]
        if self.direction == "RIGHT":
            new_pos = (head_pos[0]+1, head_pos[1])
        elif self.direction == "LEFT":
            new_pos = (head_pos[0]-1, head_pos[1])
        elif self.direction == "UP":
            new_pos = (head_pos[0], head_pos[1]-1)
        elif self.direction == "DOWN":
            new_pos = (head_pos[0], head_pos[1]+1)
        self.positions.insert(0, new_pos)
        if len(self.positions) > self.length:
            self.positions.pop()

    def grow(self):
        self.length += 1

    def check_collision(self, board_size: Tuple[int, int]) -> bool:
        head_pos = self.positions[0]
        if head_pos[0] < 0 or head_pos[0] >= board_size[0] or head_pos[1] < 0 or head_pos[1] >= board_size[1]:
            return True
        for pos in self.positions[1:]:
            if pos == head_pos:
                return True
        return False

class Food:
    def __init__(self, board_size: Tuple[int, int]):
        self.position = (0, 0)
        self.board_size = board_size

    def place_food(self, snake_positions: List[Tuple[int, int]]):
        while True:
            x = random.randint(0, self.board_size[0]-1)
            y = random.randint(0, self.board_size[1]-1)
            if (x, y) not in snake_positions:
                self.position = (x, y)
                break

class Board:
    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.snake = Snake((size[0]//2, size[1]//2), 3)
        self.food = Food(size)
        self.food.place_food(self.snake.positions)

    def update_board(self) -> Tuple[List[Tuple[int, int]], Tuple[int, int]]:
        self.snake.move()
        if self.snake.positions[0] == self.food.position:
            self.snake.grow()
            self.food.place_food(self.snake.positions)
        if self.snake.check_collision(self.size):
            return [], (-1, -1)
        return self.snake.positions, self.food.position