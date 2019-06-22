CFLAGS = -Wall -std=gnu99
LDLIBS = -lm

.PHONEY: clean out.txt


out.txt: main
	./$< > $@

main: main.o komplex.o

main.o komplex.o: komplex.h


clean: 
	$(RM) main main.o komplex.o out.txt
