all:main
all:libhandletensor.so

main:main.c handletensor.c indexing.c
	make libsome.a
	$(CC) $^ -o $@ -L./ -lsome

libhandletensor.so : handletensor.c indexing.c
	make libsome.a
	$(CC) -shared $^ -o $@ -L./ -lsome

libsome.o: somecalc.c
	$(CC) -c $^ -o $@

libsome.a: libsome.o
	ar r $@ $^


clean:
	rm -f main
	rm -f *.so
	rm -f *.o
	rm -f *a