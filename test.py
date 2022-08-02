from operator import attrgetter
import time

from models.tournament import Tournament
from models.player import Player
from models.round import Round



tournoi = Tournament("Golden Wind", "Maroc", "01/01/2022", "01/01/2022", "Blitz", "Aucune description, c'est au Maroc ca suffit")

player_1 = Player("Abdellatif", "Khirdine", "04/06/1996", "M", 3)
player_2 = Player("Moustapha", "Khirdine", "26/07/1990", "M", 2)
player_3 = Player("Zakarya", "Khirdine", "06/01/1986", "M", 1)
player_4 = Player("Saltana", "Khirdine", "07/02/1964", "F", 4)
player_5 = Player("El Hachemi", "Khirdine", "01/01/1946", "M", 5)
player_6 = Player("Ahmed", "Khirdine", "06/01/1900", "M", 6)
player_7 = Player("Mbarek", "Khirdine", "04/06/1860", "M", 7)
player_8 = Player("Himd", "Khirdine", "04/06/1880", "M", 8)


#print(tournoi.show_tournament_info())

"""une_list = ["Numéro 0", "Numéro 1", "Numéro 2"]

print("Initial")
print(une_list[1])
print(une_list[0])
print("Changement")
une_list[0], une_list[1] = une_list[1], une_list[0]
print(une_list[1])
print(une_list[0])"""


"""list_joueurs = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
for player in list_joueurs:
    print(f"Le jouer {player.first_name} est au rang {player.rank}.")

list_joueurs.sort(key=attrgetter('rank'))
print("Apres le sort: ")

for player in list_joueurs:
    print(f"Le joueur {player.first_name} est au rang {player.rank}.")"""

"""def bracket_list(liste):
    upper_bracket = []
    lower_bracket = []
    for player in liste:
        if player.rank <= 4:
            upper_bracket.append(player)
        else:
            lower_bracket.append(player)
    upper_bracket.sort(key=attrgetter("rank"))
    lower_bracket.sort(key=attrgetter("rank"))
    print("Affichage du UPPER")
    for player in upper_bracket:
        print(f"Le joueur {player.first_name} est au rang {player.rank}.")
    print("Affichage du LOWERR")
    for player in lower_bracket:
        print(f"Le joueur {player.first_name} est au rang {player.rank}.")

print("Utilisation de la fonction BRACKET_LIST()")
bracket_list(list_joueurs)"""

"""premier_tuple = (["Sidi Naser", "Maroc", 25], ["Agouliz,", "Maroc", 22])
print("Element de Sidi Naser le score: ", premier_tuple[0][2])
premier_tuple[0][2] = 28
print("Changement de Sidi Naser le score: ", premier_tuple[0][2])"""

une_autre_list = [25, 78, "Arrête !", None, None, "Juv"]

for x in une_autre_list:
    time.sleep(3)
    print(f"Valeur de x : {x} . Et voici la longueur {len(une_autre_list)}")
