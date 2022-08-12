class Tournament:
    number_of_rounds = 4

    def __init__(self, name, place, start_date, end_date, time_control, description):
        #Il faut rajouter la liste des Indices correspondant aux instances du Joueur stockées en mémoire
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.number_of_rounds = Tournament.number_of_rounds
        self.description = description
        self.players_list = []
        self.rounds_list = []

    def add_players_in_tournament(self, player):
        self.players_list.append(player)

    def add_round_in_tournament(self, round):
        self.rounds_list.append(round)

    def has_played(self, player_one, player_two):
        players_in_match = []
        for round in self.rounds_list:
            for match in round:
                for player in match:
                    players_in_match.append(player[0])
                if player_one and player_two in players_in_match:
                    return True
        return False



    def update_tournament_rank(self):
        """Cette méthode permet de MAJ le classement des joueurs dans le tournoi.
        RANG/NOM/PRENOM/POINTS/CLASSEMENT INDIVIDUEL. Elle sera appelé chaque fois
        que l'utilisateur saisira les scores de chaque match
        La liste utilisée est celle contenant les joueurs dans le tournoi players_list"""
        self.players_list.sort(key=lambda x: (float(x.points), -int(x.rank)), reverse=True)
        for rank, player in enumerate(self.players_list):
            player.rank_in_tournament = rank + 1
            print(f"{player.full_name} est classé  {str(player.rank_in_tournament)} "
                  f"et il a {str(player.points)} points. Son rang général est {player.rank}.")

    def ranking_tournament(self, player):
        """Cette méthode permet d'afficher le rang d'un joueur
        dans le tournoi. A ne pas confondre avec son classement général qui est
        externe au tournoi.
        """
        return self.players_list.index(player)

    def show_tournament_info(self):
        print(vars(self))
