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


def student_display(students):
    print("\t+--------+----------+--------------------+--------+--------+")
    print("\t| ID     | Std_code | Name               | Age    | Score  |")
    print("\t+--------+----------+--------------------+--------+--------+")

    for index, student in enumerate(students):
        print(
            f"\t| {str(index+1).ljust(7)}| {student[0].ljust(9)}| {student[1].ljust(19)}| {student[2].ljust(7)}| {student[3].ljust(7)}|"
        )

    print("\t+--------+----------+--------------------+--------+--------+")


def helper_search(students, key=None, value=None):
    result = []
    for student in students:
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
    print("Which student?")
    print("\t(!) 1. Search By Name")
    print("\t(!) 2. Search By Age")
    print("\t(!) 3. Search By Score")

    result = []

    while True:
        option = input("\t(?) Choice: ")
        if option == "1":
            str_of_name = input("Input the characters: ")
            result = helper_search(students, key="name", value=str_of_name)
            break

        elif option == "2":
            num_of_age = int(input("Input the age: "))
            result = helper_search(students, key="age", value=num_of_age)
            break

        elif option == "3":
            num_of_score = float(input("Input the score: "))
            result = helper_search(students, key="score", value=num_of_score)
            break

        else:
            print("Invalid input. Please try again.")

    if result == []:
        print("Student is not found.")
    else:
        print("Students found:")
        student_display(result)

    return result


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
            std_code = f"{len(students)+1:06d}"
            name = input("Enter name: ")
            age = input("Enter age: ")
            score = input("Enter score: ")
            students.append([std_code, name, age, score])
            print("ADDED")

        # EDIT
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
            print("Which property need to be updated?")
            print("\t(!) 1. Name")
            print("\t(!) 2. Age")
            print("\t(!) 3. Score")

            while True:
                option = input("\t(?) Choice: ")
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

        # DELETE
        elif command == "4":
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

        # SEARCH
        elif command == "5":
            print("[5] Search:")
            search_student(students)

        # SORT
        elif command == "6":
            print("[6] Sort:")
            print("\t(!) How to sort?")
            print("\t(!) 1. By Name (A-Z)")
            print("\t(!) 2. By Age (Descending)")
            print("\t(!) 3. By Score (Descending)")

            while True:
                option = input("\t(?) Choice: ")
                if option == "1":
                    students.sort(key=lambda x: (x[1].lower(), float(x[3])))
                    break

                elif option == "2":
                    students.sort(key=lambda x: (-int(x[2]), x[1].lower()))
                    break

                elif option == "3":
                    students.sort(key=lambda x: (-float(x[3]), x[1].lower()))
                    break

                else:
                    print("Invalid input. Please try again.")

            student_display(students)

        # STATS
        elif command == "7":
            print("[7] Statistics:")
            sum_of_score = 0
            excel = []
            good = []
            bad = []

            for student in students:
                sum_of_score += float(student[2])
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
            print(f"Sinh vien diem cao nhat ({top_score}) la:", ", ".join(top_std))

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
            print("Invalid input. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
