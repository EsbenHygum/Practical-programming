CFLAGS = -Wall -std=gnu99
LDLIBS = -lm

.PHONEY: out.txt clean

out.txt: main
	./$< > $@

main: main.o nvector.o

main.o nvector.o: nvector.h

clean:
	$(RM) main main.o nvector.o out.txt


