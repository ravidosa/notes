#include <stdio.h>
#include <math.h>
/*approximates derivative d^2f/dx^2 for f(x)=e^x + 2/x for user-inputted x and dx.
for x=1.0 and dx=0.1, d^2f/dx^2=6.760952
for x=1.0 and dx=0.01, d^2f/dx^2=6.718705
for x=1.0 and dx=0.001, d^2f/dx^2=6.718286.
this makes sense the program as computes the second derivative using:
(e^(x+dx)+2/(x+dx) + e^(x-dx)+2/(x-dx) - 2*(e^x+2/x))/(dx*dx).
this value is approaching e+4 as dx approaches 0*/
double myfunctione2();
int main(void)
{
  double x,dx,A,B,C,deriv2;
  printf("Enter x and dx \n");
  scanf("%lf %lf",&x,&dx);
  A=myfunctione2(x);
  B=myfunctione2(x+dx);
  C=myfunctione2(x-dx);
  deriv2=(B+C-2.*A)/(dx*dx);
  printf(" d^2f/dx^2= %lf \n",deriv2);
  return 0;
}
double myfunctione2(double x)
{
  double fofx;
  fofx=exp(x)+2/x;
  return fofx;
}