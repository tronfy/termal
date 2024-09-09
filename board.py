import numpy as np

QUARTER_CHARS = [
    " ",  # 0000
    "▗",  # 0001
    "▖",  # 0010
    "▄",  # 0011
    "▝",  # 0100
    "▐",  # 0101
    "▞",  # 0110
    "▟",  # 0111
    "▘",  # 1000
    "▚",  # 1001
    "▌",  # 1010
    "▙",  # 1011
    "▀",  # 1100
    "▜",  # 1101
    "▛",  # 1110
    "█",  # 1111
]


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.zeros((self.height, self.width))

    def display(self):
        # reduce flickering
        buf = ""

        # iterate cells in 2x2 blocks
        for y in range(0, self.height, 2):
            for x in range(0, self.width, 2):
                block = self.cells[y : y + 2, x : x + 2]

                # convert 2x2 block to 4-bit number
                block_value = 0
                for i in range(2):
                    for j in range(2):
                        block_value |= (block[i, j] > 0) << (i * 2 + j)

                buf += QUARTER_CHARS[block_value]
            buf += "\n"

        # clear then print
        print("\033[H\033[J", buf, flush=True)
