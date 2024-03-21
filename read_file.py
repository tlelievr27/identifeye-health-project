import sys
from patients import Patient, Exam

def add_patient(patient_list, name, id):
    pass

def add_exam(patient_list, exam_list, exam_id):
    pass

def del_patient(patient_list, exam_list, id):
    pass

def del_exam(patient_list, exam_list, id):
    pass

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

        elif command[:3] == "DEL":
            params = command.split() #No spaces in IDs used for deletion so no maxsplit needed

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