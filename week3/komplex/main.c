#include "komplex.h"
#include <stdio.h>
#include <stdlib.h>

int main(){
	komplex a = {1, 2}, b = {3, 4};
	printf("Testing komplex_add:\n");
	komplex add = komplex_add(a, b);
	komplex Add = {4, 6};
	komplex_print("a=", a);
	komplex_print("b=", b);

	printf("\n\nTesting the komplex add function:\n"),
	komplex_print("a+b should be equal to", Add);
	komplex_print("a+b is actually equal to", add);
	
	komplex sub = komplex_sub(a, b);
	komplex Sub = {-2, -2};
	printf("\n\nTesting complex subtraction function:\n");
	komplex_print("a-b should be equal to", Sub);
	komplex_print("a-b is actually equal to", sub);

	printf("\n\nTesting complex new and set functions:\n");
	double c = 5, d = 3, e = 2, f = 7;
	komplex z = komplex_new(c, d);
	komplex_print("Our complex new function gives us", z);
	komplex_set(&z, e, f);
	komplex_print("while our complex set function changes it to", z);

return 0;
}
