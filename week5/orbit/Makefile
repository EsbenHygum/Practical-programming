CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: out_log.txt plot_log.svg plot_orbit.svg


out_log.txt: main_log
	./$< > $@

main_log: main_log.o


main_orbit: main_orbit.o


plot_log.svg: plot_log.gpi
	gnuplot plot_log.gpi


plot_orbit.svg: plot_orbit.gpi main_orbit
	./main_orbit
	gnuplot plot_orbit.gpi

.PHONEY: clean

clean:
	$(RM) *.o out*.txt main_log main_orbit *.svg 
