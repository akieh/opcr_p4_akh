from controller.controller import Controller
from views.view import View


def main():
    view = View()
    controller = Controller(view)
    controller.generate_tournament()
    controller.generate_players()
    controller.show_players()
    controller.tournament.show_tournament_info()
    controller.bracket_list()


if __name__ == '__main__':
    main()
