CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: out_rosen.txt out_least_sq.txt plot_activity.svg


plot_activity.svg: plot_activity.gpi
	
	gnuplot plot_activity.gpi


out_least_sq.txt: main_ls
	./$< > $@


out_rosen.txt: main_rosen
	./$< > $@


clean:
	$(RM) *.svg *.txt main_rosen main_ls
