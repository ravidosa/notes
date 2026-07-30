#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    double R;
    int i,N;
    unsigned int seed;
    printf("\nEnter number of iterations and seed");
    printf("\n");
    scanf("%i %u",&N,&seed);
    srand(seed);
    for(i=0;i<N;i=i+1) {
        R=(double)rand()/RAND_MAX;
        printf("%12.8lf \n",R);
    }
    printf("\n");
}