#include <stdio.h>
#include <math.h>
/*writes trajectory of mass with user-inputted initial position, velocity, spring constant, mass, time step, and steps on spring to file named Dumbledore.txt.
a) the initial values make sense because the mass is beginning to move towards the equilibrium at 0, its velocity slowly increasing from 0.
b) the part where the value changes signs is when the mass passes the equilibrium point and is at its highest velocity, which is of magnitude x*sqrt(k/m) = 5*sqrt(8/2)=10
since it is moving downwards, it is -10*/
int main()
{
  double x,v,k,m,dt,a,t=0.;
  int i,N;
  FILE * fileout;
  fileout=fopen("Dumbledore.txt","w");
  printf("\nEnter initial x,v \n");
  scanf("%lf %lf",&x,&v);
  printf("\nEnter k,m,dt,N \n");
  scanf("%lf %lf %lf %i",&k,&m,&dt,&N);
  for (i=1; i<N+1; i=i+1)
  {
    x=x+v*dt;
    a=-k*x/m;
    v=v+a*dt;
    t=t+dt;
    fprintf(fileout,"\n%12.6lf %12.6lf %12.6lf",t,x, v);
  }
  fclose(fileout);
  return 0;
}