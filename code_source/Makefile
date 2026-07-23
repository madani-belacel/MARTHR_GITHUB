CC ?= gcc
CFLAGS ?= -std=c99 -Wall -Wextra
LDFLAGS ?= -no-pie

all: tests/test_marthr_core tests/test_marthr_rank tests/test_marthr_ablation tests/test_marthr_ocp

tests/test_marthr_core: tests/test_marthr_core.c marthr_context.c marthr_score.c marthr_trust.c marthr_metric_log.c
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

tests/test_marthr_rank: tests/test_marthr_rank.c marthr_context.c marthr_score.c marthr_trust.c marthr_metric_log.c marthr_rank.c
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

tests/test_marthr_ablation: tests/test_marthr_ablation.c marthr_context.c marthr_score.c marthr_trust.c marthr_rank.c
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

tests/test_marthr_ocp: tests/test_marthr_ocp.c marthr_context.c marthr_ocp.c
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

clean:
	rm -f tests/test_marthr_core tests/test_marthr_rank tests/test_marthr_ablation tests/test_marthr_ocp

.PHONY: all clean
