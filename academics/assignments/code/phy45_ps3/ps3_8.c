#include <stdio.h>
#include <math.h>
/*writes trajectory of Earth around Sun with user-inputted initial position (x,y), velocity (vx,vy), time step, and steps to file named kepler.csv*/
int main()
{
  double x,y,vx,vy,dt,Fx,Fy,t=0.;
  int i,N;
  double G=6.67*pow(10,-11);
  double Msun=2.0*pow(10,30);
  double Mearth=6.0*pow(10,24);
  double R=1.5*pow(10,11);
  double V=3.0*pow(10,4);
  FILE * fileout;
  fileout=fopen("kepler.csv","w");
  printf("\nEnter initial x,y in terms of R and vx,vy in terms of V \n");
  scanf("%lf %lf %lf %lf",&x,&y,&vx,&vy);
  printf("\nEnter dt,N \n");
  scanf("%lf %i",&dt,&N);
  x=R*x;
  y=R*y;
  vx=V*vx;
  vy=V*vy;
  for (i=1; i<N+1; i=i+1)
  {
    x=x+vx*dt;
    y=y+vy*dt;
    Fx=-1*G*Msun*Mearth/pow(sqrt(pow(x,2)+pow(y,2)),3)*x;
    Fy=-1*G*Msun*Mearth/pow(sqrt(pow(x,2)+pow(y,2)),3)*y;
    vx=vx+Fx/Mearth*dt;
    vy=vy+Fy/Mearth*dt;
    t=t+dt;
    fprintf(fileout,"\n%12.6lf,%12.6lf",x,y);
  }
  fclose(fileout);
  return 0;
}