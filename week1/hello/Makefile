CFLAGS = -Wall -std=gnu99
LDLIBS = -lm

out.txt: hello
	./$< > $@

hello: hello.o

.PHONEY: clean

clean:
	$(RM) *.o hello *.txt
