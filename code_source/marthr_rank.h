#ifndef MARTHR_RANK_H
#define MARTHR_RANK_H

#include <stdbool.h>
#include "marthr_context.h"

float marthr_compute_ocp_rank(float trust, float energy, float qos, int hop_count, const marthr_context_t *ctx);
float marthr_rank_with_hysteresis(float candidate_rank, float current_rank, float hysteresis);
bool marthr_rank_is_better(float rank_a, float rank_b);

#endif
