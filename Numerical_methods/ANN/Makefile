all: out.txt plot_a.svg plot_b.svg

plot_a.svg: plot_a.gpi out.txt
	gnuplot $<


plot_b.svg: plot_b.gpi out.txt
	gnuplot $<


out.txt: main.py ann.py
	python3 $<



clean:
	$(RM) -r __pycache__ *.txt *.svg
