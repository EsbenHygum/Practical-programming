all: out.txt numeric_exam.pdf 

numeric_exam.pdf: numeric_exam.bbl numeric_exam.tex
	pdflatex numeric_exam.tex
	pdflatex numeric_exam.tex

numeric_exam.bbl: numeric_exam
	biber numeric_exam

numeric_exam: bibl.bib
	pdflatex numeric_exam.tex

out.txt: main.py eigen.py qr_decomp.py
	python3 $< > $@


clean:
	$(RM) out.* *.pdf *.log *.blg *.bcf *.bbl *.run.xml *.aux
	rm -rf __pycache__
