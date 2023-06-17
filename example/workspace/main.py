import pygame
from typing import Tuple
from model import Board
from view import GameView
from controller import GameController

def main(board_size: Tuple[int, int], block_size: int):
    pygame.init()
    board = Board(board_size)
    view = GameView(board_size, block_size)
    controller = GameController()
    score = 0

    # Crea un reloj para controlar la velocidad del juego
    clock = pygame.time.Clock()

    while True:
        # Agrega un delay para que el juego no se ejecute a la máxima velocidad
        clock.tick(10)  # 10 es el número de cuadros por segundo
        # pygame.time.delay(200) # Agregamos un pequeño delay para ver mejor la acción de la serpiente
        if not controller.handle_events():
            break
        board.snake.direction = controller.direction  # Añadido para actualizar la dirección de la serpiente
        snake_positions, food_position = board.update_board()        
        if snake_positions == []:
            print("La serpiente se ha chocado")
            break
        if food_position == (-1, -1):
            print("La serpiente ha comido la comida")
            score += 1
        view.draw_board(snake_positions, food_position, score)

    pygame.quit()

if __name__ == "__main__":
    main((20, 20), 20)
