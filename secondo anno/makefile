# Description: Makefile for the exercises and examples of the 2022
#              season of the LTNDS course.

EXES := # files to compile

DEBUG_FLAGS := -O0 -g

CXXFLAGS := $(CXXFLAGS) $(DEBUG_FLAGS)

ROOT_CFLAGS := $(shell root-config --cflags)
ROOT_LIBS := $(shell root-config --libs)

all: $(EXES)

root_% : root_%.cpp
	$(LINK.cc) -o $@ $(ROOT_CFLAGS) $@.cpp $(ROOT_LIBS)

clean:
	/bin/rm -f $(EXES); /bin/rm -f *.o
