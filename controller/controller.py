from typing import List
from operator import attrgetter
import datetime

from views.view import View
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.rank_player import RankPlayer


class Controller:

    def __init__(self, view=View()):
        self.tournament = None
        self.view = view
        #Je vois pas l'utilité de cette liste de joueurs.
        self.players: List[Player] = []

    def generate_players(self):
        for x in range(8):
            first_name, last_name, birthday, gender, rank = self.view.prompt_for_player_info(x+1)
            player = Player(first_name, last_name, birthday, gender, rank)
            #05/08 le premier 0 correspond au point dans le tournoi et le None son rang dans le tournoi
            self.players.append(player)
            #07/08 le premier 0 correspond au point dans le tournoi et le None son rang dans le tournoi
            player.rank_in_tournament = x+1
            self.tournament.add_players_in_tournament(player)
        self.tournament.update_general_rank()

    def generate_tournament(self):
        """Création du tournoi et ajout des joueurs dans le tournoi"""
        print("Saisissez les informations du tournoi: ")
        name_tournament, place_tournament, start_date_tournament, end_date_tournament, time_control_tournament, \
        description_tournament = self.view.prompt_for_tournament_info()
        self.tournament = Tournament(name_tournament, place_tournament, start_date_tournament, end_date_tournament,
                                     time_control_tournament, description_tournament)

    def generate_first_round(self):
        self.view.annoucement_first_round()
        upper_bracket, lower_bracket = self.bracket_list()
        round = Round("Round 1", datetime.datetime.now())
        for i in range(len(upper_bracket)):
            #l'indice du joueur, son score qui est à None qui sera inscrit à la fin
            match = ([upper_bracket[i], None], [lower_bracket[i], None])
            round.add_matchs_in_round(match)
        self.tournament.add_round_in_tournament(round)
        #METTRE ICI UNE VUE POUR AFFICHER LA LISTE DES MATCHS DU ROUND
        print("Affichage des matchs")
        self.view.start_of_first_round(round.list_matchs)
        self.tournament.end_date = datetime.datetime.now()
        #ET INSERER LES SCORES SAISIES PAR LUTILISATEUR
        for match in round.list_matchs:
            player_one = match[0][0]
            player_two = match[1][0]
            #saisie des indices pour réucpérer les scores
            match[0][1], match[1][1] = self.view.prompt_for_score(player_one, player_two)
            if match[0][1] > match[1][1]:
                player_one.points += 1
                print(f"Le gagnant est {player_one.full_name} !")
            elif match[0][1] < match[1][1]:
                player_two.points += 1
                print(f"Le gagnant est {player_two.full_name} !")
            else:
                player_one.points += 0.5
                player_two.points += 0.5
                print("MATCH NUL !")
        #ET ENSUITE JE METS A JOUR LE CLASSEMENT
        self.tournament.update_general_rank()

    def bracket_list(self):
        upper_bracket = []
        lower_bracket = []
        for player in self.tournament.players_list:
            if player.rank <= 4:
                upper_bracket.append(player)
            else:
                lower_bracket.append(player)
        #Ordonner la liste : le premier est au début de la liste, le dernier à la fin..
        upper_bracket.sort(key=attrgetter("rank"))
        lower_bracket.sort(key=attrgetter("rank"))
        return upper_bracket, lower_bracket

    def generate_pair_of_players(self):
        """Création des paires de joueurs pour un tour après le premier tour, donc TOUR 2,3 et 4"""
        upper_bracket, lower_bracket = self.bracket_list()

    def generate_round(self):
        pass

    def show_players(self):
        print("Affichage des infos des joueurs: ")
        for player in self.tournament.players_list:
            print(vars(player))
