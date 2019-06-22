CFLAGS = -Wall -std=gnu99 -O 
LDLIBS = -lm  #gc is garbage collector
CC = gcc #Work with gcc - for errors: run clang
C = bar


out.txt: epsilon1 epsilon2 epsilon3
	./epsilon1 > $@
	./epsilon2 >> $@
	./epsilon3 >> $@


.PHONEY:clean
clean: 
	$(RM) *.o out*
	find -type f -executable -delete

