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
        print(f"Nous allons voir si {player_one.full_name} et {player_two.full_name} ont déjà "
              f" joué ensemble !")
        matches = []
        for round_number, round in enumerate(self.rounds_list, start=1):
            list_player = []
            for match_number, match in enumerate(round.list_matchs, start=1):
                for player_number, player in enumerate(match, start=1):
                    #print(f"Récupération de l'instance {player_number} de joueur du match {match_number} du round {round_number}")
                    list_player.append(player[0])
                check = input("appuyez sur la touche 'Entrée' pour passer à la suite.")
                for player in list_player:
                    print(f"Joueur du match {match_number} : {player.full_name}")
                print("Vérification de la présence du joueur P1  match")
                if player_one in list_player:
                    print("Vérification de la présence du joueur P2  match")
                    if player_two in list_player:
                        print("Le joueur P1 et P2 est dans ce match.")
                        return True
                else:
                    print("Le joueur P1 n'est pas dans ce match.")
                list_player.clear()
                check = input("appuyez sur la touche 'Entrée' pour passer à la suite.")
            print(f"{player_one.full_name} et {player_two.full_name} n'ont jamais joué ensemble !")
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
