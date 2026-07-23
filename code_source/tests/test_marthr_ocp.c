#include <unistd.h>
#include <string.h>

#include "../marthr_context.h"
#include "../marthr_ocp.h"

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
  marthr_ocp_metric_t metric;
  marthr_ocp_init(&metric);

  /* Test 1: default context (NORMAL/NORMAL/NORMAL) */
  float score = marthr_ocp_score(&metric);
  float rank = marthr_ocp_rank(&metric);
  if (!check(score >= 0.0f && score <= 1.0f, "default score out of [0,1]") ||
      !check(rank >= 0.0f && rank <= 1.0f, "default rank out of [0,1]")) {
    return 1;
  }

  /* Test 2: CRITICAL safety, HIGH threat, CRITICAL energy */
  metric.context.safety_level = MARTHR_SAFETY_CRITICAL;
  metric.context.threat_level = MARTHR_THREAT_HIGH;
  metric.context.energy_state = MARTHR_ENERGY_CRITICAL;
  score = marthr_ocp_score(&metric);
  rank = marthr_ocp_rank(&metric);
  if (!check(score >= 0.0f && score <= 1.0f, "critical score out of [0,1]") ||
      !check(rank >= 0.0f && rank <= 1.0f, "critical rank out of [0,1]") ||
      !check(score > 0.5f, "critical safety should increase trust weight")) {
    return 1;
  }

  /* Test 3: all-zero inputs (minimum) */
  metric.trust = 0.0f;
  metric.energy = 0.0f;
  metric.qos = 0.0f;
  metric.rank = 0.0f;
  marthr_context_init(&metric.context);
  score = marthr_ocp_score(&metric);
  rank = marthr_ocp_rank(&metric);
  if (!check(score >= 0.0f && score <= 1.0f, "zero score out of [0,1]") ||
      !check(rank >= 0.0f && rank <= 1.0f, "zero rank out of [0,1]")) {
    return 1;
  }

  /* Test 4: all-one inputs (maximum) */
  metric.trust = 1.0f;
  metric.energy = 1.0f;
  metric.qos = 1.0f;
  metric.rank = 1.0f;
  score = marthr_ocp_score(&metric);
  rank = marthr_ocp_rank(&metric);
  if (!check(score >= 0.0f && score <= 1.0f, "one score out of [0,1]") ||
      !check(rank >= 0.0f && rank <= 1.0f, "one rank out of [0,1]")) {
    return 1;
  }

  /* Test 5: higher MCS should produce lower (better) rank */
  metric.trust = 0.9f;
  metric.energy = 0.9f;
  metric.qos = 0.9f;
  metric.rank = 0.0f;
  marthr_context_init(&metric.context);
  float high_mcs_rank = marthr_ocp_rank(&metric);

  metric.trust = 0.1f;
  metric.energy = 0.1f;
  metric.qos = 0.1f;
  float low_mcs_rank = marthr_ocp_rank(&metric);
  if (!check(high_mcs_rank < low_mcs_rank,
             "higher MCS should produce lower rank")) {
    return 1;
  }

  /* Test 6: NULL safety */
  score = marthr_ocp_score(NULL);
  rank = marthr_ocp_rank(NULL);
  if (!check(score == 0.0f, "NULL score should return 0") ||
      !check(rank == 0.0f, "NULL rank should return 0")) {
    return 1;
  }

  write(STDOUT_FILENO, "marthr_ocp_tests: PASS\n", 23);
  return 0;
}
