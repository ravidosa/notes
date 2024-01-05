#include <stdio.h>
#include <math.h>
/*approximates derivative df/dx for f(x)=x^2 for user-inputted x and dx.
df/dx=8.857759 for x=0.9,dx=0.001.
this makes sense, as (f(x+dx)-f(x))/dx
= ((x+dx)^7e^(x+dx)sin(x+dx)-(x)^7e^(x)sin(x))/dx
As dx approaches 0, this equals e^x * x^6 * ((x+7)sin(x) + xcos(x)), which is the derivative of x^7e^xsin(x)*/
double myfunction7esin();
int main(void)
{
  double x,dx,A,B,deriv;
  printf("Enter x and dx \n");
  scanf("%lf %lf",&x,&dx);
  A=myfunction7esin(x);
  B=myfunction7esin(x+dx);
  deriv=(B-A)/dx;
  printf(" df/dx= %lf \n",deriv);
  return 0;
}
double myfunction7esin(double x)
{
  double fofx;
  fofx=pow(x,7) * exp(x) * sin(x);
  return fofx;
}