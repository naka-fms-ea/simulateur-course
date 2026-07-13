if __name__ == '__main__':

grid_speed_dice = [["","[1]", "[2]", "[3]", "[4]", "[5]", "[6]"],
                   [0, 0, 1, 1, 1, 2, 2],
                   [1, 0, 0, 1, 1, 1, 2],
                   [2, 0, 0, 1, 1, 1, 2],
                   [3, -1, 0, 0, 1, 1, 1],
                   [4, -1, 0, 0, 0, 1, 1],
                   [5, -2, -1, 0, 0, 0, 1],
                   [6, -2, -1, 0, 0, 0, "DQ"]]

    while True:
        try:
            nb_horses = input("Nombre de chevaux : ")
            race_type = input("Type de la course : ")
        except ValueError:
            print("Entrer les données.")
            continue