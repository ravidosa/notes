#include <stdio.h>
#include <math.h>
/*approximates integral of f(x) from x=a to x=b using the trapezoidal rule with user-inputted integer N segments.
since this integral is impossible to do by hand, it can be approximated by using pi as the division point between segments as the value of the function can be computed easily*/
double myfunctioncomp();
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
    f=(myfunctioncomp(x)+myfunctioncomp(x+dx))/2;
    integral=integral+f*dx;
  }
  printf(" integral= %lf \n",integral);
  return 0;
}
double myfunctioncomp(double x)
{
  double fofx;
  fofx=(pow(x,0.34)*exp(0.25*x)*sin(x))/(2.2+0.9*sqrt(x));
  return fofx;
}