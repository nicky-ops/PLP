class MyContextManager:
  def __enter__(self):
    print("Enterign context")
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    print("Exiting context")
    if exc_type is not None:
      print(f"An error of type {exc_type} occurred: {exc_val}")
    return True

with MyContextManager() as cm:
  print("Inside context")

with open("requirements.txt", "r+") as f:
  print(f.readlines())