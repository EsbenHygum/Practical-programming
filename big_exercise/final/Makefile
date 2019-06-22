CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: diff_out.txt plot.svg

plot.svg: plot.gpi
	gnuplot plot.gpi

diff_out.txt: main
	./$< > $@

main: main.o


.PHONEY: clean


clean:
	$(RM) *.txt *.svg main *.o
