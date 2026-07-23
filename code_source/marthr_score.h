#ifndef MARTHR_SCORE_H
#define MARTHR_SCORE_H

#include "marthr_context.h"
#include "marthr_trust.h"

float marthr_compute_score(float trust, float energy, float qos, const marthr_context_t *ctx);

#endif
