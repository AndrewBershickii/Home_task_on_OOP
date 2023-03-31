class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grade(self):
        grade_all = [grade for value in self.grades.values() for grade in value]
        if len(grade_all) > 0:
            grade_sum = sum(grade_all) / len(grade_all)
        else:
            grade_sum = f"Ошибка оценки"
        return grade_sum

    def __str__(self):
        res = f'Имя: {self.name} \
               \nФамилия: {self.surname} \
               \nСредняя оценка за домашние задания: {self._avg_grade()} \
               \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \
               \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student) and isinstance(self._avg_grade(), float) and isinstance(other._avg_grade(), float):
            return self._avg_grade() < other._avg_grade()
        else:
            return f'Ошибка сравнения'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        grade_all = [grade for value in self.grades.values() for grade in value]
        if len(grade_all) > 0:
            avg_grade = sum(grade_all) / len(grade_all)
        else:
            avg_grade = f"Сперва оцените преподователя"
        return avg_grade

    def __str__(self):
        res = f'Имя: {self.name} \
              \nФамилия: {self.surname} \
              \nСредняя оценка за лекции: {self._avg_grade()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer) and isinstance(self._avg_grade(), float) and isinstance(other._avg_grade(), float):
            return self._avg_grade() < other._avg_grade()
        else:
            return f'Ошибка сравнения'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \
               \nФамилия: {self.surname}'
        return res

def student_gr(lst, course):
    all_g = []
    for student in lst:
        for grade in student.grades[course]:
            all_g.append(grade)
    if len(all_g) > 0:
        return sum(all_g) / len(all_g)
    else:
        return f'Сперва добавьте оценки'


def lector_gr(lst, course):
    all_g = []
    for lecturer in lst:
        for grade in lecturer.grades[course]:
            all_g.append(grade)
    if len(all_g) > 0:
        return sum(all_g) / len(all_g)
    else:
        return f'Сперва добавьте оценки'


student1 = Student('Андрей', 'Андреевич', 'М')
student1.courses_in_progress += ['Python', 'С++']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Карина', 'Владиславовна', 'Ж')
student2.courses_in_progress += ['Python', 'С++']
student2.finished_courses += ['Введение в программирование']

lecturer = Lecturer('Снежана', 'Денисовна')
lecturer.courses_attached += ['Python', 'С++']

lecturer2 = Lecturer('Виктория', 'Викторовна')
lecturer2.courses_attached += ['Python']

reviewer = Reviewer('Геннадий', 'Иванович')
reviewer.courses_attached += ['Python', 'С++']

reviewer.rate_hw(student1, 'С++', 7)
reviewer.rate_hw(student1, 'Python', 9)
reviewer.rate_hw(student1, 'С++', 8)
reviewer.rate_hw(student1, 'Python', 10)

reviewer.rate_hw(student2, 'С++', 6)
reviewer.rate_hw(student2, 'Python', 10)
reviewer.rate_hw(student2, 'С++', 7)
reviewer.rate_hw(student2, 'Python', 9)

student1.rate_lecturer(lecturer, 'Python', 10)
student1.rate_lecturer(lecturer, 'Python', 6)
student1.rate_lecturer(lecturer2, 'Python', 7)
student1.rate_lecturer(lecturer2, 'Python', 8)

print(student1)
print(student2)
print(lecturer)
print(lecturer2)
print(reviewer)
print(lecturer > lecturer2)
print(student1 < student2)
print(student_gr([student1, student2], 'С++'))
print(lector_gr([lecturer, lecturer2], 'Python'))