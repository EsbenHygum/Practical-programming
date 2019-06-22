CFLAGS = -Wall -std=gnu99
LDLIBS = -lm

all: io.out.txt cmd.out.txt plot.svg

io.out.txt: main_stdio data.txt
	cat data.txt | ./$< > $@

cmd.out.txt: main_cmdline data.txt
	./$< `cat data.txt` > $@

plot.svg: plot.gpi io.out.txt cmd.out.txt
	gnuplot plot.gpi

data.txt:
	seq 0 0.1 8 | cat > $@

main_stdio: main_stdio.o 

main_cmdline: main_cmdline.o

.PHONEY: clean
clean: 
	$(RM) main-stdio main-cmdline *.o *.txt *.svg


