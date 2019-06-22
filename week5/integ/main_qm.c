#include <stdio.h>
#include <math.h>
#include <gsl/gsl_integration.h>


double num_func(double x, void * params){

	double alpha = *(double *) params; 
	double num_f = exp(- alpha*x*x);
	return num_f;
}

double hamil_func(double x, void * params){

	double alpha = *(double *) params;
	double hamil_f = exp(- alpha*x*x) * ((x*x)/2 + alpha/2 - (alpha*alpha*x*x)/2);
	return hamil_f;
}

int main(void){

	double limit = 1000, n = 10;
	gsl_integration_workspace * work = gsl_integration_workspace_alloc (limit);

	
	gsl_function num_f;
	num_f.function = &num_func;
	gsl_function hamil_f;
	hamil_f.function = &hamil_func;
	
	
	double epsabs = 1e-7, epsrel = 1e-7, num_result, num_error, hamil_result, hamil_error;


	for(double alpha = 0.1; alpha < n; alpha+=0.01){

		num_f.params = &alpha;
		hamil_f.params = &alpha;

		gsl_integration_qagi(&num_f, epsabs, epsrel, limit, work, &num_result, &num_error);
		gsl_integration_qagi(&hamil_f, epsabs, epsrel, limit, work, &hamil_result, &hamil_error);
		double energy = hamil_result / num_result; 
		printf("%g %g\n", alpha, energy);
	}

	gsl_integration_workspace_free(work);

return 0;
}
