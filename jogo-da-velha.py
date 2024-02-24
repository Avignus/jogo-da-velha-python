class Player:
    def __init__(self, name, sign):
        self.name = name
        self.points = 0
        self.sign = sign


class MathAroundTheGame:
    def count_occurrences_with_index(self, my_list):
        result = {}
        for i, element in enumerate(my_list):
            if element not in result:
                result[element] = [i]
            else:
                result[element].append(i)
        return result

    def check_if_it_has_won_pattern(self):
        pass

    def check_win(self, occurrences, win_pattern):
        intersection = set(occurrences) & set(win_pattern)
        print(intersection)
        if len(intersection) == 3:
            return True


math_around_the_game = MathAroundTheGame()


class Game:
    def __init__(self, players):
        self.players = players
        self.fim = False
        self.game = {str(num): "_" for num in range(1, 10)}
        self.turn = 0
        self.list_of_wins = [[0, 1, 2], [0, 3, 6], [0, 4, 8],
                             [3, 4, 5], [4, 5, 6], [2, 4, 6]]
        self.occurrences = []
        self.signs = ["X", "O"]
        self.condition = False

    def show_board(self):
        skip = 0
        for num in self.game.keys():
            if (int(num) % 3 == 0):
                if skip == 0:
                    print(list(self.game.values())[:int(num)])
                    skip += 3
                else:
                    print(list(self.game.values())[skip:int(num)])
                    skip += 3

    def show_positions_available(self):
        positions_available = [i for i, j in self.game.items() if j == "_"]
        print(f"Posições disponíveis: {positions_available}")

    def play_game(self):
        while self.fim == False:
            self.show_board()
            self.show_positions_available()
            self.play_turn()

    def play_turn(self):
        player = self.players[self.turn]
        sign = player.sign
        position_selected = input(
            f"É a vez de {player.name}, selecione a posicao:\n")
        if int(position_selected) > 9 or int(position_selected) < 1:
            print("Posição inválida, por favor, selecione uma entre 1 e 9")
            self.play_turn()
        else:
            if self.game[position_selected] == "_":
                self.game[position_selected] = sign
                self.occurrences = math_around_the_game.count_occurrences_with_index(
                    list(self.game.values()))
                for i in self.list_of_wins:
                    self.condition = math_around_the_game.check_win(
                        self.occurrences[sign], i)

                    if self.condition == True:
                        self.fim = self.condition
                        print(f"O jogador {player.name} ganhou!")
                        self.show_board()
                self.change_turn()
            else:
                print("Posição já selecionada, por favor, selecione outra:")

    def change_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0


players = [Player("Igor", "X"), Player("Henrique", "O")]
game = Game(players)

game.play_game()
