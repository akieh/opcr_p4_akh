class View:
    """View to get info of players, tournament or ranking """

    def prompt_for_player_info(self):
        """Getting the info of players with prompt"""
        first_name = input("Entrez le nom du joueur : ")
        last_name = input("Entrez le prenom du joueur : ")
        birthday = input("Entrez la date de naissance du joueur : ")
        gender = input("Entrez le sexe du joueur : ")
        return first_name, last_name, birthday, gender

    def prompt_for_tournament_info(self):
        pass

    """Ici, il faudra faire l'affichage des différents Rapports. Une autre classe View_Rapport ? """


