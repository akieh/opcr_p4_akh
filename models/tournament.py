class Tournament:
    def __init__(self, name, place, start_date, end_date, time_control, description):
        #Il faut rajouter la liste des Indices correspondant aux instances du Joueur stockées en mémoire
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.number_of_rounds = 4
        self.description = description
        self.players_list = []
        self.rounds_list = []
        self.ranking_players = None

    def add_players_in_tournament(self, player):
        self.players_list.append(player)

    def add_round_in_tournament(self, round):
        self.rounds_list.append(round)

    def general_rank(self):
        """Cette méthode permet d'afficher le classement des joueurs dans le tournoi.
        RANG/NOM/PRENOM/POINTS/CLASSEMENT INDIVIDUEL"""
        pass

    def ranking_tournament(self, player):
        """Cette méthode permet d'afficher le rang d'un joueur
        dans le tournoi. A ne pas confondre avec son classement général qui est
        externe au tournoi.
        """
        pass

    def show_tournament_info(self):
        print("Affichage des infos du tournoi: ")
        print(vars(self))
