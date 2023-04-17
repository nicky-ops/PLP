# Handling Exceptions and errors when reading/writing files
#### Areas Covered
* What are exceptions
* Purpose of handling exceptions
* Try clause
* Except clause
* Else clause
* Finally clause
* Raising exceptions
An exception is raised when a running program encounters an *error* during its execution. 
Exceptions disrupt the normal execution of a program and causes it to end abruptly. To address this you can catch them and handle them appropriately.
### Common Exceptions
1. <IndexError> - raised when you try to index a list, tuple or string beyond its permitted boundaries.
2. *KeyError* - raised when you try to acces the value of a key that doesn't exist in a dictionary.
3. *NameError* - raised when a name you are referencing in the code doesn't exist.
4. *TypeError* - raised when an operation or function is applied to an object of an inappropriate type.
5. *ZeroDivisionError* - raised when you try to divide by zero.

* By handling exceptions, you can provide an alternative flow of execution to avoid crashing your program unexpectedly.
