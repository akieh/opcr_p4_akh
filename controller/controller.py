from typing import List
from operator import attrgetter

from views.view import View
from models.player import Player
from models.tournament import Tournament
from models.round import Round


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
        """Création du tournoi et ajout des joueurs dans le tournoi"""
        print("Saisissez les informations du tournoi: ")
        name_tournament, place_tournament, start_date_tournament, end_date_tournament, time_control_tournament, \
        description_tournament = self.view.prompt_for_tournament_info()
        self.tournament = Tournament(name_tournament, place_tournament, start_date_tournament, end_date_tournament,
                                     time_control_tournament, description_tournament)

    def generate_first_round(self):
        upper_bracket, lower_bracket = self.bracket_list()
        """Ce qu'il y a faire : je cr"""

    def generate_round(self):
        pass

    def bracket_list(self):
        upper_bracket = []
        lower_bracket = []
        for player in self.players:
            if player.rank <= 4:
                upper_bracket.append(player)
            else:
                lower_bracket.append(player)
        #Ordonner la liste : le premier est au début de la liste, le dernier à la fin..
        upper_bracket.sort(key=attrgetter("rank"))
        lower_bracket.sort(key=attrgetter("rank"))
        return upper_bracket, lower_bracket

    def generate_pair_of_players(self):
        """Création des paires de joueurs pour un tour"""
        upper_bracket, lower_bracket = self.bracket_list()
