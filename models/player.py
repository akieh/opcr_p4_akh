class Player:
    def __init__(self, first_name, last_name, birthday, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        """Correspond au point et classement du joueur dans le tournoi
        Il faudra le changer à l'avenir de sorte à avoir plusieurs
        objets "points" correspondant aux points d'un joueur
        dans un tournoi aisni que son rang dans ce tournoi"""
        self.points = 0
        self.rank_in_tournament = 0

    def get_rank(self):
        return self.rank

    def update_ranking(self, new_rank):
        """"Ranking update by the person in charge"""
        self.rank = new_rank
