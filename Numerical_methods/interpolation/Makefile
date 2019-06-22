CFLAGS = -Wall

plots: plot_lin.svg plot_quad.svg


plot_lin.svg: out_lin.txt plot_lin.gpi
	gnuplot plot_lin.gpi


plot_quad.svg: main_quad.py out_quad.txt plot_quad.gpi
	gnuplot plot_quad.gpi


out_lin.txt: main_lin.py
	python3 $< > $@


out_quad.txt: main_quad.py
	python3 $< > $@


clean:
	$(RM) *.txt *.svg
