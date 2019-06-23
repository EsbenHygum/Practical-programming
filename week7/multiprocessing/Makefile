CFLAGS = -Wall -pthread
LDLIBS = -lm -pthread

#q := $(shell seq 10 1 19)
#N := $(shell for i in $q; do \echo "e($$i)"|bc -l; done)
powers := $(shell seq 13 1 25)
N := $(shell for i in $(powers); do echo "2^($$i)"|bc -l; done)
c = 1000

all: out.txt out_pi.txt conv_plot.svg


out.txt: main main_openmp
	./$< $$c > $@
	./main_openmp $$c >> $@

out_pi.txt: main
	cat /dev/null > $@
	for n in $N; do echo $$n; ./$< $$n >> $@; done
	
conv_plot.svg: conv_plot.gpi out_pi.txt
	gnuplot $<

main_openmp: main_openmp.c
	gcc -o main_openmp -fopenmp $@

.PHONEY: clean

clean:
	$(RM) main out.txt out_time.txt conv_plot.svg

