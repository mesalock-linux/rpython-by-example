src = $(wildcard *_rpy.py)
obj = $(src:.py=)

RPYFLAGS = -O0

all: $(obj)

%: %.py
	$(RPY) $(RPYFLAGS) $^

clean:
	@rm -f *-c
	@rm -rf __pycache__
