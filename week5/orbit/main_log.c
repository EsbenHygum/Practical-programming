#include <stdio.h>
#include <gsl/gsl_odeiv2.h>
#include <gsl/gsl_errno.h>

int ode_solver(double x, const double y[], double dydx[], void * params)
{
	dydx[0] = y[0] * (1 - y[0]);
	return GSL_SUCCESS;
}
	


int main(){
	
	gsl_odeiv2_system sys;
	sys.function = ode_solver;
	sys.jacobian = NULL;
	sys.dimension = 1;
	sys.params = NULL;

	gsl_odeiv2_driver *driver;
	double hstart = 0.01, abs = 1e-6, eps = 1e-6;
	driver = gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd, hstart, abs, eps);
	
	double x0 = 0;
	double y0 = 0.5;
	double y[1] = { y0 };
	
	for(double x = 0; x <= 3; x += 0.01){

		gsl_odeiv2_driver_apply (driver, &x0, x, y);
		printf("%g %g\n", x, y[0]);
	
	}
		gsl_odeiv2_driver_free(driver);
	
return 0;
}
