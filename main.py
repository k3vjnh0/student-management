import os
import csv


def clear():
    os.system("clear")


def menu_display():
    clear()
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


def student_display(students):
    print("\t+--------+--------------------+--------+--------+")
    print("\t| ID     | Name               | Age    | Mark   |")
    print("\t+--------+--------------------+--------+--------+")

    for index, student in enumerate(students):
        print(
            f"\t| {str(index+1).ljust(7)}| {student[0].ljust(19)}| {student[1].ljust(7)}| {student[2].ljust(7)}|"
        )

    print("\t+--------+--------------------+--------+--------+")


def main():
    students = []
    with open("data.csv", "r") as data:
        lines = data.read().strip().split("\n")
        for line in lines:
            students.append(line.split(","))

    while True:
        menu_display()
        command = input("Enter command: ")

        # match - case
        # PRINT
        if command == "1":
            print("[1] Print:")
            student_display(students)

        # ADD
        elif command == "2":
            print("[2] Add:")
            name = input("Enter name: ")
            age = input("Enter age: ")
            mark = input("Enter mark: ")
            students.append([name, age, mark])
            print("ADDED")

        # EDIT
        elif command == "3":
            print("[3] Edit:")
            index = input("Enter index: ")
            if int(index) > len(students):
                print('Student is not found.')
            else:
                print(f"Result: {students[int(index) - 1]}")

                print("Which property need to be updated? ")
                print("\t(!) 1. Name")
                print("\t(!) 2. Age")
                print("\t(!) 3. Mark")

                while True:
                    option = input("\t(?) Choice: ")
                    if option == "1":
                        name = input("Please enter name you want to change: ")
                        students[int(index) - 1][0] = name
                        break

                    elif option == "2":
                        age = input("Please enter age you want to change: ")
                        students[int(index) - 1][1] = age
                        break

                    elif option == "3":
                        mark = input("Please enter mark you want to change: ")
                        students[int(index) - 1][2] = mark
                        break

                    else:
                        print('Invalid input. Please try again.')

                print("EDITED")

        # DELETE
        elif command == "4":
            print("[4] Delete:")
            index = input("Enter index: ")
            if int(index) > len(students):
                print('Student is not found.')
            else:
                students.pop(int(index) - 1)
                print("DELETED")

        # SEARCH
        elif command == "5":
            print("[5] Search:")
            char = input("Input the characters: ")
            result = []
            for student in students:
                if char.lower() in student[0].lower():
                    result.append(student)

            student_display(result)

        # SORT
        elif command == "6":
            print("[6] Sort:")
            print("\t(!) How to sort?")
            print("\t(!) 1. By Name")
            print("\t(!) 2. By Age")
            print("\t(!) 3. By Mark")

            while True:
                option = input("\t(?) Choice: ")
                if option == "1":
                    students = sorted(students, key=lambda x: x[0].lower())
                    break

                elif option == "2":
                    students = sorted(students, key=lambda x: int(x[1]))
                    break

                elif option == "3":
                    students = sorted(students, key=lambda x: float(x[2]))
                    break

                else:
                    print('Invalid input. Please try again.')

            student_display(students)

        # STATS
        elif command == "7":
            print("[7] Statistics:")
            sum_of_mark = 0
            for student in students:
                sum_of_mark += float(student[2])

            print(f"Diem trung binh ca lop: {round(sum_of_mark/len(students),2)}")

            excel = []
            good = []
            bad = []

            for student in students:
                if float(student[2]) >= 8:
                    excel.append(student)
                elif float(student[2]) >= 7 and float(student[2]) < 8:
                    good.append(student)
                else:
                    bad.append(student)

            print(
                f"Ti le sinh vien gioi: {round(float(len(excel)/len(students)),2):.0%}"
            )
            print(f"Ti le sinh vien kha: {round(float(len(good)/len(students)),2):.0%}")
            print(f"Ti le sinh vien kem: {round(float(len(bad)/len(students)),2):.0%}")

            top_mark = max([float(x[2]) for x in excel])
            top_std = [x[0] for x in excel if float(x[2]) == top_mark]
            print(f"Sinh vien diem cao nhat ({top_mark}) la:", ", ".join(top_std))

        # SAVE
        elif command == "8":
            print("[8] Save:")
            with open("data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(students)

            print("SAVED")

        # QUIT
        elif command == "9":
            print("QUITED")
            break

        else:
            print('Invalid input. Please try again.')

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
