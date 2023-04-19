# Debugging in Python
* *Debugging* in Software Engineering is the process of identifying and removing errors in computer software.

## Techniques of Debugging
### 1. Print statements
One of the simplest and most common debugging techniques is to insert print statements in your code. You can use print statements to check the values of variables, to trace the flow of the program, or to check the output of a function.

### 2. Debugging With Pdb
* *Pdb* - Python's interactive source code debugger.

## Test-Driven Development (TDD)
* *Test-driven develpment* is a software development practice where develpers write test before writing the actual code. The test specify the desired behaviour of the code and serveas a specification for what the code should do.
<img src = "https://www.xenonstack.com/hubfs/test-driven-development-process-cycle-xenonstack.png" />

### Steps of TDD in Python
1. <b>Write a test:</b> defines the desired behavior of your code. It should check that the code produces the correct output given a specific input.
2. <b>Run the test:</b> run the test to see if it will fail.( which it should).
3. <b>Write the code:</b> write the code to make the test pass. At this point the goal is to make the test pass, not to write the most efficient code.
4. <b>RUn the tests:</b> run the tests to see if the code produces the expected output. If the tests pass, move to the next test, if not, debug the code and fix the errors.
5. <b>Refactor the code:</b> to make the code more efficient, you can refactor the code but ensuring that your changes don't break the code.
6. <b>Repeat:</b> Repeat all the steps above for each feature/component of your application.

Writing tests in Python is done using a testing framework such as unittest, pytest, or nose. These frameworks provide the tools and structure to write and run tests and they also provide features such as test discovery, test fixtures and test reporting.

