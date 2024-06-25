#include <stdio.h>
#include <math.h>
/*computes intersection of lines m_1x+b_1 and m_2x+b_2 for user-inputted floats m_1, m_2, b_1, and b_2.*/
int main(void)
{
  double x, y, m_1, m_2, b_1, b_2;
  printf("\nEnter m_1\n");
  scanf("%lf", &m_1);
  printf("\nEnter m_2\n");
  scanf("%lf", &m_2);
  printf("\nEnter b_1\n");
  scanf("%lf", &b_1);
  printf("\nEnter b_2\n");
  scanf("%lf", &b_2);
  if (m_1 == m_2) {
    printf("The lines are parallel and do not intersect.");
  }
  else {
  x=(b_1 - b_2)/(m_2 - m_1);
  y=m_1 * x + b_1;
  printf("\nThe lines intersect at (%lf, %lf)\n", x, y);
  return 0;
  }
}