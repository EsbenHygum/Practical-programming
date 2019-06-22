CFLAGS = -Wall -pthread
LDLIBS = -lm -pthread

all: out.txt
	cat $<

N = 1e6
out.txt: main
	time --append --portability --output $@ ./$< $N > $@

.PHONEY: clean

clean:
	$(RM) main out.txt

