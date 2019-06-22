#include <stdio.h>
#include <math.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_multimin.h>

struct exp_data {int n; double *t, *y, *err;};

double mini_fun(const gsl_vector * x, void * params){

	double A = gsl_vector_get(x, 0);
	double B = gsl_vector_get(x, 1);
	double T = gsl_vector_get(x, 2);

	struct exp_data *given = (struct exp_data*) params;
	int n = given -> n;
	double *t = given -> t;
	double *y = given -> y;
	double *err = given -> err;

	double sum = 0;

	for(int ii = 0; ii < n; ii++) sum += pow(A*exp(-t[ii]/T)+B - y[ii], 2)/pow(err[ii],2);
	return sum;
}



int main(){
	
	double t[]= {0.47,1.41,2.36,3.30,4.24,5.18,6.13,7.07,8.01,8.95};
	double y[]= {5.49,4.08,3.54,2.61,2.09,1.91,1.55,1.47,1.45,1.25};
	double err[]= {0.26,0.12,0.27,0.10,0.15,0.11,0.13,0.07,0.15,0.09};
	int n = sizeof(t)/sizeof(t[0]);

	struct exp_data par = {.n = n, .t = t, .y = y, .err = err};

	int dim = 3, iter = 0, status;

	gsl_vector *x = gsl_vector_alloc(dim);
	gsl_vector_set (x, 0, 1.);
	gsl_vector_set (x, 1, 0.5);
	gsl_vector_set (x, 2, 1.);
	
	double step_ini[3] = {0.1, 0.1, 0.1};
	gsl_vector *stepsize = gsl_vector_alloc (dim);
	gsl_vector_set (stepsize, 0, step_ini[0]);
	gsl_vector_set (stepsize, 1, step_ini[1]);
	gsl_vector_set (stepsize, 2, step_ini[2]);


	const gsl_multimin_fminimizer_type *type;
	gsl_multimin_fminimizer *solver;
	type = gsl_multimin_fminimizer_nmsimplex2;
	solver = gsl_multimin_fminimizer_alloc (type, dim);

	gsl_multimin_function multi_fun = {.n = dim, .f = &mini_fun, 
		.params = (struct exp_data*) &par};
	gsl_multimin_fminimizer_set(solver, &multi_fun, x, stepsize);


	do {
		iter++;
		status = gsl_multimin_fminimizer_iterate(solver);
		if (status)
			break;

		status = gsl_multimin_test_size(solver -> size, 1e-5),
		       printf("iteration = %i A = %g B = %g T = %g sum = %g\n", iter, 
				       gsl_vector_get(solver->x, 0), 
				       gsl_vector_get(solver->x, 1),
				       gsl_vector_get(solver->x, 2), 
				       solver -> fval);

	}
	while (status == GSL_CONTINUE && iter < 1000);
	if (status == GSL_SUCCESS) printf("Successful convergence!");
	else printf("Convergence failed");


	double best_A = gsl_vector_get(solver->x, 0), best_B = gsl_vector_get(solver->x, 1),
	       best_T = gsl_vector_get(solver->x, 2);


	FILE * fp;
	fp = fopen ("data_for_plot.txt", "w");

	fprintf(fp, "Given data:\n\n");
	for(int ii = 0; ii < n; ii++) fprintf(fp, "%g %g %g\n", t[ii], y[ii], err[ii]);
	fprintf(fp, "\n\nCalculated data:\n\n");
	for(double ii = 0.; ii < 10; ii += 0.1) fprintf(fp, "%g %g\n", ii, best_A * exp(-ii/best_T) + best_B);	


	fclose(fp);


	gsl_vector_free(x);
	gsl_vector_free(stepsize);
	gsl_multimin_fminimizer_free(solver);
	

return 0;
}
