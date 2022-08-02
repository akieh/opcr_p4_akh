import time


class View:
    """View to get info of players, tournament or ranking """

    def game_menu(self):
        print("Bienvenue dans le programme d'Echec !")

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

    def start_of_tournament(self):
        """Cette méthode indique à l'utilisateur que le tournoi est prêt à être lancer
        et lui demande d'appuyer sur entrée pour démarrer le tournoi (premier round"""
        next_step = False
        while next_step == False:
            check = input("Le tournoi est prêt à commencer. Appuyez sur la touche 'Entrée' afin de lancer le premier round")
            if check == "":
                next_step = True
                return next_step
            else:
                print("Vous avez saisi un texte avant d'appuyer sur entrée.")

    def prompt_for_player_info(self, number_player):
        """Getting the info of players with prompt"""
        print("Merci de saisir les informations du joueur numéro ", number_player)
        first_name = input("Saisissez le nom du joueur :")
        last_name = input("Saisissez le prenom du joueur : ")
        birthday = input("Saisissez la date de naissance du joueur : ")
        gender = input("Saisissez le sexe du joueur : ")
        rank = int(input("Saisissez le rang du joueur: "))
        return first_name, last_name, birthday, gender, rank

    def prompt_for_first_round(self):
        print("Début du premier round !")
        time.sleep(3)

    def prompt_for_score(self, player_one, player_two):
        print(f"Le match entre {player_one.full_name} et {player_two.full_name} est terminé.")
        winner = input(f"Merci de saisir le gagnant. Si c'est {player_one.full_name}, entrez le chiffre 1.\n"
                       f"Si c'est {player_two.full_name}, entrez le chiffre 2. ")
        return winner

    def show_list_matchs(self, list_match):
        print("Voici les rencontres pour ce round : ")
        number_of_match = 1
        for match in list_match:
            player_one = match[0][0]
            player_two = match[1][0]
            print(f"Match n° {number_of_match} sera {player_one.full_name} VS {player_two.full_name}.")
            number_of_match += 1

    """Ici, il faudra faire l'affichage des différents Rapports. Une autre classe View_Rapport ? """
