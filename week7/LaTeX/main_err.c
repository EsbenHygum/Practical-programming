#include <stdio.h>
#include <math.h>
#include <gsl/gsl_integration.h>


double err(double x, void * params){

	double u = 2/sqrt(M_PI)*exp(-(x*x)); 
	return u;
}


int main(int argc, char *argv[]){
	
	double a, b, dx;
	sscanf(argv[1], "%lg", &a);
	sscanf(argv[2], "%lg", &b);
	sscanf(argv[3], "%lg", &dx);

	int limit = 1000;

	gsl_integration_workspace *work = gsl_integration_workspace_alloc(limit);
	double epsabs = 1e-6, epsrel = 1e-6, result, error;

	gsl_function f;
	f.function = &err;
	f.params = NULL;

	for(double i = a; i <= b; i += dx){
		
		gsl_integration_qags(&f, 0, i, epsabs, epsrel, limit, work, &result, &error);
		printf("%g %g\n", i, result);
	}

	gsl_integration_workspace_free(work);
return 0;
}
