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
    float ** A, ** eigenvectors, * eigenvalues;
    char format[] = "%7.3f";  

    printf("Enter dimension of matrix to be diagonalized:\n");  
    scanf("%i",&N);

    A = matrix( 1, N, 1, N);  
    eigenvectors = matrix( 1, N, 1, N);  
    eigenvalues = vector( 1, N);

//  Get the matrix A to be diagonalized

    for (i=1;i<=N;i++)
        {
        printf("Enter elements of row%3i (separated by spaces):\n", i);
        for (j=1;j<=N;j++)
            {
            scanf("%f",&A[i][j]);
            }
        }

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

    printf("\nEigenvalues:\n");
    for (i=1;i<=N;i++)
        {
        printf(format,eigenvalues[i]);
        }
    printf("\n");

    printf("\nEigenvectors:\n");
    for (i=1;i<=N;i++) 
        {
        for (j=1;j<=N;j++)
            {
            printf(format, eigenvectors[i][j]);
            }
        printf("\n"); 
        } 
    printf("\n"); 

//  Free up memory here 
    free_matrix( A, 1, N, 1, N);  
    free_matrix( eigenvectors, 1, N, 1, N);
    free_vector( eigenvalues, 1, N);

    return 0;
}

