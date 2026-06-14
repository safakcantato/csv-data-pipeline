with open("data.csv", "r") as file:
    header = file.readline().strip().split(",")

    for line in file:
        values = line.strip().split(",")

        person = {
            header[0]: values[0],
            header[1]: values[1],
            header[2]: values[2]
        }

        print(person)
