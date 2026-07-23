#include "marthr-score.h"

#include "ns3/log.h"

NS_LOG_COMPONENT_DEFINE("MarthrScore");
NS_OBJECT_ENSURE_REGISTERED(MarthrScore);

namespace ns3 {

TypeId MarthrScore::GetTypeId() {
  static TypeId tid = TypeId("ns3::MarthrScore")
                          .SetParent<Object>()
                          .SetGroupName("Routing")
                          .AddConstructor<MarthrScore>();
  return tid;
}

MarthrScore::MarthrScore() {}

MarthrScore::~MarthrScore() {}

float MarthrScore::Clamp(float value) {
  if (value < 0.0f) return 0.0f;
  if (value > 1.0f) return 1.0f;
  return value;
}

float MarthrScore::ComputeScore(float trust, float energy, float qos,
                                Ptr<MarthrContext> context,
                                MarthrContext::SafetyLevel safety,
                                MarthrContext::ThreatLevel threat,
                                MarthrContext::EnergyState energy_state) {
  float alpha, beta, gamma;

  // Get adapted weights from context
  context->AdaptWeights(safety, threat, energy_state, alpha, beta, gamma);

  // Compute MCS
  float mcs =
      alpha * Clamp(trust) + beta * Clamp(energy) + gamma * Clamp(qos);

  return Clamp(mcs);
}

}  // namespace ns3
