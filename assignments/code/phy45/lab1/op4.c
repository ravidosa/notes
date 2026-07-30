#include <stdio.h>
#include <math.h>
/*computes root of e^x-x-5 through bisection method and newton's method. newton's method is more accurate*/
int main(void)
{
  bisection(1, 2);
  newton(2);
}

int bisection(int a1, int b1) {
  float c, f_a, f_b, f_c;
  int i;
  float a = a1;
  float b = b1;
  for (i = 0; i < 10; i = i + 1) {
    f_a = exp(a) - a - 5;
    f_b = exp(b) - b - 5;
    c = (a + b) / 2;
    f_c = exp(c) - c - 5;
    if ((f_a < 0) == (f_c < 0)) {
      a = c;
    } 
    else if ((f_b < 0) == (f_c < 0)) {
      b = c;
    } 
  }
  printf("The root is at approximately %lf.\n", c);
  return 0;
}

int newton(int x1) {
  int i;
  float x=x1;
  for (i=0; i<10; i=i+1) {
    x=x-(exp(x)-x-5)/(exp(x)-1);
  }
  printf("The root is at approximately %lf.\n",x);
}