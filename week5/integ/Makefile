CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)


all: out_part1.txt out_qm.txt plot.svg 

out_part1.txt: main_part1
	./$< > $@


out_qm.txt: main_qm
	./$< > $@


main_part1: main_part1.o


main_qm: main_qm.o


plot.svg: plot.gpi
	gnuplot $<

.PHONEY: clean
clean:
	$(RM) *.o *.txt main_part1 main_qm *.svg

