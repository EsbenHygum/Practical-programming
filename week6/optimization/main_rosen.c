#include <stdio.h>
#include <math.h>
#include <gsl/gsl_multimin.h>
#include <gsl/gsl_vector.h>


double rosen(const gsl_vector * x, void * params){

	double x0 = gsl_vector_get(x, 0);
	double x1 = gsl_vector_get(x, 1);

	return pow(1-x0, 2) + 100 * pow(x1-x0*x0,2);

}

int main(void){

	int dim = 2, iter = 0, status;

	gsl_vector *x = gsl_vector_alloc(dim);
	gsl_vector_set (x, 0, 0.5);
	gsl_vector_set (x, 1, 0.5);


	double stepsize_ini[2] = {0.01, 0.01};
	gsl_vector *stepsize = gsl_vector_alloc(dim);
	gsl_vector_set (stepsize, 0, stepsize_ini[0]);
	gsl_vector_set (stepsize, 1, stepsize_ini[1]);

	const gsl_multimin_fminimizer_type *type;
	gsl_multimin_fminimizer *solver;
	type = gsl_multimin_fminimizer_nmsimplex2;
	solver = gsl_multimin_fminimizer_alloc(type, dim);
	

	gsl_multimin_function func = {.n=dim,.f=&rosen,.params = NULL};
	gsl_multimin_fminimizer_set(solver, &func, x, stepsize);	
	

	do{
		iter++;
		status = gsl_multimin_fminimizer_iterate(solver);
		if (status)
			break;

		status = gsl_multimin_test_size(solver->size, 1e-5);
		printf("iteration = %i x = %f y = %f solution = %f\n",
				iter, gsl_vector_get(solver->x, 0), 
				gsl_vector_get(solver->x, 1), solver->fval);
	}
	while (status == GSL_CONTINUE && iter < 500);
	if (status == GSL_SUCCESS) printf("Successful convergence!");
	else printf("Convergence failed");
	
	
	gsl_vector_free(x);
	gsl_vector_free(stepsize);
	gsl_multimin_fminimizer_free(solver);


return 0;
}
