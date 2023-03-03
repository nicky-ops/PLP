// Void function
import 'dart:_http';

void main()
{
  var hello = 'Hello World';
  print(hello);
}

// function with return type
int age ()
{
  return 30;
}

// function with mandatory parameters
String greeting( String morning, String afternoon, String evening)
{
    return afternoon;
}

// function with optional parameters
int number([int countryCode = 254])
{
  return countryCode;
}