#include <stdio.h>
#include <math.h>
/*computes and prints roots of quadratic equation ax^2+bx+c for user-inputted floats a, b, and c. this accounts for positive, negative, and zero-valued discriminants. if the discriminant is positive, the quadratic equation will have two real roots, with the representative parabola intersecting the x-axis at two points. if the discriminant is 0, the quadratic equation will have one real root, with the representative parabola intersecting the x-axis at one point. if the discriminant is negative, the quadratic equation will have two complex, non-real roots, with the representative parabola intersecting the x-axis at zero points.*/
int main()
{
  double a, b, c, disc, root1, root2, root_re, root_im;
  printf(" Please enter a, b, and c \n");
  scanf("%lf %lf %lf", &a, &b, &c);
  disc = b * b - 4.0 * a * c;
  if (disc > 0)
  {
    root1 = (-b + sqrt(disc)) / (2.0 * a);
    root2 = (-b - sqrt(disc)) / (2.0 * a);
    printf("\n First root is %lf ", root1);
    printf("\n Second root is %lf ", root2);
  }
  if (disc == 0)
  {
    root1 = (-b ) / (2.0 * a);
    printf("\n Root is %lf ", root1);
  }
  if (disc < 0)
  {
    root_re = (-b) / (2.0 * a);
    root_im = (sqrt(abs(disc))) / (2.0 * a);
    printf("\n First root is %lf+%lfi ", root_re, root_im);
    printf("\n Second root is %lf-%lfi ", root_re, root_im);
  }
  printf("\n");
  return 0;
}