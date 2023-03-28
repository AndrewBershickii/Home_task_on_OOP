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


best_student = Student('Андрей', 'Андреевич', 'М')
best_student.courses_in_progress += ['Python', 'С++']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Карина', 'Владиславовна', 'Ж')
best_student2.courses_in_progress += ['Python', 'С++']
best_student2.finished_courses += ['Введение в программирование']

lecturer = Lecturer('Снежана', 'Денисовна')
lecturer.courses_attached += ['Python', 'С++']

lecturer2 = Lecturer('Виктория', 'Викторовна')
lecturer2.courses_attached += ['Python']

cool_reviewer = Reviewer('Геннадий', 'Иванович')
cool_reviewer.courses_attached += ['Python', 'С++']

cool_reviewer.rate_hw(best_student, 'С++', 7)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'С++', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student2, 'С++', 6)
cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'С++', 7)
cool_reviewer.rate_hw(best_student2, 'Python', 9)

best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 6)
best_student.rate_lecturer(lecturer2, 'Python', 7)
best_student.rate_lecturer(lecturer2, 'Python', 8)

print(cool_reviewer)
print(lecturer)
print(lecturer2)
print(best_student)
print(best_student2)
print(lecturer < lecturer2)