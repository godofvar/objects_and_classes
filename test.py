class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        all_ratings = sum(self.grades.values(), start=[])
        if all_ratings == []:
            return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}' + '\n'\
                + f'Без оценок за дз'  + '\n'\
                    + f'Курсы в процессе изучения: {list(self.grades.keys())}' + '\n'\
                        +f'Завершенные курсы: {self.finished_courses}'
        else:
            return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}' + '\n'\
                + f'Средняя оценка за дз: {round(sum(all_ratings) / len(all_ratings), 2)}'  + '\n'\
                    + f'Курсы в процессе изучения: {list(self.grades.keys())}' + '\n'\
                        +f'Завершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
           print('Not a Student!')
           return
        all_ratings_self, all_ratings_other = sum(self.grades.values(), start=[]), sum(other.grades.values(), start=[])
        return round(sum(all_ratings_self) / len(all_ratings_self), 2) < round(sum(all_ratings_other) / len(all_ratings_other), 2)

    def added_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        all_ratings = sum(self.grades.values(), start=[])
        return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}' + '\n'\
            + f'Средняя оценка за лекции: {round(sum(all_ratings) / len(all_ratings), 2)}'   

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
           print('Not a Lecturer!')
           return
        all_ratings_self, all_ratings_other = sum(self.grades.values(), start=[]), sum(other.grades.values(), start=[])
        return round(sum(all_ratings_self) / len(all_ratings_self), 2) < round(sum(all_ratings_other) / len(all_ratings_other), 2)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)