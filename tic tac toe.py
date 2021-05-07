class Board:

    boxes = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    @classmethod
    def display(cls):
        print("\nBoard:")
        print(cls.boxes[0], "|", cls.boxes[1], "|", cls.boxes[2])
        print("---------")
        print(cls.boxes[3], "|", cls.boxes[4], "|", cls.boxes[5])
        print("---------")
        print(cls.boxes[6], "|", cls.boxes[7], "|", cls.boxes[8])

    @classmethod
    def check_winner(cls):
        if Board.match_boxes(cls.boxes[0], cls.boxes[3], cls.boxes[6]):
            return True
        elif Board.match_boxes(cls.boxes[0], cls.boxes[4], cls.boxes[8]):
            return True
        elif Board.match_boxes(cls.boxes[0], cls.boxes[1], cls.boxes[2]):
            return True
        elif Board.match_boxes(cls.boxes[4], cls.boxes[1], cls.boxes[7]):
            return True
        elif Board.match_boxes(cls.boxes[2], cls.boxes[4], cls.boxes[6]):
            return True
        elif Board.match_boxes(cls.boxes[2], cls.boxes[5], cls.boxes[8]):
            return True
        elif Board.match_boxes(cls.boxes[3], cls.boxes[4], cls.boxes[5]):
            return True
        elif Board.match_boxes(cls.boxes[6], cls.boxes[7], cls.boxes[8]):
            return True

        return False

    @staticmethod
    def match_boxes(one_box, two_box, three_box):
        if " " in {one_box, two_box, three_box}:
            return False
        if one_box == two_box == three_box:
            return True
        return False


class Player:
    players = []

    def __init__(self):
        self.name = None
        self.is_winner = False
        self.symbol = None

    @staticmethod
    def new_player():
        print("\nOkay, a new player will be made!")
        player = Player()
        player.name = player.get_name()

        if len(Player.players) == 0:
            player.symbol = player.get_symbol()
        else:
            if Player.players[0].symbol == "X":
                player.symbol = "O"


        Player.players.append(player)
        return player

    @staticmethod
    def get_name():
        given_name = input("Enter your name: ")
        return given_name.upper()

    def get_symbol(self):
        print("Hello ", self.name, ", what will your symbol be?")
        while True:
            chosen_symbol = input("Choose symbol (X/O): ")
            if chosen_symbol.upper() not in ("X", "O"):
                print("Only 'X' or 'O' allowed.")
            else:
                break

        return chosen_symbol.upper()

    def player_turn(self):
        print("Okay ", self.name, ",it is now your turn.")
        chosen_box = int(input("Choose box (1-9): "))
        return chosen_box - 1


# GAME STARTS HERE
intro = input("Hello, welcome to tic tac toe!")
game_over = False

print("Would you like to play single player or two player mode?")

while True:
    game_mode = input("Choose mode (single/double): ")

    if game_mode == "single":
        print("\nOkay, single player it is!")
        player_one = Player.new_player()
        break
    elif game_mode == "double":
        print("\nOkay, double player it is!")
        player_one = Player.new_player()
        player_two = Player.new_player()
        break
    else:
        print("Only 'single' or double' allowed.")

current_player = Player.players[0]
while not game_over:

    board = Board()
    board.display()

    box = current_player.player_turn()
    board.boxes[box] = current_player.symbol

    print("The player ", current_player.name, " marked box #", box + 1)

    current_player.is_winner = Board.check_winner()

    if current_player.is_winner:
        game_over = True
        print("\n*", current_player.name, " is the winner!!!")
        Board.display()
        break

    if current_player == Player.players[0]:
        current_player = Player.players[1]
    elif current_player == Player.players[1]:
        current_player = Player.players[0]
