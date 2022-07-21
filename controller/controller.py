from typing import List

from views.view import View
from models.player import Player


class Controller:

    def __init__(self, view=View()):
        self.view = view
        #typé la variable ci-dessous en "self.players: List[Player]" ?
        self.players: List[Player] = []
        print(type(self.players))

    def generate_players(self):
        for x in range(8):
            first_name, last_name, birthday, gender = self.view.prompt_for_player_info()
            player = Player(first_name, last_name, birthday, gender)
            self.players.append(player)

    def show_players(self):
        for player in self.players:
            print(vars(player))

    def generate_tournament(self):
        pass

    def generate_pair_of_players(self):
        pass

    def bracket_list(self):
        pass

    def upper_bracket(self):
        pass

    def lower_bracket(self):
        pass






