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
        pass

    def update_general_rank(self):
        """Cette méthode permet de MAJ le classement des joueurs dans le tournoi.
        RANG/NOM/PRENOM/POINTS/CLASSEMENT INDIVIDUEL. Elle sera appelé chaque fois
        que l'utilisateur saisira les scores de chaque match"""
        self.players_list.sort(key=lambda x: (float(x.points), -int(x.rank)), reverse=True)
        """index = 1
        for player in self.players_list:
            if player.points == self.players_list[index].points \
                    and player.rank_in_tournament < self.players_list[index].rank_in_tournament:
                self.players_list.insert(index, self.players_list.pop(index - 1))"""
        print("Mise à jour du classement du tournoi")

        for rank, player in enumerate(self.players_list):
            player.rank_in_tournament = rank + 1
            print(f"{player.full_name} est classé  {str(player.rank_in_tournament)} "
                  f"et il a {str(player.points)} points. Son rang général est {player.rank}.")

    def ranking_tournament(self, player):
        """Cette méthode permet d'afficher le rang d'un joueur
        dans le tournoi. A ne pas confondre avec son classement général qui est
        externe au tournoi.
        """
        pass

    def show_tournament_info(self):
        print(vars(self))
