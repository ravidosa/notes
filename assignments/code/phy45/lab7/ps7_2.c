#include <stdio.h>
#include <math.h>
/*solves Laplace equation for given boundary conditions, dx, and dt*/
double initial_cond();
int main(void) {
    int x,y,t,N;
    double dx,dy;
    double lengths[5];
    double V[5];
    FILE * fileout;
    fileout=fopen("laplace.csv","w");
    printf("\nEnter lengths of red/blue/green/magenta/cyan sections \n");
    scanf("%lf %lf %lf %lf %lf", &lengths[0], &lengths[1], &lengths[2], &lengths[3], &lengths[4]);
    printf("\nEnter potential along r/b/g/m/c sections \n");
    scanf("%lf %lf %lf %lf %lf", &V[0], &V[1], &V[2], &V[3], &V[4]);
    printf("\nEnter number of iterations N, dx, dy \n");
    scanf("%i %lf %lf",&N,&dx,&dy);

    const int R = (int)(lengths[0] / dx);
    const int B = (int)(lengths[1] / dx);
    const int G = (int)(lengths[2] / dx);
    const int M = (int)(lengths[3] / dx);
    const int C = (int)(lengths[4] / dx);
    double V_curr[R + 1][B + M + 1],V_next[R + 1][B + M + 1];

    for (x = 0; x < R + 1; x = x + 1) {
        for (y = 0; y < B + M + 1; y = y + 1) {
            V_curr[x][y] = initial_cond(x, y, V, R, G, B, M);
        }
    }

    for (t = 0; t < N; t = t + 1) {
        for (x = 1; x < R; x = x + 1) {
            for (y = 1; y < B; y = y + 1) {
                V_next[x][y] = 0.25*(V_curr[x-1][y] + V_curr[x+1][y] + V_curr[x][y-1] + V_curr[x][y+1]);
            }
        }
        V_next[G][B - 1] = 0.25*(V_curr[G-1][B-1] + V_curr[G+1][B-1] + V_curr[G][B - 1-1] + 6);
        V_next[G + 1][B] = 0.25*(2 + V_curr[G + 1+1][B] + V_curr[G + 1][B-1] + V_curr[G + 1][B+1]);
        for (x = G + 2; x < R - G - 1; x = x + 1) {
            V_next[x][B] = 0.25*(V_curr[x-1][y] + V_curr[x+1][y] + V_curr[x][y-1] + V_curr[x][y+1]);
        }
        V_next[R - G - 1][B] = 0.25*(2 + V_curr[R - G - 1-1][B] + V_curr[R - G - 1][B-1] + V_curr[R - G - 1][B+1]);
        V_next[R - G][B - 1] = 0.25*(V_curr[R - G-1][B-1] + V_curr[R - G+1][B-1] + V_curr[R - G][B - 1-1] + 6);
        for (x = G + 1; x < R - G; x = x + 1) {
            for (y = B + 1; y < B + M; y = y + 1) {
                V_next[x][y] = 0.25*(V_curr[x-1][y] + V_curr[x+1][y] + V_curr[x][y-1] + V_curr[x][y+1]);
            }
        }
        for (x = 1; x < R; x = x + 1) {
            for (y = 1; y < B; y = y + 1) {
                V_curr[x][y] = V_next[x][y];
            }
        }
        for (x = G + 1; x < R - G; x = x + 1) {
            for (y = B; y < B + M; y = y + 1) {
                V_curr[x][y] = V_next[x][y];
            }
        }
    }
    for (x = 0; x < R + 1; x = x + 1) {
        for (y = 0; y < B + M + 1; y = y + 1) {
            fprintf(fileout,"%12.6lf,",V_curr[x][y]);
        }
        fprintf(fileout,"\n");
    }
    return 0;
}
double initial_cond(int x, int y, double V[5], int R, int B, int G, int M)
{
    if (0 < x && x < R && y == 0) {
        return V[0];
    }
    else if (0 < y && y < B && (x == 0 || x == R)) {
        return V[1];
    }
    else if (((0 < x && x < G) || (R - G < x && x < R)) && y == B) {
        return V[2];
    }
    else if ((B < y && y < B + M) && (x == G || x == R - G)) {
        return V[3];
    }
    else if ((G < x && x < R - G) && y == B + M) {
        return V[4];
    }
    else {
        return 0.0;
    }
}