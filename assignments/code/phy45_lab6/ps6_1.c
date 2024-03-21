#include <stdio.h>
#include <math.h>
/*solves Laplace equation for given boundary conditions, dx, and dt*/
double initial_cond();
int main(void) {
    int x,y,t,N,xx,yy;
    double L_x,L_y,dx,dy;
    double V_0[2][2];
    FILE * fileout;
    fileout=fopen("laplace.csv","w");
    printf("\nEnter size of box L_x, L_y \n");
    scanf("%lf %lf",&L_x,&L_y);
    printf("\nEnter potential at x=0, x=L_x, y=0, y=L_y \n");
    scanf("%lf %lf %lf %lf",&V_0[0][0],&V_0[1][0],&V_0[0][1],&V_0[1][1]);
    printf("\nEnter number of iterations N, dx, dy \n");
    scanf("%i %lf %lf",&N,&dx,&dy);

    xx = (int)(L_x / dx) + 1;
    yy = (int)(L_y / dy) + 1;
    double V_curr[xx][yy],V_next[xx][yy];

    for (x = 0; x < xx; x = x + 1) {
        for (y = 0; y < yy; y = y + 1) {
            V_curr[x][y] = initial_cond(x, y, xx, yy, V_0);
        }
    }

    for (t = 0; t < N; t = t + 1) {
        for (x = 1; x < xx - 1; x = x + 1) {
            for (y = 1; y < yy - 1; y = y + 1) {
                V_next[x][y] = 0.25*(V_curr[x-1][y] + V_curr[x+1][y] + V_curr[x][y-1] + V_curr[x][y+1]);
            }
        }
        for (x = 1; x < xx - 1; x = x + 1) {
            for (y = 1; y < yy - 1; y = y + 1) {
            V_curr[x][y] = V_next[x][y];
            }
        }
    }
    for (x = 0; x < xx; x = x + 1) {
        for (y = 0; y < yy; y = y + 1) {
            fprintf(fileout,"%12.6lf,",V_curr[x][y]);
        }
        fprintf(fileout,"\n");
    }
    return 0;
}
double initial_cond(int x, int y, int xx, int yy, double V_0[2][2])
{
    if (0 < x && x < xx & y == yy - 1) {
        return V_0[1][1];
    }
    if (0 < x && x < xx & y == 0) {
        return V_0[0][1];
    }
    if (0 < y && y < yy & x == xx - 1) {
        return V_0[1][0];
    }
    if (0 < y && y < yy & x == 0) {
        return V_0[0][0];
    }
    else {
        return 0.0;
    }
}