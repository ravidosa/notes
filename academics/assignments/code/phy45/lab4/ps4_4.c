#include <stdio.h>
#include <math.h>
/*approximates derivative d^2f/dx^2 for f(x)=x^4 for user-inputted x and dx.*/
double myfunction4();
int main(void)
{
  double x,dx,A,B,C,deriv2;
  printf("Enter x and dx \n");
  scanf("%lf %lf",&x,&dx);
  A=myfunction4(x);
  B=myfunction4(x+dx);
  C=myfunction4(x-dx);
  deriv2=(B+C-2.*A)/(dx*dx);
  printf("d^2f/dx^2= %lf \n",deriv2);
  return 0;
}
double myfunction4(double x)
{
  double fofx;
  fofx=pow(x,4);
  return fofx;
}