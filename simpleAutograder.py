import unittest
import subprocess
import re 

def grade_assignment(student_code, test_cases):
  """ grades a students python code against a set of test cases.
  Args: student_code: student's python code as a string 
        test_cases: a list of tuples, each containing an input and expected output
  Returns:
        a tuple containing the score and a detailed feedback message.
        """

  # create temp python file
  with open("student_code.py", "w") as f:
    f.write(student_code)

  # run unit tests 
  test_runner = unittest.TextTestRunner(verbosity=2)
  test_suite = unittest.TestSuite()
  for input, expected_output in test_cases:
    test_case = TestCase(input, expected_output)
    test_suite.addTest(test_case)
  result = test_runner.run(test_suite)

  # check code style 
  process = subprocess.run(["pylint", "student_code.py"], capture_output=True, text=True)
  style_score = 10 - len(re.findall(r"C\d+", process.stdout))

  # calculate final score 
  score = (result.testsRun * 10 + style_score) / (result.testsRun + 1)

  feedback = f"Test cases passed: {result.testsRun} / {len(test_cases)} \n"
  feedback += f"Code style score: {style_score} /10\n"
  feeback == process.stdout

  return score, feedback 

# example usage:

student_code = """
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
    """

test_cases = [(0,1), (5,120), (10, 3628800)]
score, feedback = grade_assignment(student_code, test_cases)
print(feedback) 
