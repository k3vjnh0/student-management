import os
import csv


def clear():
    os.system('clear')


def menu_display():
    clear()
    print('Actions list:')
    print('1 - Print')
    print('2 - Add')
    print('3 - Edit')
    print('4 - Delete')
    print('5 - Search')
    print('6 - Sort')
    print('7 - Stats')
    print('8 - Save')
    print('9 - Quit')


def student_display(students):
    print('\t+--------+--------------------+--------+--------+')
    print('\t| ID     | Name               | Age    | Mark   |')
    print('\t+--------+--------------------+--------+--------+')

    for index, student in enumerate(students):
        print(
            f'\t| {str(index+1).ljust(7)}| {student[0].ljust(19)}| {student[1].ljust(7)}| {student[2].ljust(7)}|'
        )

    print('\t+--------+--------------------+--------+--------+')


def main():
    students = []
    with open('data.csv', 'r') as data:
        lines = data.read().split('\n')
        for line in lines:
            students.append(line.split(','))

    while True:
        menu_display()
        command = input('Enter command: ')

        # match - case
        # PRINT
        if command == '1':
            print('[1] Print:')
            student_display(students)

        # ADD
        if command == '2':
            print('[2] Add:')
            name = input('Enter name: ')
            age = input('Enter age: ')
            mark = input('Enter mark: ')
            students.append([name, age, mark])
            print('ADDED')

        # EDIT
        if command == '3':
            print('[3] Edit:')
            index = input('Enter index: ')
            print(f'Result: {students[int(index) - 1]}')

            print('Which property need to be updated? ')
            print('\t(!) 1. Name')
            print('\t(!) 2. Age')
            print('\t(!) 3. Mark')

            option = input('\t(?) Choice: ')
            if option == '1':
                name = input('Please enter name you want to change: ')
                students[int(index) - 1][0] = name

            if option == '2':
                age = input('Please enter age you want to change: ')
                students[int(index) - 1][1] = age

            if option == '3':
                mark = input('Please enter mark you want to change: ')
                students[int(index) - 1][2] = mark

            print('EDITED')

        # DELETE
        if command == '4':
            print('[4] Delete:')
            index = input('Enter index: ')
            students.pop(int(index) - 1)
            print('DELETED')

        # SEARCH
        if command == '5':
            print('[5] Search:')
            char = input('Input the characters: ')
            result = []
            for student in students:
                if char.lower() in student[0].lower():
                    result.append(student)

            student_display(result)

        # SORT
        if command == '6':
            print('[6] Sort:')
            print('\t(!) How to sort?')
            print('\t(!) 1. By Name')
            print('\t(!) 2. By Age')
            print('\t(!) 3. By Mark')

            option = input('\t(?) Choice: ')
            if option == '1':
                students = sorted(students, key=lambda x: x[0])

            if option == '2':
                students = sorted(students, key=lambda x: int(x[1]))

            if option == '3':
                students = sorted(students, key=lambda x: float(x[2]))

            student_display(students)

        # STATS
        if command == '7':
            print('[7] Statistics:')
            sum_of_mark = 0
            for student in students:
                sum_of_mark += float(student[2])

            print(f'Diem trung binh ca lop: {round(sum_of_mark/len(students),2)}')

            excel = []
            good = []
            bad = []

            for student in students:
                if float(student[2]) >= 8.0:
                    excel.append(student)
                elif float(student[2]) >= 7 and float(student[2]) < 8:
                    good.append(student)
                elif float(student[2]) >= 6 and float(student[2]) < 7:
                    bad.append(student)

            print(
                f'Ti le sinh vien gioi: {round(float(len(excel)/len(students)),2):.0%}'
            )
            print(f'Ti le sinh vien kha: {round(float(len(good)/len(students)),2):.0%}')
            print(f'Ti le sinh vien kem: {round(float(len(bad)/len(students)),2):.0%}')

            top_mark = max([float(x[2]) for x in excel])
            top_std = [x[0] for x in excel if float(x[2]) == top_mark]
            print(f'Sinh vien diem cao nhat ({top_mark}) la:', ', '.join(top_std))

        # SAVE
        if command == '8':
            print('[8] Save:')
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(students)

            print('SAVED')

        # QUIT
        if command == '9':
            print('QUITED')
            break

        input('Press Enter to continue...')


if __name__ == '__main__':
    main()
