import numpy as np
import time

from board import Board

WIDTH = 256
HEIGHT = 32
FPS = 5


def main():
    life = np.random.randint(0, 2, (HEIGHT, WIDTH))
    board = Board(WIDTH, HEIGHT)

    while True:
        try:
            newlife = life.copy()

            for y in range(HEIGHT):
                for x in range(WIDTH):
                    neighbors = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if dx == 0 and dy == 0:
                                continue
                            if 0 <= y + dy < HEIGHT and 0 <= x + dx < WIDTH:
                                neighbors += life[y + dy, x + dx]
                    if life[y, x] == 1:
                        newlife[y, x] = 1 if neighbors in (2, 3) else 0
                    else:
                        newlife[y, x] = 1 if neighbors == 3 else 0

            life = newlife

            board.cells = life
            board.display()
            # time.sleep(1 / FPS)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
