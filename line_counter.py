line_number = 0

with open("lyrics.txt", "r") as file:
    for each_line in file:
        if every_line == "\n":
            empty_line_counter = empty_line_counter +1


        elif every_line.startswith("["):
            section_label_counter = section_label_counter +1

        else:
            line_counter = line_counter + 1


        print("the total lines in the song: ", line_counter)
        print("the total EMPTY lines:", empty_line_)