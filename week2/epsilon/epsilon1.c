#include<stdio.h>
#include<limits.h>
#include<float.h>



int main(){

/*Part1*/
	printf("---------- Part 1 ----------\n\n");	
	int i = 1;
	
/*Part i*/
	printf("Part i\n\n");
	while(i+1>i) {i++;} printf("My max while int = %i\n", i);
	for(int i=1; i<i+1;) {i++;} printf("My max for int = %i\n", i);
	do{printf("My max do while int = %i\n", i);} while(i+1>i);
	printf("Max limit integer = %i\n\n", INT_MAX);

/*Part ii*/
	printf("Part ii\n\n");
	while(i-1<i) {i++;} printf("My min while int = %i\n", i);
	for(int i=1; i-1<i;) {i++;} printf("My min for int = %i\n", i);
	do{printf("My min do while int = %i\n", i);} while(i-1<i);
	printf("Min limit integer = %i\n\n", INT_MIN);

/*Part iii*/
	
	printf("Part iii\n\n");
	float x = 1; 
	while(1+x!=1){x/=2;} x*=2; /* != not equal to*/ 
	printf("w-float epsilon = %f\n", x);
	for(x = 1; 1+x!=1; x/=2) {} x*=2;
	printf("f-float epsilon = %f\n", x);
	do{x/=2;} while(1+x!=1); x*=2;
	printf("dw-float epsilon = %f\n\n", x);

	double y = 1;
	while(1+y!=1){y/=2;} y*=2; /* /= x equal to x divided by two */
	printf("w-double epsilon = %lg\n", y);
	for(y = 1; 1+y!=1; y/=2) {} y*=2;
	printf("f-double epsilon = %lg\n", y);
	do{y/=2;} while(1+y!=1); y*=2;
	printf("dw-double epsilon = %lg\n\n", y);

	long double z = 1L;
	while(1 + z!=1){z/=2;} z*=2; /* *= x is equal to x multiplied by two*/
	printf("w-long double epsilon = %Lg\n", z);
	for(z = 1; 1+z!=1; z/=2) {} z*=2;
	printf("f-long double epsilon = %Lg\n", z);
	do{z/=2;} while(1+z!=1); z*=2;
       	printf("dw-long double epsilon = %Lg\n\n", z);	

	printf("Value of float epsilon = %f\n", FLT_EPSILON);
	printf("Value of double epsilon = %lg\n", DBL_EPSILON);
	printf("Value of long double epsilon = %Lg\n", LDBL_EPSILON);


return 0;
}
