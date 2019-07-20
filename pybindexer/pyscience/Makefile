$(eval PREFIX := $(shell python-config --prefix))
$(eval INCLUDES := $(shell python-config --includes))
$(eval LDFLAGS :=$(shell python-config --ldflags))
$(eval CFLAGS :=$(shell	python-config --cflags))
sample: sample.cpp
	g++ sample.cpp -std=c++11 \
	$(CFLAGS) \
	-I$(PREFIX)/include \
	-L$(PREFIX)/lib \
	-L$(PREFIX)/lib/python3.5/config-3.5m/ \
	-lc++ \
	$(LDFLAGS) \
	-o sample

clean:
	rm sample