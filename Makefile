all: ./file-server/file-server ./rest-server/rest-server ./web-server/web-server

%: %.cc
	g++ -std=c++11 $< -o $@

%: %.c
	gcc $< -o $@
