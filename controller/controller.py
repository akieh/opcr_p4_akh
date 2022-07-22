from typing import List

from views.view import View
from models.player import Player
from models.tournament import Tournament


class Controller:

    def __init__(self, view=View()):
        self.tournament = None
        self.view = view
        # typé la variable ci-dessous en "self.players: List[Player]" ?
        self.players: List[Player] = []
        print(type(self.players))

    def generate_players(self):
        for x in range(8):
            print("Saisissez les informations du joueur numéro ", x + 1)
            first_name, last_name, birthday, gender, rank = self.view.prompt_for_player_info()
            player = Player(first_name, last_name, birthday, gender, rank)
            self.players.append(player)
            self.tournament.add_players_in_tournament(player)

    def show_players(self):
        print("Affichage des infos des joueurs: ")
        for player in self.players:
            print(vars(player))

    def generate_tournament(self):
        print("Saisissez les informations du tournoi: ")
        name_tournament, place_tournament, start_date_tournament, end_date_tournament, time_control_tournament, \
        description_tournament = self.view.prompt_for_tournament_info()
        self.tournament = Tournament(name_tournament, place_tournament, start_date_tournament, end_date_tournament,
                                     time_control_tournament, description_tournament)

    def show_tournament_info(self):
        print("Affichage des infos du tournoi: ")
        print(vars(self.tournament))

    def generate_pair_of_players(self):
        pass

    def bracket_list(self):
        pass

    def upper_bracket(self):
        pass

    def lower_bracket(self):
        pass
