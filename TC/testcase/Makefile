CC = gcc

C_FILES = $(shell ls *.c)

PKGS = elementary ecore-x ecore evas x11 dlog glib-2.0 utilX

LDFLAGS += $(TET_ROOT)/lib/tet3/tcm_s.o
LDFLAGS += -L$(TET_ROOT)/lib/tet3 -ltcm_s
LDFLAGS += -L$(TET_ROOT)/lib/tet3 -lapi_s
LDFLAGS += `pkg-config --libs $(PKGS)`

CFLAGS += `pkg-config --cflags $(PKGS)`
CFLAGS += -I.
CFLAGS += -I$(TET_ROOT)/inc/tet3
CFLAGS += -Wall

#TARGETS = $(C_FILES:%.c=tc-%)
TCS := $(shell ls -1 *.c | cut -d. -f1)

all: $(TCS)

%: %.c
	$(CC) -o $@ $< $(CFLAGS) $(LDFLAGS)

clean:
	rm -f $(TCS)
