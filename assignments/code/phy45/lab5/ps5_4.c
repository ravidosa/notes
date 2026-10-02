#include <stdio.h>
#include <math.h>
#include <float.h>
double f();
double fp();
void bisection();
int main(void)
{
  int j,N;
  printf("Enter guessed number of roots and guesses for interval bounds: \n");
  scanf("%i",&N);
  double guesses[2][N];
  double root_minmax[2];
  for (j=0;j<N;j=j+1)
  {
    scanf("%lf %lfs",&guesses[0][j],&guesses[1][j]);
  }
  for (j=0;j<N;j=j+1)
  {
    bisection(guesses[0][j], guesses[1][j], root_minmax); 
    while (fabs(root_minmax[1] - root_minmax[0]) > 100 * DBL_EPSILON)
    {
        bisection(root_minmax[0], root_minmax[1], root_minmax);
    }
    printf("root from (%lf, %lf) => %lf \n",guesses[0][j],guesses[1][j],root_minmax[0]);
  } 
  return 0;
}
double f(double x)
{
  double fofx;
  fofx=x * tan(x) - sqrt(pow(10, 2) - pow(x, 2));
  return fofx;
}
void bisection(double a, double b, double ab_new []) {
    double c = (a + b) / 2;
    if (f(a) * f(c) <= 0) {
        ab_new[0] = a;
        ab_new[1] = c;
        //if a and c on opp sides of 0, switch c to new b
    }
    else {
        ab_new[0] = c;
        ab_new[1] = b;
        //else, switch c to new a
    }
}