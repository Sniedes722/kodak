all: ./web-server/web-server ./rest-server/rest-server

%: %.cc
	g++ -std=c++11 $< -o $@

%: %.c
	gcc $< -o $@
