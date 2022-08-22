import random

from models.player import Player

exemple_tuple = (["juventus", "55 victoires", "22 défaites"], ["Inter", "3 victoires", "98 défaites"])

player_1 = Player("Abdellatif", "Khirdine", "04/06/1996", "M", 3)
player_2 = Player("Moustapha", "Khirdine", "26/07/1990", "M", 2)
player_3 = Player("Zakarya", "Khirdine", "06/01/1986", "M", 1)
player_4 = Player("Saltana", "Khirdine", "07/02/1964", "F", 4)

match_1 = ([player_1, 25, "nul"], [player_2, 30, "nul", "AH OUAIIIS"])
match_2 = ([player_1, 30, "toujours nul"], [player_3, "LOUUURD", 23])

list_match = [match_1, match_2]

players_in_match = [player_1, player_4]

exist = False

if player_1 and player_3 in players_in_match:
    exist = True
print(exist)

number = len(players_in_match)

print(players_in_match)

"""for i in range(10):
    print("Voici le i: " + str(i))
    if i == 5:
        break
print("Fin boucle")

exist = False
count = 0
for ele in exemple_tuple:
    print("voici le ele:" + str(ele))
    if "22 défaites" in ele:
        print("PRESENT !")
        exist = True
    else:
        print("TOUJOURS PAS : " + str(count))
    count += 1

print(f"taille du tuple = {len(exemple_tuple)}")


print(f"La Juventus est nul au niveau de {number}")"""
"""boucle = 0

for match in list_match:
    for player in match:
        players_in_match.append(player[0])
    if player_1 and player_2 in players_in_match:
        print("il y est")
        print(players_in_match[0].full_name)
        print(players_in_match[1].full_name)
    players_in_match.clear()
    print("la boucle: " + str(boucle))
    boucle += 1

for player in enumerate(players_in_match):
    print(player[1].full_name)"""


"""for elem in exemple_tuple:
    if "juventus" in elem:
        print("Premier Présent Juve")
    if "Inter" in elem:
        print("Premier Présent Inter")

for elem in exemple_tuple:
    if "Inter" and "juventus" in elem:
        print("Deuxieme les 2 présents")
    else:
        print("pas présent")
"""