#include <stddef.h>

#include "marthr_context.h"

static void set_weights_for_context(const marthr_context_t *ctx, float *alpha, float *beta, float *gamma) {
  switch (ctx->safety_level) {
    case MARTHR_SAFETY_CRITICAL:
      *alpha = 0.60f;
      *beta = 0.20f;
      *gamma = 0.20f;
      break;
    case MARTHR_SAFETY_HIGH:
      *alpha = 0.45f;
      *beta = 0.30f;
      *gamma = 0.25f;
      break;
    case MARTHR_SAFETY_NORMAL:
      *alpha = 0.35f;
      *beta = 0.40f;
      *gamma = 0.25f;
      break;
    default:
      *alpha = 0.30f;
      *beta = 0.50f;
      *gamma = 0.20f;
      break;
  }

  if (ctx->threat_level == MARTHR_THREAT_HIGH) {
    *alpha += 0.05f;
    *gamma += 0.03f;
  } else if (ctx->threat_level == MARTHR_THREAT_LOW) {
    *beta += 0.04f;
  }

  if (ctx->energy_state == MARTHR_ENERGY_CRITICAL) {
    *beta += 0.08f;
    *alpha -= 0.03f;
  } else if (ctx->energy_state == MARTHR_ENERGY_SUFFICIENT) {
    *beta -= 0.03f;
    *gamma += 0.02f;
  }

  if (*alpha + *beta + *gamma > 1.0f + 1e-5f) {
    float sum = *alpha + *beta + *gamma;
    *alpha /= sum;
    *beta /= sum;
    *gamma /= sum;
  }
}

void marthr_context_init(marthr_context_t *ctx) {
  if (ctx == NULL) {
    return;
  }
  ctx->safety_level = MARTHR_SAFETY_NORMAL;
  ctx->threat_level = MARTHR_THREAT_NORMAL;
  ctx->energy_state = MARTHR_ENERGY_NORMAL;
}

void marthr_context_set_safety_level(marthr_context_t *ctx, marthr_safety_level_t level) {
  if (ctx != NULL) {
    ctx->safety_level = level;
  }
}

void marthr_context_set_threat_level(marthr_context_t *ctx, marthr_threat_level_t level) {
  if (ctx != NULL) {
    ctx->threat_level = level;
  }
}

void marthr_context_set_energy_state(marthr_context_t *ctx, marthr_energy_state_t state) {
  if (ctx != NULL) {
    ctx->energy_state = state;
  }
}

void marthr_context_weights(const marthr_context_t *ctx, float *alpha, float *beta, float *gamma) {
  if (ctx == NULL || alpha == NULL || beta == NULL || gamma == NULL) {
    return;
  }
  set_weights_for_context(ctx, alpha, beta, gamma);
}
