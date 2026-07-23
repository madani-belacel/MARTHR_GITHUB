#include <string.h>
#include <unistd.h>

#include "../marthr_context.h"
#include "../marthr_rank.h"
#include "../marthr_score.h"
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

  marthr_trust_table_t table;
  marthr_trust_table_init(&table);

  for (unsigned int i = 1; i <= 5; ++i) {
    marthr_trust_update_success(&table, i, 0.95f);
    marthr_trust_update_success(&table, i, 0.90f);
    marthr_trust_update_success(&table, i, 0.85f);
    marthr_trust_update_success(&table, i, 0.95f);
    marthr_trust_update_success(&table, i, 0.90f);
  }

  float trust_sum = 0.0f;
  for (unsigned int i = 1; i <= 5; ++i) {
    float t = marthr_trust_get(&table, i);
    if (!check(t >= 0.75f && t <= 1.0f, "trust score should reflect success history")) {
      return 1;
    }
    trust_sum += t;
  }

  float avg_trust = trust_sum / 5.0f;
  float trust_only_score = marthr_compute_ocp_rank(avg_trust, 0.0f, 0.0f, 1, &ctx);
  if (!check(trust_only_score > 0.0f, "trust-only variant should produce non-zero score")) {
    return 1;
  }

  float energy_only_score = marthr_compute_ocp_rank(0.0f, 0.8f, 0.0f, 1, &ctx);
  if (!check(energy_only_score > 0.0f, "energy-only variant should produce non-zero score")) {
    return 1;
  }

  float qos_only_score = marthr_compute_ocp_rank(0.0f, 0.0f, 0.7f, 1, &ctx);
  if (!check(qos_only_score > 0.0f, "qos-only variant should produce non-zero score")) {
    return 1;
  }

  float full_score = marthr_compute_ocp_rank(avg_trust, 0.8f, 0.7f, 1, &ctx);
  if (!check(full_score > 0.0f && full_score <= 1.0f, "full variant should produce normalized score")) {
    return 1;
  }

  if (!check(full_score <= trust_only_score || full_score <= energy_only_score,
             "full variant should leverage multiple factors (lower rank = better)")) {
    return 1;
  }

  const char *success = "marthr_ablation_tests: PASS\n";
  write(STDOUT_FILENO, success, strlen(success));
  return 0;
}
