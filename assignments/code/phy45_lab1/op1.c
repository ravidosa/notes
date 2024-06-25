#include <stdio.h>
/*tests collatz conjecture for first N positive integers*/
int main(void) {
  int i, N;
  printf("\nEnter N\n");
  scanf("%i", &N);
  for(i = 1; i <= N; i = i + 1)
  {
    if (collatz(i) == 0) {
      printf("\nThe Collatz Conjecture holds for %i", i);
    }
  }
  printf("\n");
  return 0;
}

/*tests collatz conjecture for integer n*/
int collatz(int n) {
  if (n == 1) {
    return 0;
  }
  if (n % 2 == 0) {
  return collatz(n / 2);
  }
  if (n % 2 != 0) {
  return collatz(n * 3 + 1);
  }
}

/*for sufficiently large N, N itself or 3N+1 may exceed INT_MAX. further, it may take too long for the computation to be completed. while the first issue cannot be solved easily, for the second option, a potential solution would be to automatically return 0 once the algorithm returns a value less than the original n. this works because in this implementation, if the collatz conjecture is not satisfied, the algorithm would (presumably) be trapped in an infinite loop. therefore, for a number to be checked for validity, it can be assumed that all numbers less than it have satisfied the collatz conjecture. if the algorithm returns a value equal to the original n, this would disprove the collatz conjecture, as this would be a cycle that would never reach 1*/