#include<stdio.h>
#include<limits.h>
#include<float.h>

int main(){
/*Part2*/
	printf("\n--------Part 2--------\n\n");
	int max = INT_MAX/3;
	float sum_up = 0.0f;
	for(int i = 1; i < max; i++)
		sum_up = sum_up + 1.0/i;
	printf("Part i\n Sum up float = %f\n", sum_up);

	float sum_down = 0.0f;
	for(int i = 1; i < max; i++)
		sum_down = sum_down + 1.0/(max - i);
	printf("Sum down float = %f\n\n", sum_down);
	

	printf("Part ii\nThe difference stems from the size of the first added value. When summing up (starting with 1.0 and adding smaller and smaller fractions) the size of the numbers will eventually be too small for the sum to change value. When summing down, we start with the lowest possible value and add larger and larger fractions. Hence, the added fractions will be large enough to make a difference at this precision.\n");

	printf("\nPart iii\n");

	double sum_up_d = 0.0;
	for(int i = 1; i < max; i++)
		sum_up_d = sum_up_d + 1.0/i;
	printf("\nPart iv\nSum up double = %g\n", sum_up_d);

	double sum_down_d = 0.0;
	for(int i = 1; i < max; i++)
		sum_down_d = sum_down_d + 1.0/(max - i);
	printf("Sum down double = %g\n", sum_down_d);

	printf("When using double the sums are equal. Here it does not matter whether we are summing up or down since the precision is double that of a float.");

return 0;
}
