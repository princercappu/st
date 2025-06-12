
def add_numbers(a, b):
    return a + b


def read_test_cases(file_path):
    test_cases = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 3:  
                    input1 = int(parts[0])
                    input2 = int(parts[1])
                    expected_output = int(parts[2])
                    test_cases.append((input1, input2, expected_output))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return test_cases


def execute_tests_and_log(test_cases, result_file_path):
    with open(result_file_path, 'w') as result_file:
        for index, (input1, input2, expected) in enumerate(test_cases):
            actual = add_numbers(input1, input2)
            if actual == expected:
                result = "PASS"
            else:
                result = "FAIL"
         
            result_file.write(f"Test Case {index+1}: Inputs=({input1},{input2}), Expected={expected}, Actual={actual} --> {result}\n")

    print(f"Testing complete. Results saved in '{result_file_path}'.")


if __name__ == "__main__":
    test_case_file = "test_cases.txt"
    result_file = "test_results.txt"

  
    test_cases = read_test_cases(test_case_file)

    if test_cases:
     
        execute_tests_and_log(test_cases, result_file)
    else:
        print("No valid test cases to execute.")
