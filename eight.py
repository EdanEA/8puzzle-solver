from random import shuffle
from math import ceil, sqrt

class Eight:
    def __init__(self, order: str = "", expected = "123456780"):
        order_list = []

        if len(order) != 9:
            order_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            shuffle(order_list)
            order = ''.join([str(x) for x in order_list])
        else:
            order_list = [int(c) for c in order]

        self.order: str = order
        self.grid: list[list[int]] = []
        self.expected = expected
        self.exptected_xys = []

        for y in range(3):
            row = []

            for x in range(3):
                row.append(order_list.pop(0))

            self.grid.append(row)

    def available_moves(self) -> list[str]:
        output = []
        x, y = self.locate(0)

        if x == -1 or x == -1:
            return output

        if x == 0 or x == 1:
            output.append("l")

        if x == 1 or x == 2:
            output.append("r")

        if y == 0 or y == 1:
            output.append("u")

        if y == 1 or y == 2:
            output.append("d")

        return output

    def locate(self, val: int) -> tuple[int, int]:
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == val:
                    return (x, y)

        return (-1, -1)

    def __str__(self) -> str:
        out = ""

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                out += str(self.grid[i][j]) + "\t"

            if i != len(self.grid) - 1:
                out += "\n"

        return out

    def move(self, direction: str) -> bool:
        x, y = self.locate(0)
        moves = self.available_moves()

        if direction not in moves:
            return False

        if direction == "l":
            self.grid[y][x] = self.grid[y][x + 1]
            self.grid[y][x + 1] = 0
        elif direction == "r":
            self.grid[y][x] = self.grid[y][x - 1]
            self.grid[y][x - 1] = 0
        elif direction == "u":
            self.grid[y][x] = self.grid[y + 1][x]
            self.grid[y + 1][x] = 0
        elif direction == "d":
            self.grid[y][x] = self.grid[y - 1][x]
            self.grid[y - 1][x] = 0

        self.update_order()

        return True

    def update_order(self) -> None:
        order = ""

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                order += str(self.grid[i][j])

        self.order = order

    def opposite_move(self, move: str) -> str:
        if move == "l":
            return "r"
        elif move == "r":
            return "l"
        elif move == "u":
            return "d"
        elif move == "d":
            return "u"

        return ""

    def distance_from_expected(self, val: int, order: str = "123456780") -> int:
        if val < 0 or val > 9:
            return -1

        expected_puzzle = Eight(order)
        expected_xys = []

        if order == self.expected and len(self.exptected_xys) != 0:
            expected_xys = self.exptected_xys
        else:
            for i in range(0, 9):
                expected_xys.append(expected_puzzle.locate(i))

            if order == self.expected:
                self.exptected_xys = expected_xys

        expected = expected_xys[val]
        actual = self.locate(val)

        return ceil(sqrt((actual[0] - expected[0]) ** 2 + (actual[1] - expected[1]) ** 2))

    def unsolvable(self) -> bool:
        count = 0

        for j in range(len(self.order)):
            if self.order[j] == "0":
                continue

            for i in range(j + 1, len(self.order)):
                if self.order[i] == "0":
                    continue

                if int(self.order[i]) < int(self.order[j]):
                    count += 1

        return count % 2 == 1
