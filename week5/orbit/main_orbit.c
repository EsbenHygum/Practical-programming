#include <stdio.h>
#include <gsl/gsl_odeiv2.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_vector.h>

int orbit(double phi, const double u[], double dudphi[], void * params)
{
	double epsilon = *(double *) params;
	dudphi[0] = u[1];
	dudphi[1] = 1 - u[0] + epsilon * u[0] * u[0];
	return GSL_SUCCESS;
}
	
void orbit_solver(char * name, double epsilon, double u0, double uprime0){

	double phi0 = 0;
	int n = 500;

	FILE *fp = fopen(name, "w");
	gsl_odeiv2_system sys;
	sys.function = orbit;
	sys.jacobian = NULL;
	sys.dimension = 2;
	sys.params = (void *) &epsilon;

	gsl_odeiv2_driver *driver;
	double hstart = 1e-3, abs = 1e-6, eps = 1e-6;
	driver = gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd, hstart, abs, eps);
	
	
	double u[2] = { u0, uprime0 };

	for(double phi = 0; phi < n; phi +=0.1){
		gsl_odeiv2_driver_apply (driver, &phi0, phi, u);
		fprintf(fp, "%g %g\n", phi, u[0]);
	}
	
	fclose(fp);	
	gsl_odeiv2_driver_free(driver);

}


int main(){


	orbit_solver("out_part_i.txt", 0.0, 1.0, 0.0);

	orbit_solver("out_part_ii.txt", 0.0, 1.0, -0.5);

	orbit_solver("out_part_iii.txt", 0.01, 1.0, -0.5);
	
return 0;
}
