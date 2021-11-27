import os
import csv


def menu_display():
    os.system("clear")
    print("Actions list:")
    print("1 - Print")
    print("2 - Add")
    print("3 - Edit")
    print("4 - Delete")
    print("5 - Search")
    print("6 - Sort")
    print("7 - Stats")
    print("8 - Save")
    print("9 - Quit")


def check_error(students):
    for index, student in enumerate(students):
        if "" in student or None in student:
            print(f"There is missing info in the list at row {index+1}.")
            print(f"{student}")
        return True

    return False


def student_display(students):
    if students == []:
        print("The list is empty.")
        return

    print("\t+--------+--------+--------------------+--------+--------+")
    print("\t| No.    | ID     | Name               | Age    | Score  |")
    print("\t+--------+--------+--------------------+--------+--------+")

    for index, student in enumerate(students):
        print(
            f"\t| {str(index+1).ljust(7)}| {student[0].ljust(7)}| {student[1].ljust(19)}| {student[2].ljust(7)}| {student[3].ljust(7)}|"
        )

    print("\t+--------+--------+--------------------+--------+--------+")


def helper_search(students, key=None, value=None):
    result = []
    for student in students:
        if key == "id":
            if value == student[0]:
                result.append(student)
        if key == "name":
            if value.lower() in student[1].lower():
                result.append(student)
        if key == "age":
            if value == int(student[2]):
                result.append(student)
        if key == "score":
            if value == float(student[3]):
                result.append(student)

    return result


def search_student(students):
    if students == []:
        print("The list is empty.")
        return

    result = []
    while True:
        print("Which student?")
        print("\t(!) 1. Search By ID")
        print("\t(!) 2. Search By Name")
        print("\t(!) 3. Search By Age")
        print("\t(!) 4. Search By Score")
        option = input("\t(?) Option: ")
        if option == "1":
            id = input("Input the student ID: ")
            result = helper_search(students, key="id", value=id)
            break

        if option == "2":
            str_of_name = input("Input the characters: ")
            result = helper_search(students, key="name", value=str_of_name)
            break

        elif option == "3":
            num_of_age = int(input("Input the age: "))
            result = helper_search(students, key="age", value=num_of_age)
            break

        elif option == "4":
            num_of_score = float(input("Input the score: "))
            result = helper_search(students, key="score", value=num_of_score)
            break

        else:
            print("Invalid input. Please try again.")

    print("Student(s) found:")
    student_display(result)

    return result


def main():
    students = []
    if not os.path.exists("data.csv"):
        open("data.csv", "w").close()
    elif os.path.getsize("data.csv") == 0:
        print("The file is empty.")
        file_empty = True
    else:
        with open("data.csv", "r") as data:
            lines = data.read().strip().split("\n")
            for line in lines:
                students.append(line.split(","))

    while True:
        menu_display()
        command = input("Enter command: ")

        # match - case
        # (1)-PRINT--------------------------------------------------
        if command == "1":
            print("[1] Print:")
            student_display(students)

        # (2)-ADD----------------------------------------------------
        elif command == "2":
            print("[2] Add:")
            if file_empty:
                id = "000001"
            else:
                id = f"{int(students[-1][0])+1:06d}"
            name = input("Enter name: ")
            age = input("Enter age: ")
            score = input("Enter score: ")
            students.append([id, name, age, score])
            print("ADDED")

        # (3)-EDIT---------------------------------------------------
        elif command == "3":
            print("[3] Edit:")
            result = []
            while len(result) != 1:
                if len(result) == 0:
                    result = search_student(students)
                if len(result) > 1:
                    print("There are many students in the list.")
                    result = search_student(result)

            index = students.index(result[0])

            while True:
                print("Which property need to be updated?")
                print("\t(!) 1. Name")
                print("\t(!) 2. Age")
                print("\t(!) 3. Score")
                option = input("\t(?) Option: ")
                if option == "1":
                    name = input("Please enter name you want to change: ")
                    students[index][1] = name
                    break

                elif option == "2":
                    age = input("Please enter age you want to change: ")
                    students[index][2] = age
                    break

                elif option == "3":
                    score = input("Please enter score you want to change: ")
                    students[index][3] = score
                    break

                else:
                    print("Invalid input. Please try again.")

            print("EDITED")

        # (4)-DELETE-------------------------------------------------
        elif command == "4":
            if check_error(students):
                break

            print("[4] Delete:")
            result = []
            while len(result) != 1:
                if len(result) == 0:
                    result = search_student(students)
                if len(result) > 1:
                    print("There are many students in the list.")
                    result = search_student(result)

            while True:
                confirm = input("Are you sure to delete this student (y/n)? ")
                if confirm == "y":
                    index = students.index(result[0])
                    students.pop(int(index))
                    print("DELETED")
                    break
                elif confirm == "n":
                    break
                else:
                    "Invalid input. Please try again."

        # (5)-SEARCH-------------------------------------------------
        elif command == "5":
            print("[5] Search:")
            search_student(students)

        # (6)-SORT---------------------------------------------------
        elif command == "6":
            if check_error(students):
                break

            print("[6] Sort:")
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
                            students.sort(key=lambda x: x[0])
                            break
                        elif select == "2":
                            students.sort(key=lambda x: x[0], reverse=True)
                            break
                        else:
                            print("Invalid input. Please try again.")
                    break

                elif option == "2":
                    while True:
                        print("\t(!) 1. Ascending")
                        print("\t(!) 2. Descending")
                        select = input("\t(?) Select: ")
                        if select == "1":
                            students.sort(
                                key=lambda x: (x[1].lower(), int(x[2]), float(x[3]))
                            )
                            break
                        elif select == "2":
                            students.sort(
                                key=lambda x: (x[1].lower(), int(x[2]), float(x[3])),
                                reverse=True,
                            )
                            break
                        else:
                            print("Invalid input. Please try again.")
                    break

                elif option == "3":
                    while True:
                        print("\t(!) 1. Ascending")
                        print("\t(!) 2. Descending")
                        select = input("\t(?) Select: ")
                        if select == "1":
                            students.sort(
                                key=lambda x: (int(x[2]), x[1].lower(), float(x[3]))
                            )
                            break
                        elif select == "2":
                            students.sort(
                                key=lambda x: (int(x[2]), x[1].lower(), float(x[3])),
                                reverse=True,
                            )
                            break
                        else:
                            print("Invalid input. Please try again.")
                    break

                elif option == "4":
                    while True:
                        print("\t(!) 1. Ascending")
                        print("\t(!) 2. Descending")
                        select = input("\t(?) Select: ")
                        if select == "1":
                            students.sort(
                                key=lambda x: (float(x[3]), x[1].lower(), int(x[2]))
                            )
                            break
                        elif select == "2":
                            students.sort(
                                key=lambda x: (float(x[3]), x[1].lower(), int(x[2])),
                                reverse=True,
                            )
                            break
                        else:
                            print("Invalid input. Please try again.")
                    break

                else:
                    print("Invalid input. Please try again.")

            student_display(students)

        # (7)-STATS--------------------------------------------------
        elif command == "7":
            if check_error(students):
                break

            print("[7] Statistics:")
            sum_of_score = 0
            excel = []
            good = []
            bad = []

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
            print(f"Ti le sinh vien kha: {round(float(len(good)/len(students)),2):.0%}")
            print(f"Ti le sinh vien kem: {round(float(len(bad)/len(students)),2):.0%}")
            print(f"Sinh vien diem cao nhat ({top_score}) la: " + ", ".join(top_std))

        # (8)-SAVE---------------------------------------------------
        elif command == "8":
            print("[8] Save:")
            with open("data.csv", "w+", newline="") as data:
                writer = csv.writer(data)
                writer.writerows(students)

            print("SAVED")

        # (9)-QUIT---------------------------------------------------
        elif command == "9":
            print("QUITED")
            break

        else:
            print("Invalid input. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
