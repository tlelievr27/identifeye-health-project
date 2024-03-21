import sys
from patients import Patient, Exam

def parse_file(file_name):
    f = open(file_name, "r")
    commands = f.readlines()
    f.close()

    for command in commands:
        print(command)

if __name__ == '__main__':
    #I'm assuming this file will be called with the format
    #  python read_file.py [filepath]
    parse_file(file_name=sys.argv[2])