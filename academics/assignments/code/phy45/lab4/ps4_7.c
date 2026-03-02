#include <stdio.h>
#include <math.h>
/*solves diffusion equation for given N, Nbox, D, dx, and dt*/
double initial_cond();
int main(void) {
    int x,t,N,Nbox;
    double D,dx,dt;
    FILE * fileout;
    fileout=fopen("diffusion.csv","w");
    printf("\nEnter diffusion constant D \n");
    scanf("%lf",&D);
    printf("\nEnter number of time steps N and number of boxes Nbox \n");
    scanf("%i %i",&N,&Nbox);
    printf("\nEnter dx, dt \n");
    scanf("%lf %lf",&dx,&dt);

    double rho_curr[Nbox],rho_next[Nbox];

    for (x = 0; x < Nbox; x = x + 1) {
        rho_curr[x] = initial_cond(x);
    }
    for (t = 0; t < N; t = t + 1) {
        for (x = 1; x < Nbox - 1; x = x + 1) {
            rho_next[x] = rho_curr[x] + D*dt/pow(dx,2)*(rho_curr[x+1]+rho_curr[x-1]-2.*rho_curr[x]);
        }
        for (x = 1; x < Nbox - 1; x = x + 1) {
            rho_curr[x] = rho_next[x];
        }
    }
    for (x = 0; x < Nbox; x = x + 1) {
        fprintf(fileout,"\n%i,%12.6lf,",x,rho_curr[x]);
    }
    return 0;
}
double initial_cond(int x)
{
    if (x == 500) {
        return 1.0;
    }
    else {
        return 0.0;
    }
}