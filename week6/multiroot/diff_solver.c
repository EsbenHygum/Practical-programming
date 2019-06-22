#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_odeiv2.h>


int diff_func(double r, const double y[], double f[], void * params){

	double epsilon = *(double *)params;
	f[0] = y[1];
	f[1] = -2*(epsilon + (1/r)) * y[0];

	return GSL_SUCCESS;
}	


int diff_solver(double epsilon, double r){
		
	int dim = 2;

	assert(r >= 0.0);			
	const double rmin = 1e-5;
	if (r < rmin) return r-r*r;

	gsl_odeiv2_system sys = {diff_func, NULL, dim, &epsilon};
	gsl_odeiv2_driver *driver;
	
	double hstart = 1e-4, abs = 1e-7, eps = 1e-7;
	driver = gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd, hstart, abs, eps);


	double r0 = rmin, y[2] = {r0-r0*r0, 1-2*r0}; 	
	int status = gsl_odeiv2_driver_apply (driver, &r0, r, y);
	if(status != GSL_SUCCESS) printf("Differential solver went wrong: %d\n", status);	
	
	gsl_odeiv2_driver_free(driver);

	return y[0];
}
