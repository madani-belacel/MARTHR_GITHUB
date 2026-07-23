#include <stddef.h>

#include "marthr_score.h"

float marthr_compute_score(float trust, float energy, float qos, const marthr_context_t *ctx) {
  if (ctx == NULL) {
    return 0.0f;
  }

  float alpha = 0.0f;
  float beta = 0.0f;
  float gamma = 0.0f;
  marthr_context_weights(ctx, &alpha, &beta, &gamma);

  float score = alpha * trust + beta * energy + gamma * qos;
  if (score < 0.0f) {
    return 0.0f;
  }
  if (score > 1.0f) {
    return 1.0f;
  }
  return score;
}
