#include <stdio.h>
#include <math.h>
/*approximates integral of f(x) from x=a to x=b using the trapezoidal rule with user-inputted integer N segments for f(x) = sqrt(9-x^2) from x=0 to x=3.
yields 6.985 for N=10, 7.065938 for N=100, 7.068500 for N=1000.
this is equivalent to a quarter circle with radius 3, or 9pi/4, which is what the area under the curve looks like*/
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
  fofx=sqrt(9-pow(x,2));
  return fofx;
}