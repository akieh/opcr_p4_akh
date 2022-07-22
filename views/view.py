class View:
    """View to get info of players, tournament or ranking """

    def prompt_for_tournament_info(self):
        """Getting the info of tournament"""
        name_tournament = input("Saisissez le nom du tournoi : ")
        place_tournament = input("Saisissez le lieu du tournoi : ")
        start_date_tournament = input("Saisissez la date de début du tournoi: ")
        end_date_tournament = input("Saisissez la date de fin du tournoi: ")
        time_control_tournament = input("Saisissez le type de contrôle du temps du tournoi: ")
        description_tournament = input("Saisissez la description du tournoi: ")
        return name_tournament, place_tournament, start_date_tournament, end_date_tournament, \
               time_control_tournament, description_tournament

    def prompt_for_player_info(self):
        """Getting the info of players with prompt"""
        first_name = input("Saisissez le nom du joueur : ")
        last_name = input("Saisissez le prenom du joueur : ")
        birthday = input("Saisissez la date de naissance du joueur : ")
        gender = input("Saisissez le sexe du joueur : ")
        rank = input("Saisissez le rang du joueur: ")
        return first_name, last_name, birthday, gender, rank

    """Ici, il faudra faire l'affichage des différents Rapports. Une autre classe View_Rapport ? """
