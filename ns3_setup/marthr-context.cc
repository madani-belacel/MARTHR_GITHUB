#include "marthr-context.h"

#include "ns3/log.h"
#include "ns3/type-id.h"

NS_LOG_COMPONENT_DEFINE("MarthrContext");
NS_OBJECT_ENSURE_REGISTERED(MarthrContext);

namespace ns3 {

TypeId MarthrContext::GetTypeId() {
  static TypeId tid = TypeId("ns3::MarthrContext")
                          .SetParent<Object>()
                          .SetGroupName("Routing")
                          .AddConstructor<MarthrContext>();
  return tid;
}

MarthrContext::MarthrContext()
    : m_baseTrustWeight(0.35f),
      m_baseEnergyWeight(0.33f),
      m_baseQosWeight(0.32f) {}

MarthrContext::~MarthrContext() {}

void MarthrContext::AdaptWeights(SafetyLevel safety, ThreatLevel threat,
                                 EnergyState energy, float &alpha, float &beta,
                                 float &gamma) {
  alpha = m_baseTrustWeight;
  beta = m_baseEnergyWeight;
  gamma = m_baseQosWeight;

  // Safety-driven adjustments
  switch (safety) {
    case SAFETY_CRITICAL:
      alpha += 0.25f;
      break;
    case SAFETY_HIGH:
      alpha += 0.10f;
      break;
    case SAFETY_NORMAL:
      break;
    case SAFETY_BEST_EFFORT:
      alpha -= 0.05f;
      break;
  }

  // Threat-driven adjustments
  switch (threat) {
    case THREAT_HIGH:
      alpha += 0.05f;
      gamma += 0.03f;
      break;
    case THREAT_NORMAL:
      break;
    case THREAT_LOW:
      beta += 0.04f;
      break;
  }

  // Energy-driven adjustments
  switch (energy) {
    case ENERGY_CRITICAL:
      beta += 0.08f;
      alpha -= 0.03f;
      break;
    case ENERGY_NORMAL:
      break;
    case ENERGY_SUFFICIENT:
      beta -= 0.03f;
      gamma += 0.02f;
      break;
  }

  // Renormalize to sum to 1.0
  float sum = alpha + beta + gamma;
  if (sum > 0.0f) {
    alpha /= sum;
    beta /= sum;
    gamma /= sum;
  }
}

}  // namespace ns3
