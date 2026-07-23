#include "marthr_rank.h"
#include "marthr_score.h"

float marthr_compute_ocp_rank(float trust, float energy, float qos, int hop_count, const marthr_context_t *ctx) {
  float mcs = marthr_compute_score(trust, energy, qos, ctx);
  /* Invert MCS: higher MCS gives lower (better) rank, matching RPL convention */
  float inverted_mcs = 1.0f - mcs;
  /* Add hop penalty: more hops = higher (worse) rank */
  float hop_penalty = hop_count * 0.1f;
  float rank = inverted_mcs + hop_penalty;
  /* Clamp to [0, 1] */
  if (rank < 0.0f) rank = 0.0f;
  if (rank > 1.0f) rank = 1.0f;
  return rank;
}

float marthr_rank_with_hysteresis(float candidate_rank, float current_rank, float hysteresis) {
  if (candidate_rank < 0.0f) {
    candidate_rank = 0.0f;
  }
  if (candidate_rank > 1.0f) {
    candidate_rank = 1.0f;
  }

  if (current_rank < 0.0f) {
    return candidate_rank;
  }

  float difference = candidate_rank - current_rank;
  if (difference >= hysteresis) {
    return candidate_rank;
  }
  if (difference <= -hysteresis) {
    return candidate_rank;
  }

  return current_rank;
}

bool marthr_rank_is_better(float rank_a, float rank_b) {
  return rank_a < rank_b;
}
