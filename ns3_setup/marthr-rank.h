#ifndef MARTHR_RANK_H
#define MARTHR_RANK_H

#include "ns3/object.h"

namespace ns3 {

/**
 * OCP/RPL rank computation for routing decision.
 */
class MarthrRank : public Object {
 public:
  static TypeId GetTypeId();
  MarthrRank();
  ~MarthrRank();

  /**
   * Compute routing rank from multi-criteria score.
   * @param mcs Multi-criteria score [0.0, 1.0]
   * @return Routing rank (scaled for RPL/OCP)
   */
  float ComputeRank(float mcs);

  /**
   * Apply hysteresis to avoid rank oscillation.
   * @param candidate_rank Candidate new rank
   * @param current_rank Current rank
   * @param hysteresis Hysteresis threshold
   * @return Accepted rank (current or candidate)
   */
  float ApplyHysteresis(float candidate_rank, float current_rank,
                        float hysteresis);

  /**
   * Compare two ranks.
   * @param rank_a First rank
   * @param rank_b Second rank
   * @return true if rank_a is better (higher)
   */
  bool IsBetter(float rank_a, float rank_b);

 private:
  float Clamp(float value);
};

}  // namespace ns3

#endif  // MARTHR_RANK_H
