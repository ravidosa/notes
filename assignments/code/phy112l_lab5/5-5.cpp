using namespace std;
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>

int right_shift(int t, int s) {
    return t / pow(3,  s);
}

int mul(int N, int t1, int t2) {
    int p = 0;
    for (int i = 0; i < N;  i++) {
        p += (int(pow(3, i)) * ((((t1 % 3) * (t2 % 3))) % 3));
        t1 = t1 / 3;
        t2 = t2 / 3;
    }
    return p;
}

int count(int N, int t, int s) {
    int p = 0;
    for (int i = 0; i < N;  i++) {
        if (t % 3 == s) {
            p += 1;
        }
        t = t / 3;
    }
    return p;
}

int main(void) {
    int J = 1;
    int N_1 = 4;
    int N_2 = 4;
    int N = N_1 * N_2;
    int states = int(pow(3, N));
    int E_max = J * (N_1 * (N_2 - 1) + (N_1 - 1) * N_2);
    int E_n[2 * E_max + 1] = {0};
    FILE * fileout;
    fileout=fopen("mod_ising.txt","w");

    int m = 0;
    for (int i = 0; i < N_2; i++) {
        m += pow(3, N_1 * i);
    }

    for (int i = 0; i < states; i++) {
        int anti_1 = mul(N, mul(N, i, right_shift(i, 1)), (pow(3, N_1 - 1) - 1) / 2 * m);
        int anti_2 = mul(N, mul(N, i, right_shift(i, N_1)), (pow(3,  N_1 * (N_2 - 1)) - 1) / 2);
        int E = -1 * J * (count(N, anti_1, 1) + count(N, anti_2, 1) - count(N, anti_1, 2) - count(N, anti_1, 2));
        E_n[E + E_max] += 1;
    }

    for (int i = 0; i < 2 * E_max + 1; i++) {
        fprintf(fileout,"%i %i\n", -E_max + i, E_n[i]);
    }
    return 0;
}