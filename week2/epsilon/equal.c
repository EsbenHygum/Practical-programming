#include <stdio.h>
#include <math.h>
#include <stdlib.h>


int equal(double a, double b, double tau, double epsilon){
	if(fabs(a - b) < tau){return printf("Since |%g-%g|<%g, I obtain 1.\n", a, b, tau);}
	else if (fabs(a-b)/(fabs(a) + fabs(b)) < epsilon/2){return printf("Since |%g-%g|/(|%g|+|%g|)<%g/2, I obtain 1.\n", a, b, a, b, epsilon);}
	else {return printf("With a=%g, b=%g, tau=%g, and epsilon=%g none of the criteria are met, and I thus obtain 0.\n", a, b, tau, epsilon);};
return 0;
}
