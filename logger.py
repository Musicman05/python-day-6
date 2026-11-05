def question():
    who_are_you = input("what is your name")

with open("guest_list.txt", "a") as file:
    file.write(who_are_you + "\n")
    