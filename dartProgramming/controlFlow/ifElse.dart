void main()
{
  const name = 'Fred';
  const age = 42;
  var retirement = 60;
  if (age >= 60)
  {
    print("This is a retired officer");
  } else {
    retirement -= age;
    print("Retirement is due in $retirement years");
  }
}