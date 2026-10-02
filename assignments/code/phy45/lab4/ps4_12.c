#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int i,N;
    unsigned int seed;
    printf("\nEnter number of steps and seed \n");
    scanf("%i %u",&N,&seed);
    double r[N],s;
    FILE * fileout;
    fileout=fopen("walk.csv","w");
    srand(seed);
    r[0]=0;
    for(i=1;i<N;i=i+1) {
        s = (double)rand()/RAND_MAX;
        if (s > 0.5) {
            r[i]=r[i-1] + 1;
        }
        else {
            r[i]=r[i-1] - 1;
        }
    }
    for(i=0;i<N;i=i+1) {
        fprintf(fileout, "%i,%12.8lf, \n",i,r[i]);
    }
}