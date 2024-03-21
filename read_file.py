import sys
from patients import Patient, Exam

def add_patient(patient_list, name, id):
    #Check to make sure another patient with the same id doesn't already exist
    if id not in patient_list.keys():
        patient_list[id] = Patient(name, id)

def add_exam(patient_list, exam_list, patient_id, exam_id):
    #Need to check a universal list of exams to see if the same id already exists, rather than just the patients exams
    #Also verify that the patient exists
    if exam_id not in exam_list.keys() and patient_id in patient_list.keys():
        exam_list[exam_id] = Exam(exam_id, patient_id)
        patient_list[patient_id].add_exam(exam_id)

def del_patient(patient_list, exam_list, id):
    #Make sure patient exists
    if id in patient_list.keys():
        exams = patient_list[id].exams
        #Clear exams associated with the patient from the list before deleting the patient
        for exam_id in exams:
            del exam_list[exam_id]
        del patient_list[id]

def del_exam(patient_list, exam_list, exam_id):
    #Make sure exam exists
    if exam_id in exam_list.keys():
        patient_id = exam_list[exam_id].patient_id #Get the patient associated with the exam
        patient_list[patient_id].remove_exam(exam_id) #Remove exam from patients list
        del exam_list[exam_id]

def parse_file(file_name):
    f = open(file_name, "r")
    commands = f.read().splitlines() #Doing this instead of readlines to get rid of newlines
    f.close()


    #Keeping patient and exam records in a dictionary keyed by their unique ID
    patient_list = {}
    exam_list = {}

    for command in commands:

        #Would need to split ADD and DEL commands differently
        if command[:3] == "ADD": 
            params = command.split(maxsplit=3) #Setting maxsplit to 3 so the name doesn't get split but everything else does
            if params[1] == "PATIENT":
                add_patient(patient_list, params[3], params[2])
            elif params[1] == "EXAM":
                add_exam(patient_list, exam_list, params[2], params[3])           

        elif command[:3] == "DEL":
            params = command.split() #No spaces in IDs used for deletion so no maxsplit needed
            if params[1] == "PATIENT":
                del_patient(patient_list, exam_list, params[2])
            elif params[1] == "EXAM":
                del_exam(patient_list, exam_list, params[2])      

    #Returning the print output as a string for testing function
    return_str = ""    
    for patient in patient_list.values():
        print(patient)
        return_str += str(patient)

    return return_str

if __name__ == '__main__':
    #I'm assuming this file will be called with the format
    #  python read_file.py [filepath]
    parse_file(file_name=sys.argv[1])