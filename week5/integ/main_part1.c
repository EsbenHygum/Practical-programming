#include <stdio.h>
#include <math.h>
#include <gsl/gsl_integration.h>


double func(double x, void * params){


	double f = log(x) / sqrt(x); 
	return f;
}


int main(void){

	printf("Part 1:\n");

	int limit = 1000;
	gsl_integration_workspace *work = gsl_integration_workspace_alloc(limit);
	double low_lim = 0.0, up_lim = 1.0, epsabs = 1e-5, epsrel = 1e-5, result, error;

	gsl_function f;
	f.function = &func;
	f.params = NULL;

	gsl_integration_qags(&f, low_lim, up_lim, epsabs, epsrel, limit, work, &result, &error);
	printf("A numerical integration of the function yields the result =  %f\n", result);

	gsl_integration_workspace_free(work);
return 0;
}
