import itertools

class School:
    def __init__(self):
        self.add_history = []
        self.grades = {}

    def add_student(self, name, grade):
        if any([name in self.grades[grade] for grade in self.grades.keys()]):
            self.add_history.append(False)
            return

        if grade not in self.grades:
            self.grades[grade] = []

        self.grades[grade].append(name)
        self.add_history.append(True)

    def roster(self):
        current_grades = sorted(self.grades.keys())
        return list(itertools.chain(*[self.grade(grade) for grade in current_grades]))

    def grade(self, grade_number):
        if grade_number not in self.grades:
            return []
        return list(sorted(self.grades[grade_number]))

    def added(self):
        return self.add_history