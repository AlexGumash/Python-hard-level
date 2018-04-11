import random
from pygame.locals import *
from copy import deepcopy
import pygame


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        cell_list = CellList(self.cell_width, self.cell_height, True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.screen.fill(pygame.Color('white'))
            for cell in cell_list:
                if cell.is_alive():
                    pygame.draw.rect(self.screen, pygame.Color('green'), (cell.row * self.cell_size, cell.col * self.cell_size, self.cell_size, self.cell_size))

            cell_list = cell_list.update()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


class Cell:

    def __init__(self, row, col, state):
        self.row = row
        self.col = col
        self.state = state
        pass

    def is_alive(self):
        if self.state == 0:
            return False
        else:
            return True
        pass


class CellList:

    def __init__(self, nrows, ncols, randomize=True):
        self.nrows = nrows
        self.ncols = ncols

        self.randomize = randomize

        self.iterator_x = 0
        self.iterator_y = 0

        self.list = [[Cell(i, j, random.randrange(0, 2)) for j in range(ncols)] for i in range(nrows)]
        pass

    def get_neighbours(self, cell):
        i, j = cell.row, cell.col
        try:
            count = 0
            if self.list[i-1][j-1].is_alive(): count += 1
            if self.list[i-1][j].is_alive(): count += 1
            if self.list[i-1][j+1].is_alive(): count += 1
            if self.list[i][j-1].is_alive(): count += 1
            if self.list[i][j+1].is_alive(): count += 1
            if self.list[i+1][j-1].is_alive(): count += 1
            if self.list[i+1][j].is_alive(): count += 1
            if self.list[i+1][j+1].is_alive(): count += 1
        except:
            return 0
        return count

    def update(self):
        new_clist = deepcopy(self)
        for i in range(len(new_clist.list)):
            for j in range(len(new_clist.list[i])):
                neighbours = self.get_neighbours(self.list[i][j])
                if neighbours > 3 or neighbours < 2:
                    new_clist.list[i][j].state = 0
                if (self.list[i][j].is_alive() == False and neighbours == 3):
                    new_clist.list[i][j].state = 1
        return new_clist

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator_x == self.nrows - 1 and self.iterator_y == self.ncols - 1:
            self.iterator_x, self.iterator_y = 0, 0
            raise StopIteration

        self.iterator_y += 1

        if self.iterator_y == self.ncols:
            self.iterator_y = 0
            self.iterator_x += 1
        return self.list[self.iterator_x][self.iterator_y]

    @classmethod
    def from_file(cls, filename):
        pass

if __name__ == '__main__':
    game = GameOfLife(320, 240, 10)
    game.run()