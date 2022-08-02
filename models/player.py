class Player:
    def __init__(self, first_name, last_name, birthday, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    def get_rank(self):
        return self.rank

    def info_player(self):
        """Show the info of the players, méthode __repr__ ?"""
        pass

    def update_ranking(self, new_rank):
        """"Ranking update by the person in charge"""
        self.rank = new_rank
