#include <stdio.h>
#include <math.h>
/*approximates integral of f(x) from x=a to x=b using the trapezoidal rule with user-inputted integer N segments*/
double myfunction();
int main(void)
{
  int j,N;
  double a,b,x,dx,f,integral=0;
  printf("Enter a,b and N \n");
  scanf("%lf %lf %i",&a,&b,&N);
  dx=(b-a)/N;
  for (j=0;j<N;j=j+1)
  {
    x=a+j*dx;
    f=(myfunction(x)+myfunction(x+dx))/2;
    integral=integral+f*dx;
  }
  printf(" integral= %lf \n",integral);
  return 0;
}
double myfunction(double x)
{
  double fofx;
  fofx=x*x;
  return fofx;
}