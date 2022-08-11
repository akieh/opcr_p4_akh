import datetime

from controller.controller import Controller
from views.view import View
from models import match, player, round, tournament


def main():
    view = View()
    controller = Controller(view)
    controller.tournament = tournament.Tournament("Turin Tournament", "Italie"
                                                  , datetime.date.today(), datetime.date.today(),
                                                  "Blitz", " Pas de description")

    player_1 = player.Player("Abdellatif", "Khirdine", "04/06/1996", "M", 8)
    player_2 = player.Player("Jacques", "Joes", "07/07/1990", "M", 2)
    player_3 = player.Player("Miro", "Mello", "01/01/1986", "M", 1)
    player_4 = player.Player("Pierre", "Henri", "01/01/1946", "M", 3)
    player_5 = player.Player("Pavel", "Toei", "04/06/1964", "F", 4)
    player_6 = player.Player("Exa", "Mus", "04/06/1900", "M", 5)
    player_7 = player.Player("Free", "Lobe", "04/06/1946", "M", 6)
    player_8 = player.Player("Sonny", "Sung", "04/06/1994", "M", 7)

    controller.tournament.add_players_in_tournament(player_1)
    controller.tournament.add_players_in_tournament(player_2)
    controller.tournament.add_players_in_tournament(player_3)
    controller.tournament.add_players_in_tournament(player_4)
    controller.tournament.add_players_in_tournament(player_5)
    controller.tournament.add_players_in_tournament(player_6)
    controller.tournament.add_players_in_tournament(player_7)
    controller.tournament.add_players_in_tournament(player_8)

    controller.tournament.update_general_rank()

    #controller.show_players()
    #controller.tournament.show_tournament_info()
    start_of_tournament = controller.view.start_of_tournament()
    if start_of_tournament:
        controller.generate_first_round()


if __name__ == '__main__':
    main()
