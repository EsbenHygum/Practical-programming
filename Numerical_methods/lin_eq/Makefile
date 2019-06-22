
all: out.txt
	cat $<

out.txt: main.py qr_decomp.py matrix_codes.py
	python3 $< > $@


clean:
	$(RM) out.*
	rm -rf __pycache__
