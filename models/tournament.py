class Tournament:
    def __init__(self, name, lieu, date, time_control, number_of_rounds, description):
        self.name = name
        self.lieu = lieu
        self.date = date
        self.time_control = time_control
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.players_list = []
        self.rounds_list = []

    def add_players_in_tournament(self, player):
        self.players_list.append(player)

    def add_round_in_tournament(self, round):
        self.rounds_list.append(round)
