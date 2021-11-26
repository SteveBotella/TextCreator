import os


def main():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    text_file = os.path.join(this_folder, 'text.txt')
    run_options = True

    while run_options:
        text_check = input("Choose action : create, add, read or quit")
        if text_check == "create":
            create_text = input("Your text : ")
            with open('text.txt', 'w') as file:
                file.write(f"{create_text} \n")
                file.close()
        if text_check == "add":
            add_text = input("Your text : ")
            with open('text.txt', 'a') as file:
                file.write(add_text + "\n")
                file.close()
        if text_check == "read":
            with open('text.txt', 'r') as file:
                read = file.readlines()
                file.close()
            line_number = -1
            input_next = True
            while input_next:
                next_line = input("Press S to display next line or Q to quit")
                if next_line == "s":
                    line_number = line_number + 1
                    print(read[line_number])
                if next_line == "q":
                    input_next = False

        if text_check == "quit":
            run_options = False


if __name__ == '__main__':
    main()
