#include <stdio.h>
#include <math.h>
#include <float.h>
double f();
double fp();
double newton();
int main(void)
{
  int j,N;
  double root;
  printf("Enter guessed number of roots and guesses: \n");
  scanf("%i",&N);
  double guesses[N];
  for (j=0;j<N;j=j+1)
  {
    scanf("%lf",&guesses[j]);
  }
  for (j=0;j<N;j=j+1)
  {
    root = newton(guesses[j]);
    while (fabs(f(root)) > 100 * DBL_EPSILON)
    {
        root = newton(root); 
    }
    printf("root from x_0 = %lf => %lf \n",guesses[j],root);
  }
  return 0;
}
double f(double x)
{
  double fofx;
  fofx=x * tan(x) - sqrt(pow(10, 2) - pow(x, 2));
  return fofx;
}
double fp(double x)
{
  double fofx;
  fofx=tan(x) + x * (1/pow(cos(x),2)) + x/sqrt(pow(10, 2) - pow(x, 2));
  return fofx;
}
double newton(double x) {
    x = x - f(x) / fp(x);
    return x;
}