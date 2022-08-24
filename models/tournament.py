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

    def has_been_played(self, player_one, player_two):
        """
        Retourne True si player_one et player_two ont déjà joué ensemble
        sinon il retourne False
        """
        players_in_match = []
        matches = []
        for round_number, round in enumerate(self.rounds_list, start=1):
            list_player = []
            for match_number, match in enumerate(round.list_matchs, start=1):
                for player_number, player in enumerate(match, start=1):
                    list_player.append(player[0])
                if player_one in list_player:
                    if player_two in list_player:
                        return True
                list_player.clear()
        print(f"{player_one.full_name} et {player_two.full_name} n'ont jamais joué ensemble dans le round "
              f"{round_number}!")
        check = input("appuyez sur la touche 'Entrée' pour passer à la suite.")
        return False

    def update_tournament_rank(self):
        """Cette méthode permet de MAJ le classement des joueurs dans le tournoi.
        RANG/NOM/PRENOM/POINTS/CLASSEMENT INDIVIDUEL. Elle sera appelé chaque fois
        que l'utilisateur saisira les scores de chaque match
        La liste utilisée est celle contenant les joueurs dans le tournoi players_list"""
        self.players_list.sort(key=lambda x: (float(x.points), -int(x.rank)), reverse=True)
        for rank, player in enumerate(self.players_list):
            player.rank_in_tournament = rank + 1

    def ranking_tournament(self, player):
        """Cette méthode permet d'afficher le rang d'un joueur
        dans le tournoi. A ne pas confondre avec son classement général qui est
        externe au tournoi.
        """
        return self.players_list.index(player)

    def show_tournament_info(self):
        print(vars(self))
