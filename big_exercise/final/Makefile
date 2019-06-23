CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: diff_out.txt plot.pdf report.pdf

report.pdf: report.bbl report.tex plot.pdf
	pdflatex report.tex
	pdflatex report.tex

report.bbl: report
	biber report

report: bibl.bib
	pdflatex report.tex

plot.pdf: plot.gpi
	gnuplot plot.gpi

diff_out.txt: main
	./$< > $@

main: main.o


.PHONEY: clean
clean:
	$(RM) *.txt *.pdf main *.o report.blg report.log report.bcf report.run.xml rm report.bbl report.aux
