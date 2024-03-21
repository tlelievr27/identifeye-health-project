from read_file import parse_file

def run_tests(input_files, expected_outputs):

    for i in range(0, len(input_files)):
        print("Function Output")
        return_str = parse_file(input_files[i])
        #parse_file will return the string it outputs with print

        #Open the expected output text and assert that it matches
        with open(expected_outputs[i]) as output:
            output = output.read()
            print("Expected Output:\n" + output + "\n")
            assert return_str == output, "Input does not match expected output"

    print("All tests passed")

if __name__ == '__main__':
    #Responsible for running through the tests in the tests folder
    #And asserting their output matches the intended format

    #The test files I wrote look at edge cases for each individual command type
    #plus any interactions between commands (ie deleting a patient then being able to add an exam number they used to have)

    #Set up the parse_file function to return the string it prints to stdout to make testing easier
    test_files = ['./tests/example.txt', './tests/add_exams.txt', './tests/del_exams.txt', './tests/del_patients.txt']
    expected_files = ['./tests/example_expected.txt', './tests/add_exams_expected.txt', './tests/del_exams_expected.txt', './tests/del_patients_expected.txt']
    run_tests(test_files, expected_files)