class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0


class MathAroundTheGame:
    def count_occurrences_with_index(self, my_list):
        result = {}
        for i, element in enumerate(my_list):
            if element not in result:
                result[element] = [i]
            else:
                result[element].append(i)
        return result


math_around_the_game = MathAroundTheGame()


class Jogo:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.fim = False
        self.game = {str(num): "_" for num in range(1, 10)}
        self.turn = 0
        self.list_of_wins = [[0, 1, 2], [0, 4, 8],
                             [3, 4, 5], [4, 5, 6], [2, 4, 6]]
        self.occurrences = []

    def iniciar_jogo(self):
        while self.fim == False:
            skip = 0
            for num in self.game.keys():
                if (int(num) % 3 == 0):
                    if skip == 0:
                        print(list(self.game.values())[:int(num)])
                        skip += 3
                    else:
                        print(list(self.game.values())[skip:int(num)])
                        skip += 3
            positions_available = [i for i, j in self.game.items() if j == "_"]

            print(f"posições disponíveis: {positions_available}")
            if (self.turn == 0):
                position_selected = input(
                    f"Selecione a posição, {self.jogadores[0].nome}\n")
                self.game[position_selected] = "X"
                self.occurences = math_around_the_game.count_occurrences_with_index(
                    list(self.game.values()))
                print(self.occurences)
                if (list(self.occurences["X"]) in self.list_of_wins):
                    self.jogadores[0].pontos += 1
                    print(f"O jogador {self.jogadores[0].nome} ganhou!")
                    self.fim = True

                self.turn = 1
            elif (self.turn == 1):
                position_selected = input(
                    f"Selecione a posição, {self.jogadores[1].nome}\n")
                self.game[position_selected] = "O"
                self.occurences = math_around_the_game.count_occurrences_with_index(
                    list(self.game.values()))
                print(self.occurences)
                if (list(self.occurences["O"]) in self.list_of_wins):
                    self.jogadores[1].pontos += 1
                    print(f"O jogador {self.jogadores[0].nome} ganhou!")
                    self.fim = True
                self.turn = 0


jogadores = [Jogador("Igor"), Jogador("Henrique")]
jogo = Jogo(jogadores)

jogo.iniciar_jogo()
