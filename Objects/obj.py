class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and (grade > 10 or grade < 1):
            return 'Ошибка'
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grades(self):
        if not self.grades:
            return 0
        list_grades = []
        for value in self.grades.values():
            list_grades.extend(value)
        return round(sum(list_grades) / len(list_grades), 2)

    def __eq__(self, obj):
        if not isinstance(obj, Student):
            raise Exception('Error')
        return self.middle_grades() == obj.middle_grades()

    def __lt__(self, obj):
        if not isinstance(obj, Student):
            raise Exception('Error')
        return self.middle_grades() < obj.middle_grades()

    def __le__(self, obj):
        if not isinstance(obj, Student):
            raise Exception('Error')
        return self.middle_grades() <= obj.middle_grades()

    def __str__(self):
        return f"""Имя: {self.name}
        \rФамилия: {self.surname}
        \rСредняя оценка за домашние задания: {self.middle_grades()}
        \rКурсы в процессе обучения: {', '.join(self.courses_in_progress)}
        \rЗавершенные курсы: {', '.join(self.finished_courses)}
        """


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def middle_grades(self):
        if not self.grades:
            return 0
        list_grades = []
        for value in self.grades.values():
            list_grades.extend(value)
        return round(sum(list_grades) / len(list_grades), 2)

    def __eq__(self, obj):
        if not isinstance(obj, Lecturer):
            raise Exception('Error')
            return 'error'
        return self.middle_grades() == obj.middle_grades()

    def __lt__(self, obj):
        if not isinstance(obj, Lecturer):
            raise Exception('Error')
        return self.middle_grades() < obj.middle_grades()

    def __le__(self, obj):
        if not isinstance(obj, Lecturer):
            raise Exception('Error')
            return 'error'
        return self.middle_grades() <= obj.middle_grades()

    def __str__(self):
        return f"""Имя: {self.name}
        \rФамилия: {self.surname}
        \rСредняя оценка за лекции: {self.middle_grades()} 
        """


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (grade > 10 or grade < 1):
            return 'Ошибка'
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
        \rФамилия: {self.surname}
        """


def rating_all_students(list_students, course):
    if not isinstance(list_students, list):
        return "Not list"
    list_one = []
    for person in list_students:
        list_one.extend(person.grades.get(course, []))
    if not list_one:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(list_one) / len(list_one), 2)


def rating_of_lections(list_lectors, course):
    return rating_all_students(list_lectors, course)


list_lector = []

list_stud = []

some_student = Student('Ruoy', 'Eman', 'Male')
two_student = Student('Rikki', 'Obichniy', 'Male')

list_stud.append(some_student)
list_stud.append(two_student)

some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
some_student.courses_in_progress += ['C++']
some_student.courses_in_progress += ['Java Script']
some_student.finished_courses += ['Pascal']
some_student.finished_courses += ['C++']
two_student.courses_in_progress += ['Python']
two_student.courses_in_progress += ['Java']
two_student.finished_courses += ['Java Script']

one_reviewer = Reviewer('Vanya', 'Tuchniy')
one_reviewer.courses_attached += ['Python']
one_reviewer.courses_attached += ['C++']
one_reviewer.courses_attached += ['Java']
one_reviewer.courses_attached += ['Java Script']

two_reviewer = Reviewer('Kolya', 'Horoshiy')
two_reviewer.courses_attached += ['Java']
two_reviewer.courses_attached += ['C++']
three_reviewer = Reviewer('Jenya', 'Normal')
three_reviewer.courses_attached += ['C++']
three_reviewer.courses_attached += ['Python']

one_lector = Lecturer('Den', 'Zangiev')
one_lector.courses_attached += ['Python']
one_lector.courses_attached += ['Java']
one_lector.courses_attached += ['Java Script']
one_lector.courses_attached += ['Her']

list_lector.append(one_lector)

two_lector = Lecturer('Alex', 'Solnce')
two_lector.courses_attached += ['Java']
two_lector.courses_attached += ['C++']
two_lector.courses_attached += ['Python']

list_lector.append(two_lector)

three_lector = Lecturer('Vasya', 'Krutov')
three_lector.courses_attached += ['C++']
three_lector.courses_attached += ['Java']

list_lector.append(three_lector)

one_reviewer.rate_hw(some_student, 'Python', 10)

one_reviewer.rate_hw(some_student, 'Python', 30)
one_reviewer.rate_hw(some_student, 'Java', 3430)

one_reviewer.rate_hw(some_student, 'Python', 3)
one_reviewer.rate_hw(two_student, 'Python', 1)
three_reviewer.rate_hw(some_student, 'Python', 7)
three_reviewer.rate_hw(some_student, 'Python', 2)
one_reviewer.rate_hw(two_student, 'Python', 5)
one_reviewer.rate_hw(two_student, 'Python', 3)

two_reviewer.rate_hw(some_student, 'Java', 10)
two_reviewer.rate_hw(some_student, 'Java', 6)
two_reviewer.rate_hw(some_student, 'Java', 9)

two_reviewer.rate_hw(two_student, 'Java', 6)
two_reviewer.rate_hw(two_student, 'Java', 1)
two_reviewer.rate_hw(two_student, 'Java', 9)

three_reviewer.rate_hw(some_student, 'C++', 10)

three_reviewer.rate_hw(two_student, 'C++', 9)

one_reviewer.rate_hw(some_student, 'C++', 10)
one_reviewer.rate_hw(some_student, 'C++', 9)
one_reviewer.rate_hw(some_student, 'C++', 3)
one_reviewer.rate_hw(some_student, 'C++', 2)
one_reviewer.rate_hw(some_student, 'C++', 2)
one_reviewer.rate_hw(some_student, 'C++', 4)
one_reviewer.rate_hw(some_student, 'Java', 9)

one_reviewer.rate_hw(some_student, 'Java Script', 5)

two_reviewer.rate_hw(two_student, 'Java', 10)
two_reviewer.rate_hw(two_student, 'Java', 7)
two_reviewer.rate_hw(two_student, 'Python', 1)
two_reviewer.rate_hw(two_student, 'Python', 2)
two_reviewer.rate_hw(two_student, 'C++', 4)

some_student.rate_hw(one_lector, 'Python', 5)
some_student.rate_hw(one_lector, 'Python', 59)
some_student.rate_hw(one_lector, 'Java Script', 7)
some_student.rate_hw(two_lector, 'Python', 10)
some_student.rate_hw(one_lector, 'Java', 3)
some_student.rate_hw(two_lector, 'Java', 4)
some_student.rate_hw(three_lector, 'Java', 10)
some_student.rate_hw(three_lector, 'Java', 9)
some_student.rate_hw(three_lector, 'C++', 9)

two_student.rate_hw(one_lector, 'Python', 10)
two_student.rate_hw(two_lector, 'Java', 2)
two_student.rate_hw(three_lector, 'Java', 7)

print('Студент 1', some_student, sep='\n')
print()
print('Студент 2', two_student, sep='\n')
print()
print('Ревьювер 1', one_reviewer, sep='\n')
print()
print('Ревьювер 2', two_reviewer, sep='\n')
print()
print('Ревьювер 3', three_reviewer, sep='\n')
print()
print('Лектор 1', one_lector, sep='\n')
print()
print('Лектор 2', two_lector, sep='\n')
print()
print('Лектор 3', three_lector, sep='\n')
print()

if some_student == two_student:
    print('Студенты с одинаковой успеваемостью')
elif some_student < two_student:
    print(f' {some_student.name} студент не успевает')
else:
    print(f'{two_student.name} студент не успевает')

if one_lector == two_lector:
    print('Студенты одинаково оценивают лекторов')
elif one_lector < two_lector:
    print(f'Студенты оценивают лектора {one_lector.name} хуже')
else:
    print(f'Студенты оценивают лектора {one_lector.name} лучше')

print()

course_stud = input('Введите курс, по которому будет расчёт средней оценки у всех студентов ')
print(
    f'Средняя оценка по всем студентам в рамке одного курса {course_stud} : {rating_all_students(list_stud, course_stud)}')

print()

course_lect = input('Введите название курса для средней оценки лекторов ')
print(f'Средняя оценка за лекции от студентов по курсу {course_lect} : {rating_of_lections(list_lector, course_lect)}')

