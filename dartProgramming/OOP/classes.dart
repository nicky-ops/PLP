class Cat {
  String? name;
  String? color;
  static String sound = "Meow";

  static String walk(){
    print("I can walk!");
    return "Exit";
  }
}
void main(){
  var nora = Cat ();
  nora.name = 'Zepphyrr';
  nora.color = 'Grey';
  print(nora);
  print(nora.name);
  print(nora.color);
  print(Cat.walk());
  print(Cat.sound);
}
get fieldName {}
