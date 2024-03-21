def Patient():
    #Class for a patient record

    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.exams = [] #List of exams associated with patient id
    
    def get_num_exams(self): #For convenience
        return len(self.exams)

    def add_exam(self, exam_id):
        pass

    def remove_exam(self, exam_id):
        pass


def Exam():
    #Class for an exam record

    def __init__(self, exam_id, patient_id):
        self.id = exam_id
        self.patient_id = exam_id