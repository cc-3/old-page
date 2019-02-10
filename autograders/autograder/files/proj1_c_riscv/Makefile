SOURCES := utils.c part1.c part2.c riscv.c
HEADERS := types.h utils.h riscv.h

riscv: $(SOURCES) $(HEADERS)
	gcc -g -Wall -O2 -o $@ $(SOURCES)

.PHONY: clean

clean:
	rm -f riscv output.json
	rm -rf riscvcode/out
