#include <stdio.h>
/*tests locker problem for first N positive integers (0 = open, 1 = closed)*/
int main(void) {
  int i, j, s;
  int lockers[1000] = {0};
  for(i = 1; i <= 1000; i = i+1)
  {
    for(j = i; j <= 1000; j = j + i)
    {
      lockers[j] = 1 - lockers[j];
    }
  }
  printf("\nThe following lockers are open:");
  s = 0;
  for(i = 1; i <= 1000; i = i + 1)
  {
    if (lockers[i]==0) {
      printf("\n%i", i);
      s = s + 1;
    }
  }
  printf("\nThe following lockers are closed:");
  s = 0;
  for(i = 1; i <= 1000; i = i + 1)
  {
    if (lockers[i] == 1) {
      printf("\n%i", i);
      s = s + 1;
    }
  }
  printf("\nIn total, %i lockers are closed.", s);
  printf("\n");
  return 0;
}

/*The closed locker numbers are all perfect squares; since they have an odd number of factors, they are interacted with an odd number of times, and are thus closed.*/