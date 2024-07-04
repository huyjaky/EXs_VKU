class StudentProfile:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.subjects = {}

    def add_subject(self, subject_name, mark):
        self.subjects[subject_name] = mark

    def average_mark(self):
        if self.subjects:
            return sum(self.subjects.values()) / len(self.subjects)
        return 0

    def __call__(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print("Subjects and Marks:")
        for subject, mark in self.subjects.items():
            print(f"{subject}: {mark}")
        print(f"Average Mark: {self.average_mark()}")


name = input("Name of Student: ")
dob = input("Date of Birth (DD/MM/YYYY): ")
student = StudentProfile(name, dob)

for i in range(3):
    subject_name = input(f"Name of Subject {i+1}: ")
    mark = float(input(f"Mark of {subject_name}: "))
    student.add_subject(subject_name, mark)

student()
