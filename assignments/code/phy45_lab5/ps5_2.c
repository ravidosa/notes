#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int i,N,M=0;
    printf("\nEnter N \n");
    scanf("%i",&N);
    double x,y;
    for(i=1;i<N;i=i+1) {
        x = (double)rand()/RAND_MAX;
        y = (double)rand()/RAND_MAX;
        if (pow(x, 2) + pow(y, 2) < 1) {
            M = M + 1;
        }
    }
    printf("%12.8lf \n",(double)M/N);
}