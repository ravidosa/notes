#include <stdio.h>
#include <math.h>
/*prints first 20 multiples of 7*/
int main(void)
{
  int j;
  for(j = 1; j <= 20; j = j + 1)
  {
  printf("\n%i", 7 * j);
  }
  printf("\n");
  return 0;
}