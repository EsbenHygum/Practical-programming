#include <gsl/gsl_linalg.h>
#include <stdio.h>


int main(void){
	int dim = 3;
	double matrix[] = { 6.13,  -2.90,  5.86,	
			    8.08,  -6.31, -3.89,
	       		   -4.36,  1.00,   0.19 };
	double result[] = {6.23, 5.37, 2.29};

	gsl_matrix_view m = gsl_matrix_view_array (matrix, dim, dim);
	gsl_vector_view b = gsl_vector_view_array (result, dim);
	gsl_vector *x = gsl_vector_alloc(dim);

	int sig;
	gsl_permutation * perm = gsl_permutation_alloc (dim);
	
	gsl_linalg_LU_decomp (&m.matrix, perm, &sig);
	gsl_linalg_LU_solve (&m.matrix, perm, &b.vector, x);

	printf("My vector solution:\nx0 = %g\nx1 = %g\nx2 = %g\n\n", (*x).data[0], (*x).data[1], (*x).data[2]);
	printf("Testing the obtained vector:\n");

	double matrix_new[] = { 6.13,  -2.90,  5.86,	
			    8.08,  -6.31, -3.89,
	       		   -4.36,  1.00,   0.19 };

	gsl_matrix_view m2 = gsl_matrix_view_array(matrix_new, dim, dim);
	gsl_vector *res = gsl_vector_alloc(dim);

	
	for(int i = 0; i < dim; i++)
		for(int j = 0; j < dim; j++)
			(*res).data[i] += gsl_matrix_get(&m2.matrix, i, j) * (*x).data[j]; 

	printf("y0 = %g\ny1 = %g\ny2 = %g\n", (*res).data[0], (*res).data[1], (*res).data[2]);
	printf("The result should be:\ny0 = %g\ny1 = %g\ny2 = %g\n", result[0], result[1], result[2]);

	gsl_permutation_free (perm);
	gsl_vector_free (x);
	gsl_vector_free (res);

return 0;
}


