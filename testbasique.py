import random

from models.player import Player

exemple_tuple = (["juventus", "55 victoires", "22 défaites"], ["Inter", "3 victoires", "98 défaites"])

print(exemple_tuple[0][2], exemple_tuple[0][1])
print(exemple_tuple[1][2])

list_une = [["Juventus", 5], ["Inter", 2], ["Nap-oli", 3]]
list_deux = []

player_1 = Player("Abdellatif", "Khirdine", "04/06/1996", "M", 8)
player_2 = Player("Moustapha", "Khirdine", "07/07/1990", "M", 2)
player_3 = Player("Zakarya", "Khirdine", "01/01/1986", "M", 1)
player_4 = Player("El Hachemi", "Khirdine", "01/01/1946", "M", 3)

list_deux.append(player_1)
list_deux.append(player_2)
list_deux.append(player_3)
list_deux.append(player_4)
"""random.shuffle(list_deux)

for player in list_deux:
    count = 0
    if player == player_1:
        print(player.full_name, "L'index: ", list_deux[count])
        player.full_name += "!"
    else:
        print(player.full_name, "Il n'y est pas", list_deux[count])
    count += 1

if player_1 in list_deux:
    print("present")"""

