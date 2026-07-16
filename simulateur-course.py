import random

minimum_integer = 1
maximum_integer = 6


def dice_roll():
    dice = random.randint(minimum_integer, maximum_integer)
    return dice


def create_grid_horses(nbhorses):
    grid_horses = [{"name": f"horse {i}", "speed": 0, "distance": 0} for i in range(1, nbhorses + 1)]
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

        dice_integer = dice_roll()

        print(f"Résultat du dés : {dice_integer}")

        horses_list = create_grid_horses(nb_horses)

        print(f"Liste des chevaux : {horses_list}")
