class Round:
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date
        self.end_date = None
        self.list_matchs = []

    def add_matchs_in_round(self, match):
        self.list_matchs.append(match)
