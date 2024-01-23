#include <stdio.h>
#include <math.h>
/*approximates cos(x) using taylor series with N terms for user-inputted integer N and float x. accuracy decreases as x increases for constant N*/
int main(void)
{
  int j, N;
  long int fact;
  double x, sum;
  printf("Enter N \n");
  printf("\n");
  scanf("%i", &N);
  printf("Enter x\n");
  scanf("%lf", &x);
  sum = 1.0;
  fact = 1;
  for (j = 1; j < N; j = j + 1)
  {
    fact = fact * j;
    if (j % 4 == 1 || j % 4 == 3) {
      sum = sum;
    }
    if (j % 4 == 0) {
      sum = sum + pow(x, j) / fact;
    }
    if (j % 4 == 2) {
      sum = sum - pow(x, j) / fact;
    }
    printf("\n %i %lf", j, sum);
  }
  printf("\n");
  return 0;
}