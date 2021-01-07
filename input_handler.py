class CoordinatesInputError(Exception):
    pass

def input_coordinates():
    text = "Enter the coordinates (e.g.: b2): "

    while True:
        try:
            coordinates = input(text)
            
            if len(coordinates) != 2:
                raise CoordinatesInputError("Coordinates are from two characters. First is letter and second is number.")

            raw_x = coordinates[0]
            raw_y = coordinates[1]

            if raw_x.isnumeric():
                raise CoordinatesInputError("First coordinate must be a letter.")

            if raw_y.isnumeric() != True:
                raise CoordinatesInputError("Second coordinate must be a number.")

            # Horizontal (a, b, c...)
            x = str(raw_x).upper()
            # Vertical (1, 2, 3...)
            y = int(raw_y)

        except CoordinatesInputError as e:
            print(e)
            continue
        break

    return x, y