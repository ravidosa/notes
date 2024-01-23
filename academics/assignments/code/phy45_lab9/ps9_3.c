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

    int N,num_rot,i,j; 
    float k;
    float ** A, ** eigenvectors, * eigenvalues;
    char format[] = "%7.3f";  
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
                    A[i][j] = 2*k;
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
                    A[i][j] = 2*k;
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
        A[1][N] = -1 * k;
        A[N][1] = -1 * k;

//  Echo A back to the screen

    printf("\nSolving Eigenproblem for matrix:\n");
    for (i=1;i<=N;i++) 
        {
        for (j=1;j<= N;j++)
            {
            printf(format,A[i][j]);
            }
        printf("\n"); 
        }

//  Heart of the program:  The function jacobi does the diagonalization.

    jacobi( A, N, eigenvalues, eigenvectors, &num_rot);

//  Output the results

    printf("\nNumber of Jacobi rotations: %8i\n", num_rot);

    double min = eigenvalues[0], max = eigenvalues[0];
    int mini = 0, maxi = 0;
    // Traverse the given array
    for (i = 0; i < N; i++)
    {
        // If current element is smaller
        // than min then update it
        if (eigenvalues[i] < min)
        {
            min = eigenvalues[i];
            mini = i;
        }
        // If current element is greater
        // than max then update it
        if (eigenvalues[i] > max)
        {
            max = eigenvalues[i];
            maxi = i;
        }
    }

    printf("\nEigenvalues:\n");
    printf("min eigenvalue: %7.3f\n", min);
    printf("eigenvector of min eigenvalue:\n");
    for (j=1;j<=N;j++)
    {
    printf(format, eigenvectors[i][mini]);
    }
    printf("\nmax eigenvalue: %7.3f\n", max);
    printf("eigenvector of max eigenvalue:\n");
    for (j=1;j<=N;j++)
    {
    printf(format, eigenvectors[i][maxi]);
    }
    for (j=1;j<=N;j++)
    {
        if (j != mini && j != maxi) {
            printf("\nmiddle eigenvalue: %7.3f\n", eigenvalues[j]);
        printf("eigenvector of middle eigenvalue:\n");
        for (i=1;i<=N;i++)
        {
        printf(format, eigenvectors[i][j]);
        }
        } 
    }

//  Free up memory here 
    free_matrix( A, 1, N, 1, N);  
    free_matrix( eigenvectors, 1, N, 1, N);
    free_vector( eigenvalues, 1, N);

    return 0;
}

