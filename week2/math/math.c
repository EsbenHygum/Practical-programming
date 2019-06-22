#include "stdio.h"
#include "math.h"
#include "complex.h"

int main(void){
	printf("Part 1:\n\n");
	printf("Gamma(5) = %f\n", tgamma(5));
	printf("j1(0.5) = %f\n", j1(0.5));
			
	printf("sqrt(-2) = %f + %.2fi\n", creal(csqrt(-2)), cimag(csqrt(-2)));
	printf("exp(i) = %f + %.2fi\n", creal(cexp(I)), cimag(cexp(I)));
	printf("exp(i*pi) = %f + %.2fi\n", creal(cexp(I*M_PI)), cimag(cexp(I*M_PI)));
	printf("i^e = %f + %.2fi\n", creal(cpow(I,M_E)), cimag(cpow(I,M_E)));

	return 0;


}
