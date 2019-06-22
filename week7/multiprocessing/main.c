#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include <time.h>

struct pars {int a, b; double res;};

void* pi(void* param){
	
	struct pars* data = (struct pars*)param;
	int a = data -> a;
	int b = data -> b;
	int sum = 0;

	for(int i = a; i < b; i++){
		unsigned int alpha = time(NULL) + 105 * i;
		unsigned int beta = time(NULL) + 62 * i;
		double x = (double)rand_r(&alpha)/(double)RAND_MAX;
		double y = (double)rand_r(&beta)/(double)RAND_MAX;
		if(sqrt(x*x + y*y) < 1.0){
			sum += 1;
		}
	}

	data -> res = sum;
	return 0;
}


int main(int argc, char** argv){
	int N = argc>1? (int)atof(argv[1]):1e6;
	int mid_sq = N/2;
	struct pars data1, data2;

	data1.a = 0;
	data1.b = mid_sq;
	pthread_t thread;
	pthread_create(&thread, NULL, pi, (void*)&data1);

	data2.a = mid_sq;
	data2.b = N;
	pi((void*)&data2);

	pthread_join(thread, NULL);

	double pi = 4.0 * (data1.res + data2.res)/N;

	printf("Pi = %g\n", pi);

return 0;
}
