#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <gsl/gsl_odeiv2.h>
#include <gsl/gsl_errno.h>

int function(double x, const double y[], double dydx[], void * params){

	dydx[0] = 1/(2*y[0]);
	return GSL_SUCCESS;

}


double sqr(double x){
	assert(x>=0);
	if(x==0) return 0;
	if(x<1)return 1/sqr(1/x);
	if(x>4)return 2*sqr(x/4);

	int dim = 1;

	gsl_odeiv2_system sys;
	sys.function = function;
	sys.jacobian = NULL;
	sys.dimension = dim;
	sys.params = NULL;

	gsl_odeiv2_driver *driver;
	double hstart = 0.01, abs = 1e-10, eps = 1e-10;
	driver = gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd, hstart, abs, eps);


	double x0 = 1.0;
	double y0 = 1.0;
	double y[1] = { y0 };

	int status = gsl_odeiv2_driver_apply(driver, &x0, x, y);

	if (status != GSL_SUCCESS){
		printf("Error! Return value is %d\n", status);
		return NAN;
	}
	gsl_odeiv2_driver_free(driver);
	return y[0];
}

int main(){
	for(double x=0;x<25;x+=0.2){
		printf("%g %g %g\n",x,sqr(x),sqrt(x));
	}
}
