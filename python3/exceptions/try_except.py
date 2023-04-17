students = {
        "Nora":15,
        "Gino":30
        }
n = input("Enter students name: ")
while (n):

    try:
        print(f"{n} is {students[n]} years old")

    except:
        print("Name not found!")
