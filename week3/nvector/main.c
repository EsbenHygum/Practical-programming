#include "nvector.h"
#include <stdio.h>
#include <stdlib.h>
#define RND (double)rand()/RAND_MAX

int main(){

	printf("Testing vector allocation:\n");
	int n = 5;
	nvector *v = nvector_alloc(n);
	if (v == NULL) printf("My chosen dimension is %i. The function allocates the memory for a %d-dimensional vector. The function has failed\n\n", n, (*v).size);
	else printf("My chosen dimension is %i. The function allocates memory for a %d-dimensional vector. The function has passed.\n\n", n, (*v).size);
	
	printf("Testing nvector_set and nvector_get:\n");
	int i = 4;
	double value = RND;
	nvector_set(v, i, value);
	double v_i = nvector_get(v, i);
	if (v_i == value) printf("My chosen value for the i'th index is %g. The i'th value of my vector is %g. The functions have passed.\n\n", value, v_i);
	else printf("My chosen value for the i'th index is %g. The i'th value of my vector is %g. The functions have failed.\n\n", value, v_i);

	printf("Testing nvector_dot_product:\n");
	double my_result = 0.0;
	nvector *u = nvector_alloc(n);
	for(int i = 0; i < n; i++)
	{
		double x = RND;
		double y = RND;
		nvector_set(v, i, x);
		nvector_set(u, i, y);
		my_result += nvector_get(u, i) * nvector_get(v, i);
	}
	double function_result = nvector_dot_product(u, v, n);
	
	if(my_result == function_result) printf("My result is %g, while the function prints %g. The function has passed.\n\n", my_result, function_result);
	else printf("My result is %g, while the function prints %g. The function has not passed.\n\n", my_result, function_result);
	

	printf("Testing nvector_free:\n");
	printf("The size of the vector before is %d, ", (*v).size);
	nvector_free(v);
if((*v).size < 1) printf("the size after freeing is %d. The function has passed.\n\n", (*v).size);
	else printf("the size after freeing is %d. The function has not passed.\n\n", (*v).size);	

return 0;
}


