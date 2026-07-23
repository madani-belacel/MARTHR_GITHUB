#ifndef MARTHR_SCORE_H
#define MARTHR_SCORE_H

#include "ns3/object.h"
#include "marthr-context.h"

namespace ns3 {

/**
 * Multi-criteria score computation.
 * Computes MCS = alpha * trust + beta * energy + gamma * qos
 */
class MarthrScore : public Object {
 public:
  static TypeId GetTypeId();
  MarthrScore();
  ~MarthrScore();

  /**
   * Compute multi-criteria score.
   * @param trust Trust value [0.0, 1.0]
   * @param energy Residual energy [0.0, 1.0]
   * @param qos QoS metric (latency/throughput) [0.0, 1.0]
   * @param context Context for weight adaptation
   * @return Normalized MCS [0.0, 1.0]
   */
  float ComputeScore(float trust, float energy, float qos,
                     Ptr<MarthrContext> context,
                     MarthrContext::SafetyLevel safety,
                     MarthrContext::ThreatLevel threat,
                     MarthrContext::EnergyState energy_state);

 private:
  float Clamp(float value);
};

}  // namespace ns3

#endif  // MARTHR_SCORE_H
