void main()
{
  // Numbers - type int and double
  int age = 66;
  print("My age is $age");
  double price = 34.44;
  print("The price is $price");
  
  // String - represents sequence of characters
  String name = "Hello World";
  print(name);
  
  // Boolean 
  bool is_animal = true;
  print("Is this an animal? $is_animal");
  
  // Lists
  List animals = ['Cow','Dog','Cat','Chicken','Duck','Ship','Pig'];
  print('We have a $animals at home.');
  
  // Maps
  var person = {
    name: "Jack",
    'age': 55,
    'sex' : 'Male',
  };
  print('My name is $person');
  
  // Runes
  var heart_symbol = '\u2665';  
  var laugh_symbol = '\u{1f600}';  
  print(heart_symbol);  
  print(laugh_symbol);
  
}