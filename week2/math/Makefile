CFLAGS = -Wall -std=gnu99
LDLIBS = -lm



out.txt: math math2
	./math > $@
	./math2 >> $@

math: math.o 
math2: math2.o


.PHONEY: clean
clean: 
	$(RM) math math2 *.o *.txt
