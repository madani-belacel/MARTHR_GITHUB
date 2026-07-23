#include <unistd.h>
#include <string.h>

#include "../marthr_context.h"
#include "../marthr_score.h"
#include "../marthr_trust.h"
#include "../marthr_metric_log.h"

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

  float alpha = 0.0f;
  float beta = 0.0f;
  float gamma = 0.0f;
  marthr_context_weights(&ctx, &alpha, &beta, &gamma);

  if (!check(alpha > 0.5f, "critical safety should increase trust weight") ||
      !check(beta > 0.2f, "energy weight should be non-trivial") ||
      !check(gamma > 0.1f, "qos weight should be non-trivial")) {
    return 1;
  }

  marthr_trust_table_t table;
  marthr_trust_table_init(&table);
  marthr_trust_update_success(&table, 1, 0.9f);
  marthr_trust_update_success(&table, 1, 0.8f);
  marthr_trust_update_failure(&table, 1);

  float trust = marthr_trust_get(&table, 1);
  if (!check(trust >= 0.0f && trust <= 1.0f, "trust score should stay in range")) {
    return 1;
  }

  float score = marthr_compute_score(trust, 0.8f, 0.7f, &ctx);
  if (!check(score >= 0.0f && score <= 1.0f, "score should stay in range")) {
    return 1;
  }

  marthr_metric_entry_t metric = {1, 2, 0.42f, trust, 0.8f, 0.7f, score};
  FILE *out = fopen("/dev/null", "w");
  if (out != NULL) {
    marthr_metric_log(&metric, out);
    fclose(out);
  }

  printf("marthr_core_tests: PASS\n");
  return 0;
}
