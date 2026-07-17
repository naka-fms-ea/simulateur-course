import random

minimum_integer = 1
maximum_integer = 6


def dice_roll():
    dice = random.randint(minimum_integer, maximum_integer)
    return dice


def create_grid_horses(nbhorses):
    grid_horses = [{"name": f"horse {i}", "speed": 0, "distance": 0, "rank": 0} for i in range(1, nbhorses + 1)]
    return grid_horses


if __name__ == '__main__':

    grid_speed_dice = [["", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]"],
                       [0, 0, 1, 1, 1, 2, 2],
                       [1, 0, 0, 1, 1, 1, 2],
                       [2, 0, 0, 1, 1, 1, 2],
                       [3, -1, 0, 0, 1, 1, 1],
                       [4, -1, 0, 0, 0, 1, 1],
                       [5, -2, -1, 0, 0, 0, 1],
                       [6, -2, -1, 0, 0, 0, "DQ"]]

    dict_distance_speed = {0: 0, 1: 23, 2: 46, 3: 69, 4: 92, 5: 115, 6: 138}

    while True:
        try:
            nb_horses = int(input("Nombre de chevaux : "))
            race_type = input("Type de la course : ")
        except ValueError:
            print("Entrer les données.")
            continue

        print(f"Nombre de chevaux : {nb_horses}")
        print(f"Type de la course : {race_type}")

        horses_list = create_grid_horses(nb_horses)

        list_win = []

        list_horses_ranking = []

        while len(list_horses_ranking) < nb_horses:
            for nb in range(len(horses_list)):
                print(f"{horses_list[nb]["name"]}")
                dice_integer = dice_roll()
                print(f"Lancer de dés : {dice_integer}")

                if grid_speed_dice[horses_list[nb]["speed"] + 1][dice_integer] == "DQ":
                    horses_list[nb]["rank"] = "DQ"
                    print(f"{horses_list[nb]["rank"]}")
                elif horses_list[nb]["distance"] < 2400:
                    horses_list[nb]["speed"] = horses_list[nb]["speed"] + grid_speed_dice[horses_list[nb]["speed"] + 1][dice_integer]
                    print(f"Vitesse : {horses_list[nb]["speed"]}")
                    horses_list[nb]["distance"] = horses_list[nb]["distance"] + dict_distance_speed[horses_list[nb]["speed"]]
                    print(f"Distance : {horses_list[nb]["distance"]}")

                if horses_list[nb]["distance"] >= 2400 and horses_list[nb]["rank"] != "DQ":
                    list_horses_ranking.append(horses_list[nb]["name"])

        print(f"Classement du {race_type} = {list_horses_ranking}")
