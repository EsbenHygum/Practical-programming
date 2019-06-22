#include <stdio.h>
#include <stdlib.h>
#include <gsl/gsl_sf_airy.h>

int main(int argc, char *argv[]){

	for(int i = 1; i < argc; i++){
		double x = atof(argv[i]);
		double ai = gsl_sf_airy_Ai(x, GSL_PREC_DOUBLE);
		double bi = gsl_sf_airy_Bi(x, GSL_PREC_DOUBLE);
		printf("%g \t %g \t %g\n", x, ai, bi);
	}	
	
return 0;
}
