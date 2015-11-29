

doit:
	g++ TrackBuilder.cpp -std=c++11 -shared -fPIC -I cairo-include -L . -l cairo -o libdoit.so

all: doit


clean:
	rm libdoit.so hello.png
