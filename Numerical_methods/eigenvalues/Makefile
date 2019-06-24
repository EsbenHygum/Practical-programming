PYTHON = python3 -00
mkfname = $(word $(word $(MAKEFILE_LIST)), $(MAKEFILE_LIST) )

all: out_cyclic.txt out_ebye.txt time_cyclic.txt time_ebye.txt plot_time.svg

out_cyclic.txt: main_cyclic.py eigen.py matrix_codes.py
	python3 $< > $@

out_ebye.txt: main_ebye.py eigen.py matrix_codes.py
	python3 $< > $@

time_cyclic.txt: main_cyclic.py eigen.py matrix_codes.py
	for n in `seq 2 1 14`; do \
		echo "n=$$n"; \
		\time --format "$$n %U" --append --output $@ python3 $< $$n > /dev/null; done

time_ebye.txt: main_ebye.py eigen.py matrix_codes.py
	for n in `seq 2 1 14`; do \
		echo "n=$$n"; \
		\time --format "$$n %U" --append --output $@ python3 $< $$n > /dev/null; done


plot_time.svg: plot_time.gpi time_cyclic.txt time_ebye.txt
	gnuplot $<

.PHONEY: clean

clean: 
	$(RM) *.txt -r __pycache__ *.svg *.log
