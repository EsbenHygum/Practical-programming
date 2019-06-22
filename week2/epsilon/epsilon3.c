#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "equal.c"

int main(){

	printf("\n\n---------- Part 3 ----------\n\n");
	double a = 7.0;
	double b = 10.0;
	double tau = 4.0;
	double epsilon = 10.0;
	equal(a, b, tau, epsilon);
	
	double tau2 = 1;
	equal(a, b, tau2, epsilon);

	double epsilon2 = 3/18;
	equal(a, b, tau2, epsilon2);

return 0;
}



