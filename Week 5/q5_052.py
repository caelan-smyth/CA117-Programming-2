import sys


def sorter(t):
    return t[1]


def main():
    skipped = []
    student_marks = {}
    for line in sys.stdin:
        name = line.strip().split(':')[0]
        marks = line.strip().split(':')[1].split(',')

        total_marks = 0
        try:
            for mark in marks:
                total_marks += int(mark)
        except ValueError:
            skipped.append(name)
        else:
            student_marks[name] = total_marks

    for student in sorted(student_marks.items(), key=sorter, reverse=True):
        print('{} : {}'.format(student[0], student[1]))

    print('Skipped:')
    for student in skipped:
        print(student)


if __name__ == '__main__':
    main()