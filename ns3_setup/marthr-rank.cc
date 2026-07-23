#include "marthr-rank.h"

#include "ns3/log.h"

NS_LOG_COMPONENT_DEFINE("MarthrRank");
NS_OBJECT_ENSURE_REGISTERED(MarthrRank);

namespace ns3 {

TypeId MarthrRank::GetTypeId() {
  static TypeId tid = TypeId("ns3::MarthrRank")
                          .SetParent<Object>()
                          .SetGroupName("Routing")
                          .AddConstructor<MarthrRank>();
  return tid;
}

MarthrRank::MarthrRank() {}

MarthrRank::~MarthrRank() {}

float MarthrRank::Clamp(float value) {
  if (value < 0.0f) return 0.0f;
  if (value > 1.0f) return 1.0f;
  return value;
}

float MarthrRank::ComputeRank(float mcs) {
  // MCS [0.0, 1.0] is directly used as rank
  return Clamp(mcs);
}

float MarthrRank::ApplyHysteresis(float candidate_rank, float current_rank,
                                  float hysteresis) {
  float difference = candidate_rank - current_rank;

  // Accept candidate if difference is significant in either direction
  if (difference >= hysteresis) {
    return candidate_rank;
  }
  if (difference <= -hysteresis) {
    return candidate_rank;
  }

  // Stay with current rank (within hysteresis band)
  return current_rank;
}

bool MarthrRank::IsBetter(float rank_a, float rank_b) {
  return rank_a > rank_b;
}

}  // namespace ns3
