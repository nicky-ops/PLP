void main()
{
  const price = 40;
  var budget = 3000;
  var items = 75;
  var days = 65;

  if (items*price > budget)
  {
    print("I cannot afford that item ");
  } else if(items*price == budget)
  {
    print("I will spend all my money on $items items");
  }else
  {
    print("I can afford them comfortably!");
  }
}