#ifndef MARTHR_CONTEXT_H
#define MARTHR_CONTEXT_H

#include "ns3/object.h"

namespace ns3 {

/**
 * Context-aware weight adaptation for MARTHR routing.
 * Adapts weights (alpha, beta, gamma) based on safety level, threat level, and energy state.
 */
class MarthrContext : public Object {
 public:
  static TypeId GetTypeId();
  MarthrContext();
  ~MarthrContext();

  enum SafetyLevel {
    SAFETY_CRITICAL = 0,
    SAFETY_HIGH = 1,
    SAFETY_NORMAL = 2,
    SAFETY_BEST_EFFORT = 3
  };

  enum ThreatLevel {
    THREAT_HIGH = 0,
    THREAT_NORMAL = 1,
    THREAT_LOW = 2
  };

  enum EnergyState {
    ENERGY_CRITICAL = 0,
    ENERGY_NORMAL = 1,
    ENERGY_SUFFICIENT = 2
  };

  /**
   * Adapt weights based on current context.
   * @param safety Safety level
   * @param threat Threat level  
   * @param energy Energy state
   * @param alpha Output: trust weight (initially 0.35)
   * @param beta Output: energy weight (initially 0.33)
   * @param gamma Output: QoS weight (initially 0.32)
   */
  void AdaptWeights(SafetyLevel safety, ThreatLevel threat, EnergyState energy,
                    float &alpha, float &beta, float &gamma);

 private:
  float m_baseTrustWeight;
  float m_baseEnergyWeight;
  float m_baseQosWeight;
};

}  // namespace ns3

#endif  // MARTHR_CONTEXT_H
