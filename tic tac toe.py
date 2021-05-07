MAX_TURNS = 9


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
        if cls.match_boxes(cls.boxes[0], cls.boxes[3], cls.boxes[6]):
            return True
        elif cls.match_boxes(cls.boxes[0], cls.boxes[4], cls.boxes[8]):
            return True
        elif cls.match_boxes(cls.boxes[0], cls.boxes[1], cls.boxes[2]):
            return True
        elif cls.match_boxes(cls.boxes[4], cls.boxes[1], cls.boxes[7]):
            return True
        elif cls.match_boxes(cls.boxes[2], cls.boxes[4], cls.boxes[6]):
            return True
        elif cls.match_boxes(cls.boxes[2], cls.boxes[5], cls.boxes[8]):
            return True
        elif cls.match_boxes(cls.boxes[3], cls.boxes[4], cls.boxes[5]):
            return True
        elif cls.match_boxes(cls.boxes[6], cls.boxes[7], cls.boxes[8]):
            return True
        return False

    @staticmethod
    def match_boxes(box_one, box_two, box_three):
        if " " in {box_one, box_two, box_three}:
            return False

        if box_one == box_two == box_three:
            return True
        return False


class Player:
    players = []

    def __init__(self):
        print("\nOkay, a new player will be made!")
        self.name = self.get_name()

        if len(Player.players) == 0:
            self.symbol = self.get_symbol()
        else:
            self.symbol = self.set_symbol()
        print("Okay, your symbol is ", self.symbol)

        self.is_winner = False
        Player.players.append(self)

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

    def set_symbol(self):
        if Player.players[0].symbol == "X":
            return "O"
        return "X"

    @staticmethod
    def player_turn():
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
        player_one = Player()
        break
    elif game_mode == "double":
        print("\nOkay, double player it is!")
        player_one = Player()
        player_two = Player()
        break
    else:
        print("Only 'single' or double' allowed.")

current_player = Player.players[0]
turns_count = 0

while not game_over:
    board = Board()
    board.display()

    if turns_count == MAX_TURNS:
        print("\nDraw, there is no winner!")
        game_over = True
        break

    print("Okay ", current_player.name, ",it is now your turn.")
    while True:
        box_number = current_player.player_turn()
        box = board.boxes[box_number]

        if box != "X" and box != "O":
            box = current_player.symbol
            break
        print("You must choose an empty box.")

    print("The player ", current_player.name, " marked box #", box_number + 1)

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

    turns_count += 1
