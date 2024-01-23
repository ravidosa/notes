#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int i,j,N;
    unsigned int seed;
    printf("\nEnter number of iterations and seed \n");
    scanf("%i %u",&N,&seed);
    double mom[6];
    double r;
    FILE * fileout;
    fileout=fopen("random_moment.csv","w");
    srand(seed);
    for(i=0;i<N;i=i+1) {
        r=(double)rand()/RAND_MAX;
        for (j=0;j<6;j=j+1) {
            mom[j] = mom[j] + pow(r, j+1)/N;
        }
    }
    for(i=0;i<6;i=i+1) {
        fprintf(fileout, "%i,%12.8lf, \n",i,mom[i]);
    }
}