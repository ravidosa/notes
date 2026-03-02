#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main() {
    int i,N;
    printf("\nEnter N \n");
    scanf("%i",&N);
    double x,y;
    FILE * fileout;
    fileout=fopen("random2d.csv","w");
    for(i=1;i<N;i=i+1) {
        x = (double)rand()/RAND_MAX;
        y = (double)rand()/RAND_MAX;
        fprintf(fileout, "%12.8lf,%12.8lf, \n",x,y);
    }
}