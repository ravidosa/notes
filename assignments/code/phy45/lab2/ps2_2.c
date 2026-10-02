#include <stdio.h>
#include <math.h>
/*approximates derivative df/dx for f(x)=x^2 for user-inputted x and dx.
df/dx=-0.049958 for x=0,dx=0.1 and df/dx=-0.999987 for x=1.57,dx=0.01.
this makes sense, as (f(x+dx)-f(x))/dx = (cos(x+dx)-cos(x))/dx
= (cos(x)cos(dx)+sin(x)sin(dx)-cos(x))/dx
= (cos(x)(cos(dx)-1)+sin(x)sin(dx))/dx
As dx approaches 0, this equals sin(x), which is the derivative of cos(x) (as found analytically).*/
double myfunctioncos();
int main(void)
{
  double x,dx,A,B,deriv;
  printf("Enter x and dx \n");
  scanf("%lf %lf",&x,&dx);
  A=myfunctioncos(x);
  B=myfunctioncos(x+dx);
  deriv=(B-A)/dx;
  printf(" df/dx= %lf \n",deriv);
  return 0;
}
double myfunctioncos(double x)
{
  double fofx;
  fofx=cos(x);
  return fofx;
}