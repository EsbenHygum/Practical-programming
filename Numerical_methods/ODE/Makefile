all: run plot_orbit.svg plot_log.svg

plot_orbit.svg: plot_orbit.gpi run
	gnuplot $<

plot_log.svg: plot_log.gpi run
	gnuplot $<

run: main.py ode_solver.py
	python3 $<

clean: 
	$(RM) -r __pycache__ *.txt *.svg log_func.dat orbit.dat
