void main()
{
  int i =0;
  String message = "Hello World";

  for (int j =0; j<=(message.length);j++)
  {
    print(j); 
  }
  
  while (i<=10)
  {
    print(message);
    i++;
  }

  i =0;
  do {
    print("Do Do Do");
    i++;
  } while(i<4);
}