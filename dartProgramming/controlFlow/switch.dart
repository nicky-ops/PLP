import 'dart:io';

void main()
{
  print("Enter a the grade attained");
  String? grade = stdin.readLineSync();
  switch (grade)
  {
    case "A":
      {
        print("Excellent!");
      }
      break;
    case "B":
      {
        print("Good");
      }
      break;
    case "C":
      {
        print("Average");
      }
      break;
    case "D":
      {
        print("Below average");
      }
      break;
    case "E":
      {
        print("Poor");
      }
      break;
    case "F":
      {
        print("Fail!");
      }
      break;
    default:
      print("Invalid choice. Try again!");
}
}