#include <stdio.h>
#include <math.h>
/*evaluates and prints whether user-inputted integer is even*/
int main(void)
{
  int i, j;
  printf("\nEnter i\n");
  scanf("%i", &i);
  j=i % 2;
  if (j == 0) {
  printf("the number is even\n");
  }
  if (j != 0) {
  printf("the number is odd\n");
  }
  return 0;
}