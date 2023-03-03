/*
  function getFirstElement takes a list as an argument    and returns the first element of that list
*/

int getFirstElement(List nums)
{
  return nums.elementAt(0);
}
void main()
{
  print(getFirstElement([1,2,3,4,5,6])); 
}