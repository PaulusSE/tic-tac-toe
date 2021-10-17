# dockstring for my file
""" This is tic tac toe console python game """


class GameSession:
    """ This is class for creatin tic tac toe game session """
    def __init__(self):
        self.coords = []
        self.value = 'O'
        self.end_game = False
        self.check_value = False
        # current field
        self.dict = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]
        # combination of coordinates that will lead to victory
        self.win_combination = [[[1, 1], [1, 2], [1, 3]],
                                [[1, 1], [2, 1], [3, 1]],
                                [[1, 1], [2, 2], [3, 3]],
                                [[3, 1], [2, 2], [1, 3]],
                                [[1, 3], [2, 3], [3, 3]],
                                [[3, 1], [3, 2], [3, 3]],
                                [[2, 1], [2, 2], [2, 3]],
                                [[1, 2], [2, 2], [3, 2]],
                                ]

    def point_input(self):
        """ create user input and check it for valid values """
        # create user input and check it for valid values
        self.coords = input().split()
        if len(self.coords) != 2:
            print('Введите 2 числа через пробел!\n'
                  'Ожидаются координаты от 1 до 3')
            self.check_value = False
            self.point_input()
            return None
        if int(self.coords[0]) not in (1, 2, 3) \
                or int(self.coords[1]) not in (1, 2, 3):
            print('Неверный формат, повторите ввод!\n'
                  'Ожидаются координаты от 1 до 3')
            self.check_value = False
            self.point_input()
            return None
        if self.dict[int(self.coords[0])-1][int(self.coords[1])-1] != ' ':
            print('Клетка уже занята! измените выбор!')
            self.check_value = False
            self.point_input()
            return None

        self.check_value = True
        return [self.coords[0], self.coords[1]]

    def display_board(self):
        """ Display game board on screen. """
        # Display game board on screen.
        print('y\\x', '', "|", 1, "|", 2, "|", 3)
        print("   ---------------")
        print('  ', '1', "|", self.dict[0][0], "|",
              self.dict[0][1], "|", self.dict[0][2])
        print("   ---------------")
        print('  ', '2', "|", self.dict[1][0], "|",
              self.dict[1][1], "|", self.dict[1][2])
        print("   ---------------")
        print('  ', '3', "|", self.dict[2][0], "|",
              self.dict[2][1], "|", self.dict[2][2])

    def field_update(self):
        """ update current field with appropriate value """
        # update current field with appropriate value
        self.point_input()
        self.dict[int(self.coords[0])-1][int(self.coords[1])-1] = self.value
        self.display_board()

    def game_process(self):
        """ game process function that will determine the winners and draft """
        # game process function that will determine the winners and draft
        game.display_board()

        player = 1

        while self.end_game is not True:
            print(f'Xодит игрок {player}.\nKуда поставить {self.value}?\n'
                  '(введите координаты Х и У от 1 до 3 через пробел):')
            self.field_update()

            for each in self.win_combination:
                if self.dict[each[0][0] - 1][each[0][1] - 1] == \
                        self.dict[each[1][0] - 1][each[1][1] - 1] == \
                        self.dict[each[2][0] - 1][each[2][1] - 1] != ' ':
                    self.end_game = True
                    print(f'Player {player} win!')

            if player == 1:
                player += 1
                self.value = 'X'
            else:
                player -= 1
                self.value = 'O'

            if ' ' not in self.dict[0] \
                    and ' ' not in self.dict[1] \
                    and ' ' not in self.dict[2]:
                self.end_game = True
                print('Draft')


game = GameSession()
game.game_process()
