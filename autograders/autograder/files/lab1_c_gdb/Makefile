CC=gcc
CFLAGS=-D TEST


test_eccentric: test_eccentric.c
	$(CC) $(CFLAGS) -o $@ $?

test_ll_equal: test_ll_equal.c
	$(CC) $(CFLAGS) -o $@ $?

test_ll_cycle: test_ll_cycle.c
	$(CC) $(CFLAGS) -o $@ $?

.PHONY: clean

clean:
	$(RM) test_eccentric test_ll_equal test_ll_cycle
