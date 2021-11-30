import os
import csv


class Student:
    def __init__(self, name, age, score):
        self.id = None
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


def menu_display(full=True):
    os.system("clear")
    print("Actions list:")
    if not full:
        print("1 - Add")
        print("0 - Quit")
        print("(!) The student list is empty")
    else:
        print("1 - Add")
        print("2 - Print")
        print("3 - Edit")
        print("4 - Delete")
        print("5 - Search")
        print("6 - Sort")
        print("7 - Stats")
        print("8 - Save")
        print("9 - Validate")
        print("0 - Quit")


def fix_missing(students):
    for index, student in enumerate(list(students)):
        if student.count("") == len(student):
            students.remove(student)
            continue

        while len(student) != 4:
            student.append("")

        if student[0] == "":
            students[index][0] = "000000"

        if student[1] == "":
            students[index][1] = "_"

        if student[2] == "":
            students[index][2] = "0"

        if student[3] == "":
            students[index][3] = "-1"


def find_error(students):
    errors = []
    for student in students:
        try:
            int(student[0])
        except ValueError:
            if student not in errors:
                errors.append(student)

        try:
            int(student[2])
        except ValueError:
            if student not in errors:
                errors.append(student)

        try:
            float(student[3])
        except ValueError:
            if student not in errors:
                errors.append(student)

        err = (
            student[0] == "000000"
            or student[1] == "_"
            or student[2] == "0"
            or student[3] == "-1"
        )

        if err and student not in errors:
            errors.append(student)

    return errors


def validate_input(message, type=None):
    usr_input = None
    while True:
        try:
            if type == "int":
                usr_input = int(input(message))
            if type == "float":
                usr_input = float(input(message))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return usr_input


def student_display(students):
    if len(students) == 0:
        print("There are no students.")
        return

    len_of_id = []
    len_of_name = []
    len_of_age = []
    len_of_score = []

    for student in students:
        len_of_id.append(len(student[0]))
        len_of_name.append(len(student[1]))
        len_of_age.append(len(student[2]))
        len_of_score.append(len(student[3]))

    no_len = len(str(len(students))) + 1 if len(str(len(students))) > 4 else 4
    id_len = max(len_of_id) + 1 if max(len_of_id) > 7 else 7
    name_len = max(len_of_name) + 1 if max(len_of_name) > 19 else 19
    age_len = max(len_of_age) + 1 if max(len_of_age) > 7 else 7
    score_len = max(len_of_score) + 1 if max(len_of_score) > 7 else 7

    print(
        "\t+-"
        + "-" * no_len
        + "+-"
        + "-" * id_len
        + "+-"
        + "-" * name_len
        + "+-"
        + "-" * age_len
        + "+-"
        + "-" * score_len
        + "+"
    )
    print(
        "\t| "
        + "No.".ljust(no_len)
        + "| "
        + "ID".ljust(id_len)
        + "| "
        + "Name".ljust(name_len)
        + "| "
        + "Age".ljust(age_len)
        + "| "
        + "Score".ljust(score_len)
        + "|"
    )
    print(
        "\t+-"
        + "-" * no_len
        + "+-"
        + "-" * id_len
        + "+-"
        + "-" * name_len
        + "+-"
        + "-" * age_len
        + "+-"
        + "-" * score_len
        + "+"
    )

    for index, student in enumerate(students):
        print(
            f"\t| {str(index+1).ljust(no_len)}| {student[0].ljust(id_len)}| {student[1].ljust(name_len)}| {student[2].ljust(age_len)}| {student[3].ljust(score_len)}|"
        )

    print(
        "\t+-"
        + "-" * no_len
        + "+-"
        + "-" * id_len
        + "+-"
        + "-" * name_len
        + "+-"
        + "-" * age_len
        + "+-"
        + "-" * score_len
        + "+"
    )


def search_student(students):
    result = []
    while True:
        print("Which student?")
        print("\t(!) 1. Search By ID")
        print("\t(!) 2. Search By Name")
        print("\t(!) 3. Search By Age")
        print("\t(!) 4. Search By Score")
        option = input("\t(?) Option: ")
        if option == "1":
            std_id = input("Input the student ID: ")
            result = [std for std in students if std_id.lower() == std[0].lower()]
            break

        if option == "2":
            str_of_name = input("Input the characters: ")
            result = [std for std in students if str_of_name.lower() in std[1].lower()]
            break

        elif option == "3":
            num_of_age = input("Input the age: ")
            result = [std for std in students if num_of_age.lower() == std[2].lower()]
            break

        elif option == "4":
            num_of_score = input("Input the score: ")
            result = [std for std in students if num_of_score.lower() == std[3].lower()]
            break

        else:
            continue

    return result


def main():
    students = []
    errors = []
    if not os.path.exists("data.csv"):
        open("data.csv", "w").close()
    else:
        with open("data.csv", "r") as data:
            lines = data.read().strip().split("\n")
            students = [line.split(",") for line in lines]

    while True:
        fix_missing(students)
        errors = find_error(students)

        menu_display(full=False) if len(students) == 0 else menu_display()

        command = input("Enter command: ")

        if command in ("2", "3", "4", "5", "6", "7", "8", "9") and len(students) == 0:
            continue

        # match - case
        # (1)-ADD----------------------------------------------------
        elif command == "1":
            print("[1] Add:")
            if len(students) == 0:
                std_id = "000001"
            else:
                try:
                    lst_of_id = [int(student[0]) for student in students]
                    std_id = f"{max(lst_of_id)+1:06d}"
                    name = input("Enter name: ")
                    age = validate_input("Enter age: ", type="int")
                    score = validate_input("Enter score: ", type="float")
                    students.append([std_id, name, str(age), str(score)])
                    print("ADDED")
                except ValueError:
                    print("There is an error in the student list")

        # (2)-PRINT--------------------------------------------------
        elif command == "2":
            print("[2] Print:")
            student_display(students)

        # (3)-EDIT---------------------------------------------------
        elif command == "3":
            print("[3] Edit:")
            result = []
            while len(result) != 1:
                result = search_student(students)
                student_display(result)
                if len(result) != 1:
                    ask = input("Press 0 to main menu...")
                    if ask == "0":
                        break

            while len(result) == 1:
                index = students.index(result[0])
                print("Which property need to be updated?")
                print("\t(!) 1. Name")
                print("\t(!) 2. Age")
                print("\t(!) 3. Score")
                print("\t(!) 0. Back to main menu")
                option = input("\t(?) Option: ")
                if option == "1":
                    name = input("Please enter name you want to change: ")
                    students[index][1] = name
                    print("Name editted")
                    break

                elif option == "2":
                    age = validate_input(
                        "Please enter age you want to change: ", type="int"
                    )
                    students[index][2] = str(age)
                    print("Age editted")
                    break

                elif option == "3":
                    score = validate_input(
                        "Please enter score you want to change: ", type="float"
                    )
                    students[index][3] = str(score)
                    print("Score editted")
                    break

                elif option == "0":
                    break

                else:
                    continue

        # (4)-DELETE-------------------------------------------------
        elif command == "4":
            print("[4] Delete:")
            result = []
            while True:
                if len(errors) != 0:
                    print("There is an error in the student list.")
                    ask = input(
                        "Do you want to remove all errors in student list (y/n)? "
                    )
                    if ask == "y":
                        result = list(errors)
                        break
                    elif ask == "n":
                        print("Keep searching")
                        result = search_student(students)
                        break
                    else:
                        continue
                else:
                    result = search_student(students)
                    break

            print("Student(s) found:")
            student_display(result)
            while True:
                confirm = input("Are you sure to delete (y/n)? ")
                if confirm == "y":
                    for std in result:
                        students.pop(int(students.index(std)))
                    errors = []
                    print("DELETED")
                    break
                if confirm == "n":
                    break
                else:
                    continue

        # (5)-SEARCH-------------------------------------------------
        elif command == "5":
            print("[5] Search:")
            result = search_student(students)
            if len(result) != 0:
                print("Student(s) found:")
                student_display(result)
            else:
                print("Not found.")

        # (6)-SORT---------------------------------------------------
        elif command == "6":
            print("[6] Sort:")
            try:
                while True:
                    print("How to sort?")
                    print("\t(!) 1. By ID")
                    print("\t(!) 2. By Name")
                    print("\t(!) 3. By Age")
                    print("\t(!) 4. By Score")
                    option = input("\t(?) Option: ")
                    if option == "1":
                        while True:
                            print("\t(!) 1. Ascending")
                            print("\t(!) 2. Descending")
                            select = input("\t(?) Select: ")
                            if select == "1":
                                students.sort(key=lambda x: int(x[0]))
                                break
                            elif select == "2":
                                students.sort(key=lambda x: int(x[0]), reverse=True)
                                break
                            else:
                                continue
                        break

                    elif option == "2":
                        while True:
                            print("\t(!) 1. Ascending")
                            print("\t(!) 2. Descending")
                            select = input("\t(?) Select: ")
                            if select == "1":
                                students.sort(
                                    key=lambda x: (
                                        x[1].lower(),
                                        int(x[2]),
                                        float(x[3]),
                                    )
                                )
                                break
                            elif select == "2":
                                students.sort(
                                    key=lambda x: (
                                        x[1].lower(),
                                        int(x[2]),
                                        float(x[3]),
                                    ),
                                    reverse=True,
                                )
                                break
                            else:
                                continue
                        break

                    elif option == "3":
                        while True:
                            print("\t(!) 1. Ascending")
                            print("\t(!) 2. Descending")
                            select = input("\t(?) Select: ")
                            if select == "1":
                                students.sort(
                                    key=lambda x: (
                                        int(x[2]),
                                        x[1].lower(),
                                        float(x[3]),
                                    )
                                )
                                break
                            elif select == "2":
                                students.sort(
                                    key=lambda x: (
                                        int(x[2]),
                                        x[1].lower(),
                                        float(x[3]),
                                    ),
                                    reverse=True,
                                )
                                break
                            else:
                                continue
                        break

                    elif option == "4":
                        while True:
                            print("\t(!) 1. Ascending")
                            print("\t(!) 2. Descending")
                            select = input("\t(?) Select: ")
                            if select == "1":
                                students.sort(
                                    key=lambda x: (
                                        float(x[3]),
                                        x[1].lower(),
                                        int(x[2]),
                                    )
                                )
                                break
                            elif select == "2":
                                students.sort(
                                    key=lambda x: (
                                        float(x[3]),
                                        x[1].lower(),
                                        int(x[2]),
                                    ),
                                    reverse=True,
                                )
                                break
                            else:
                                continue
                        break

                    else:
                        continue

                student_display(students)
            except ValueError:
                print("There is an error in the student list.")

        # (7)-STATS--------------------------------------------------
        elif command == "7":
            print("[7] Statistics:")
            sum_of_score = 0
            excel = []
            good = []
            bad = []

            try:
                for student in students:
                    sum_of_score += float(student[3])
                    if float(student[3]) >= 8:
                        excel.append(student)
                    elif float(student[3]) >= 7 and float(student[3]) < 8:
                        good.append(student)
                    else:
                        bad.append(student)

                top_score = max([float(x[3]) for x in excel])
                top_std = [x[1] for x in excel if float(x[3]) == top_score]

                print(f"Diem trung binh ca lop: {round(sum_of_score/len(students),2)}")
                print(
                    f"Ti le sinh vien gioi: {round(float(len(excel)/len(students)),2):.0%}"
                )
                print(
                    f"Ti le sinh vien kha: {round(float(len(good)/len(students)),2):.0%}"
                )
                print(
                    f"Ti le sinh vien kem: {round(float(len(bad)/len(students)),2):.0%}"
                )
                print(
                    f"Sinh vien diem cao nhat ({top_score}) la: " + ", ".join(top_std)
                )

            except ValueError:
                print("There is an error in the student list.")

        # (8)-SAVE---------------------------------------------------
        elif command == "8":
            print("[8] Save:")
            with open("data.csv", "w+", newline="") as data:
                writer = csv.writer(data)
                writer.writerows(students)

            print("SAVED")

        # (9)-VALIDATE-----------------------------------------------
        elif command == "9":
            print("[9] Validate:")
            if len(errors) != 0:
                print("/!\\ ERRORS:")
                student_display(errors)
            else:
                print("Congrats! There are no errors!")

        # (0)-QUIT---------------------------------------------------
        elif command == "0":
            print("QUITED")
            break

        else:
            continue

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
