all: out.txt plot_fit.svg

out.txt: main.py main_fit.py
	python3 $< > $@
	python3 main_fit.py >> $@

plot_fit.svg: plot_fit.gpi out.txt
	gnuplot plot_fit.gpi

clean: 
	$(RM) -r __pycache__ *.txt fitting_params.dat *.svg
