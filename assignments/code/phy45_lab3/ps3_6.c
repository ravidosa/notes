#include <stdio.h>
#include <math.h>
/*writes trajectory of mass with user-inputted initial position (x,y), velocity (vx,vy), mass, time step, and steps on spring to file named projectile.csv.
here, a do-while loop is better because the program will stop when the projectile hits the ground (x < 0),
as opposed to having to calculate the approximate time of impact to set the number of time steps needed.*/
int main()
{
  double x,m,y,vx,vy,dt,Fx,Fy,t=0.;
  int i;
  FILE * fileout;
  fileout=fopen("projectile.csv","w");
  printf("\nEnter initial x,y,vx,vy \n");
  scanf("%lf %lf %lf %lf",&x,&y,&vx,&vy);
  printf("\nEnter m,dt \n");
  scanf("%lf %lf",&m,&dt);
  do
  {
    x=x+vx*dt;
    y=y+vy*dt;
    Fx=0.*m;
    Fy=-9.8*m;
    vx=vx+Fx/m*dt;
    vy=vy+Fy/m*dt;
    t=t+dt;
    fprintf(fileout,"\n%12.6lf,%12.6lf",x,y);
  } while (y > 0);
  fclose(fileout);
  return 0;
}