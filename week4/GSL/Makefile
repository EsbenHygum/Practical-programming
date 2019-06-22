CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: out_airy.txt out_linal.txt plot.svg

out_airy.txt: airy data.txt
	./$< `cat data.txt` > $@
	
out_linal.txt: main_linal
	./$< > $@

data.txt:
	seq -15 0.05 5 | cat > $@

main_linal: main_linal.o

airy: airy.o

plot.svg: plot.gpi out_airy.txt
	gnuplot plot.gpi


.PHONEY: clean

clean:
	$(RM) *.svg data.txt out*.txt *.o airy main_linal
