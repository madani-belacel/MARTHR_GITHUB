#include <stddef.h>

#include "marthr_ocp.h"
#include "marthr_score.h"
#include "marthr_context.h"

void marthr_ocp_init(marthr_ocp_metric_t *metric) {
  if (metric == NULL) {
    return;
  }
  metric->trust = 0.8f;
  metric->energy = 0.7f;
  metric->qos = 0.9f;
  metric->rank = 0.0f;
  marthr_context_init(&metric->context);
}

float marthr_ocp_score(const marthr_ocp_metric_t *metric) {
  if (metric == NULL) {
    return 0.0f;
  }
  float alpha, beta, gamma;
  marthr_context_weights(&metric->context, &alpha, &beta, &gamma);
  return alpha * metric->trust + beta * metric->energy + gamma * metric->qos;
}

float marthr_ocp_rank(const marthr_ocp_metric_t *metric) {
  if (metric == NULL) {
    return 0.0f;
  }
  float score = marthr_ocp_score(metric);
  /* Invert MCS: higher MCS gives lower (better) rank, matching RPL convention */
  float inverted_mcs = 1.0f - score;
  /* Add hop penalty: more hops = higher (worse) rank */
  float hop_penalty = metric->rank * 0.1f;
  float rank = inverted_mcs + hop_penalty;
  /* Clamp to [0, 1] */
  if (rank < 0.0f) rank = 0.0f;
  if (rank > 1.0f) rank = 1.0f;
  return rank;
}
