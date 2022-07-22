class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description):
        #Il faut rajouter la liste des Indices correspondant aux instances du Joueur stockées en mémoire
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.number_of_rounds = 8
        self.description = description
        self.players_list = []
        self.rounds_list = []

    def add_players_in_tournament(self, player):
        self.players_list.append(player)

    def add_round_in_tournament(self, round):
        self.rounds_list.append(round)

    def show_tournament_info(self):
        print("Affichage des infos du tournoi: ")
        print(vars(self))
