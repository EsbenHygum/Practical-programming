all: out.txt conv_plot.svg
	cat $<


conv_plot.svg: conv_plot.gpi convergence.txt
	gnuplot conv_plot.gpi

out.txt: main.py mc.py
	python3 $< > $@


clean:
	$(RM) out.txt convergence.txt conv_plot.svg
	rm -rf __pycache__
