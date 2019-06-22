all: out_ls.txt out_cov.txt plot_ls.svg plot_cov.svg

out_ls.txt: main.py least_square.py qr_decomp.py
	python3 $< > $@

out_cov.txt: main_cov.py least_square.py
	python3 $< > $@

plot_ls.svg: plot_ls.gpi data.txt out_ls.txt
	gnuplot $<

plot_cov.svg: plot_cov.gpi out_cov.txt
	gnuplot $<

clean:
	$(RM) data_exp_cov.txt data_exp.txt out_cov.txt out_ls.txt *.svg
	$(RM) -r __pycache__
