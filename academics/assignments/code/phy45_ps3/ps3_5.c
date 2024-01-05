#include <stdio.h>
#include <math.h>
/*writes trajectory of mass with user-inputted initial position, velocity, constant force, mass, frictional constant, time step, and steps on spring to file named mass_spring.csv.*/
int main()
{
  double x,v,m,F0,b,dt,F,t=0.;
  int i,N;
  FILE * fileout;
  fileout=fopen("mass_spring.csv","w");
  printf("\nEnter initial x,v \n");
  scanf("%lf %lf",&x,&v);
  printf("\nEnter F,m,b,dt,N \n");
  scanf("%lf %lf %lf %lf %i",&F0,&m,&b,&dt,&N);
  for (i=1; i<N+1; i=i+1)
  {
    x=x+v*dt;
    F=F0-b*v;
    v=v+F/m*dt;
    t=t+dt;
    fprintf(fileout,"\n%12.6lf,%12.6lf,%12.6lf",t,x, v);
  }
  fclose(fileout);
  return 0;
}