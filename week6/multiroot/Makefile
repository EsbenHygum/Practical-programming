CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)


all: out_rosen.txt out_shoot.txt plot.svg


out_rosen.txt: main_rosen
	./$< > $@

main_rosen: main_rosen.o


out_shoot.txt: main_shoot
	./$< > $@

main_shoot: main_shoot.c diff_solver.c


plot.svg: plot.gpi main_shoot
	gnuplot plot.gpi

.PHONEY: clean

clean: 
	$(RM) *.svg *.o *.txt main_rosen main_shoot 
