#ifndef MARTHR_CONTEXT_H
#define MARTHR_CONTEXT_H

typedef enum {
  MARTHR_SAFETY_CRITICAL = 0,
  MARTHR_SAFETY_HIGH = 1,
  MARTHR_SAFETY_NORMAL = 2,
  MARTHR_SAFETY_BEST_EFFORT = 3
} marthr_safety_level_t;

typedef enum {
  MARTHR_THREAT_HIGH = 0,
  MARTHR_THREAT_NORMAL = 1,
  MARTHR_THREAT_LOW = 2
} marthr_threat_level_t;

typedef enum {
  MARTHR_ENERGY_CRITICAL = 0,
  MARTHR_ENERGY_NORMAL = 1,
  MARTHR_ENERGY_SUFFICIENT = 2
} marthr_energy_state_t;

typedef struct {
  marthr_safety_level_t safety_level;
  marthr_threat_level_t threat_level;
  marthr_energy_state_t energy_state;
} marthr_context_t;

void marthr_context_init(marthr_context_t *ctx);
void marthr_context_set_safety_level(marthr_context_t *ctx, marthr_safety_level_t level);
void marthr_context_set_threat_level(marthr_context_t *ctx, marthr_threat_level_t level);
void marthr_context_set_energy_state(marthr_context_t *ctx, marthr_energy_state_t state);
void marthr_context_weights(const marthr_context_t *ctx, float *alpha, float *beta, float *gamma);

#endif
