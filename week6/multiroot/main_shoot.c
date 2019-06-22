#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <gsl/gsl_odeiv2.h>
#include <gsl/gsl_multiroots.h>
#include <gsl/gsl_errno.h>


double diff_solver(double epsilon, double r);

int printing(int iter, gsl_multiroot_fsolver * s){

	printf("iter = %d epsilon = %.3f M(epsilon) = %.3e\n", iter, 
			gsl_vector_get(s->x, 0), 
			gsl_vector_get(s->f, 0));

return 0;
}

int auxiliary(const gsl_vector *energy, void *param, gsl_vector *f){
	
	double epsilon = gsl_vector_get(energy, 0);
	double rmax = *(double*) param;
	double feval = diff_solver(epsilon, rmax);
	gsl_vector_set(f, 0, feval);

	return GSL_SUCCESS;
}


int main(){
	
	int dim = 1;
	double rmax = 8;

	const gsl_multiroot_fsolver_type *type;
	gsl_multiroot_fsolver *solver;
	gsl_multiroot_function func = {&auxiliary, dim, &rmax};

	gsl_vector *energy = gsl_vector_alloc(dim);
	gsl_vector_set(energy, 0, -1);

	type = gsl_multiroot_fsolver_hybrids;
	solver = gsl_multiroot_fsolver_alloc(type, dim);
	gsl_multiroot_fsolver_set(solver, &func, energy);


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

	
	double epsilon = gsl_vector_get(solver->x, 0);
	
	FILE * fp;
	fp = fopen("out_plot_dat.txt", "w");
	
	for(double r = 0.0; r <= rmax; r += rmax/64){
		fprintf(fp, "%g %g %g\n", r, diff_solver(epsilon, r), r*exp(-r));
	}

	fclose(fp);
	gsl_multiroot_fsolver_free(solver);
	gsl_vector_free(energy);

return 0;
}
