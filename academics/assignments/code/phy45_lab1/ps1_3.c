#include <stdio.h>
#include <math.h>
/*computes and prints roots of quadratic equation ax^2+bx+c for user-inputted floats a, b, and c. this accounts for negative discrimants by ensuring that the discriminant is positive before computing the roots*/
int main()
{
  double a, b, c, disc, root1, root2;
  printf("Enter a, b, and c: \n");
  scanf("%lf %lf %lf", &a, &b, &c);
  disc = b * b - 4.0 * a * c;
  if (disc > 0)
  {
    root1 = (-b + sqrt(disc)) / (2.0 * a);
    root2 = (-b - sqrt(disc)) / (2.0 * a);
    printf("First root is %lf \n", root1);
    printf("Second root is %lf \n", root2);
  }
  else
  {
    printf("The discriminant is negative. There are no real roots.\n");
  }
  return 0;
}