// jacobi_test.c
//   Matrix Diagonalizer from "Numerical Recipes" 
//   Uses FORTRAN indexing convention in which array start from '1'
//   N is the dimansion of the matrix.
//   The matrix must be symmetric.
//   The eigenvectors come out as columns.
//   Matrix A overwritten during solution.  Save a copy if needed.

#include <stdio.h>
#include "nrutil.h"

void jacobi(float **a, int n, float d[], float **v, int *nrot);

int main() {

    int N,num_rot,i,j,l; 
    float k,dot;
    float ** A, ** eigenvectors, * eigenvalues;
    char format[] = "%7.3f,";  
    FILE * fileout;
    fileout=fopen("eigen.csv","w");

    printf("Enter number of masses N and spring constant k:\n");  
    scanf("%i %f",&N,&k);


    A = matrix( 1, N, 1, N);  
    eigenvectors = matrix( 1, N, 1, N);  
    eigenvalues = vector( 1, N);

//  Get the matrix A to be diagonalized
    for (i=1;i<=N;i++)
        {
        for (j=1;j<=N;j++)
            {
            if (j == 1) {
                if (i == j) {
                    A[i][j] = k;
                }
                else if (i == j + 1) {
                    A[i][j] = -1 * k;
                }
                else {
                    A[i][j] = 0;
                }
            }
            else if (j == N) {
                if (i == j) {
                    A[i][j] = k;
                }
                else if (i == j - 1) {
                    A[i][j] = -1 * k;
                }
                else {
                    A[i][j] = 0;
                }
            }
            else {
                if (i == j) {
                    A[i][j] = 2*k;
                }
                else if (i == j + 1 || i == j - 1) {
                    A[i][j] = -1 * k;
                }
                else {
                    A[i][j] = 0;
                }
            }
            }
        }

//  Echo A back to the screen

    printf("\nSolving Eigenproblem for matrix:\n");
    for (i=1;i<=N;i++) 
        {
        for (j=1;j<= N;j++)
            {
            //printf(format,A[i][j]);
            }
        //printf("\n"); 
        }

//  Heart of the program:  The function jacobi does the diagonalization.

    jacobi( A, N, eigenvalues, eigenvectors, &num_rot);

//  Output the results

    printf("\nNumber of Jacobi rotations: %8i\n", num_rot);

    printf("\nEigenvalues:\n");
    for (i=1;i<=N;i++)
        {
        //printf(format,eigenvalues[i]);
        //fprintf(fileout,"%12.6lf,",eigenvalues[i]);
        }
    printf("\n");

    printf("\nEigenvectors:\n");
    for (i=1;i<=N;i++) 
        {
        for (j=1;j<=N;j++)
            {
            dot = 0;
            for (l=1;l<=N;l++)
            {
                dot = dot + eigenvectors[i][l] * eigenvectors[j][l];
            }
            fprintf(fileout, format, dot);
            }
        fprintf(fileout, "\n"); 
        } 
    fprintf(fileout, "\n"); 

//  Free up memory here 
    free_matrix( A, 1, N, 1, N);  
    free_matrix( eigenvectors, 1, N, 1, N);
    free_vector( eigenvalues, 1, N);

    return 0;
}

