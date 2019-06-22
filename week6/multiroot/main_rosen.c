#include <stdio.h>
#include <gsl/gsl_multiroots.h>
#include <gsl/gsl_vector.h>

int rosenbrock(const gsl_vector * x, void * params, gsl_vector * f){

	const double x0 = gsl_vector_get(x, 0);
	const double x1 = gsl_vector_get(x, 1);

	double f0 = -2*(1 - x0) - 400*x0*(x1 - x0*x0);
	double f1 = 200*(x1 - x0*x0);

	gsl_vector_set(f, 0, f0);
	gsl_vector_set(f, 1, f1);

	return GSL_SUCCESS;
}


int printing(int iter, gsl_multiroot_fsolver * s){

	printf("iter = %d x = %.3f y = %.3f dfdx = %.3e dfdy = %.3e\n", iter, 
			gsl_vector_get(s->x, 0), 
			gsl_vector_get(s->x, 1),
			gsl_vector_get(s->f, 0),
			gsl_vector_get(s->f, 1));

return 0;
}

int main(void){

	const gsl_multiroot_fsolver_type *type;
	gsl_multiroot_fsolver *solver;
		
	int dim = 2;
	gsl_multiroot_function func = {&rosenbrock, dim, NULL};

	double x_initial[2] = {0.5, 0.5};
	gsl_vector *x = gsl_vector_alloc(dim);
	gsl_vector_set (x, 0, x_initial[0]);
	gsl_vector_set (x, 1, x_initial[1]);

	type = gsl_multiroot_fsolver_hybrids;
	solver = gsl_multiroot_fsolver_alloc(type, dim);
	gsl_multiroot_fsolver_set(solver, &func, x);


	int status; 
	size_t iter = 0;
	double prec = 1e-10;
	printing(iter, solver);

	do{
		iter++;
		status = gsl_multiroot_fsolver_iterate (solver);
		
		printing(iter, solver);
		if (status)
			break;
	
		status = gsl_multiroot_test_residual(solver->f, prec);
	}
	while(status == GSL_CONTINUE && iter < 1000);

	printf("status = %s\n", gsl_strerror (status));

	gsl_multiroot_fsolver_free(solver);
	gsl_vector_free(x);

return 0;
}


