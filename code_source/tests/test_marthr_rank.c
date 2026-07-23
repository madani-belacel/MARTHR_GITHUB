#include <string.h>
#include <unistd.h>

#include "../marthr_context.h"
#include "../marthr_rank.h"
#include "../marthr_trust.h"

static int check(int condition, const char *message) {
  if (!condition) {
    const char *prefix = "FAIL: ";
    write(STDERR_FILENO, prefix, strlen(prefix));
    write(STDERR_FILENO, message, strlen(message));
    write(STDERR_FILENO, "\n", 1);
    return 0;
  }
  return 1;
}

int main(void) {
  marthr_context_t ctx;
  marthr_context_init(&ctx);
  marthr_context_set_safety_level(&ctx, MARTHR_SAFETY_CRITICAL);
  marthr_context_set_threat_level(&ctx, MARTHR_THREAT_HIGH);
  marthr_context_set_energy_state(&ctx, MARTHR_ENERGY_CRITICAL);

  float rank1 = marthr_compute_ocp_rank(0.8f, 0.6f, 0.7f, 2, &ctx);
  float rank2 = marthr_compute_ocp_rank(0.4f, 0.9f, 0.2f, 2, &ctx);
  if (!check(rank1 < rank2, "rank1 should be better (lower) than rank2 for critical safety")) {
    return 1;
  }

  float next_rank = marthr_rank_with_hysteresis(0.47f, 0.42f, 0.05f);
  if (!check(next_rank == 0.47f, "hysteresis should update current rank when difference equals threshold")) {
    return 1;
  }

  next_rank = marthr_rank_with_hysteresis(0.43f, 0.42f, 0.05f);
  if (!check(next_rank == 0.42f, "hysteresis should preserve current rank when candidate is not sufficiently better")) {
    return 1;
  }

  marthr_trust_table_t table;
  marthr_trust_table_init(&table);
  marthr_trust_update_success(&table, 1, 0.9f);
  marthr_trust_update_failure(&table, 1);
  marthr_trust_decay(&table, 1, 0.1f);
  float trust = marthr_trust_get(&table, 1);
  if (!check(trust >= 0.0f && trust <= 1.0f, "trust score should stay in range after decay")) {
    return 1;
  }

  const char *success = "marthr_rank_tests: PASS\n";
  write(STDOUT_FILENO, success, strlen(success));
  return 0;
}
