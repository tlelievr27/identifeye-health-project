class Patient():
    #Class for a patient record

    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.exams = [] #List of exams associated with patient id

    def add_exam(self, exam_id):
        self.exams.append(exam_id)

    def remove_exam(self, exam_id):
        self.exams.remove(exam_id)

    #For printing the output
    def __str__(self):
        return f'Name: {self.name}, Id: {self.id}, Exam Count: {len(self.exams)}'

    #For returning the output string to testing function
    def __repr__(self):
        return f'Name: {self.name}, Id: {self.id}, Exam Count: {len(self.exams)}\n'


class Exam():
    #Class for an exam record

    def __init__(self, exam_id, patient_id):
        self.id = exam_id
        self.patient_id = patient_id