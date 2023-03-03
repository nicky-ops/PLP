// anonymous fxn stored in a variable
void main()
{
  var sum = (int num1, int num2){
    return num1 + num2;
  };
  print(sum(30,40));
  cars(); //calls the car function
}

// anonymous function as a parameter
void cars(){
  List vehicles = ['Mazda','BMW','Hyundai','Toyota','Audi'];
  vehicles.forEach((item) {
    print(item);
  });
}