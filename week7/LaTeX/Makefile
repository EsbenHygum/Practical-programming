CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

All: out_err.txt plot_err.pdf Error_function.pdf 

Error_function.pdf: main.bbl main.tex plot_err.pdf
	pdflatex main.tex
	pdflatex main.tex

main.bbl: main
	biber main

main: bibliography.bib
	pdflatex main.tex

plot_err.pdf: plot_err.gpi out_err.txt
	gnuplot plot_err.gpi

out_err.txt: main_err
	./$< -3 3 0.1 > $@


main_err: main_err.c


.PHONEY: clean

clean: 
	$(RM) main.bcf main.blg main.bbl main.run.xml *.pdf *.txt main_err *.aux *.log *.eps
