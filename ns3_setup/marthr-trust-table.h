#ifndef MARTHR_TRUST_TABLE_H
#define MARTHR_TRUST_TABLE_H

#include "ns3/object.h"
#include "ns3/ipv6-address.h"

namespace ns3 {

/**
 * Trust table entry for a single neighbor node.
 */
struct MarthrTrustEntry {
  Ipv6Address node_address;
  float trust_score;
  uint32_t successes;
  uint32_t failures;
  Time last_seen;
};

/**
 * Trust table management with reputation tracking and decay.
 */
class MarthrTrustTable : public Object {
 public:
  static TypeId GetTypeId();
  MarthrTrustTable();
  ~MarthrTrustTable();

  /**
   * Initialize empty trust table.
   */
  void Initialize();

  /**
   * Update trust on successful transmission.
   * @param address Node address
   * @param link_quality Quality of the successful transmission [0.0, 1.0]
   */
  void UpdateSuccess(Ipv6Address address, float link_quality);

  /**
   * Update trust on failed transmission.
   * @param address Node address
   */
  void UpdateFailure(Ipv6Address address);

  /**
   * Get current trust value for node.
   * @param address Node address
   * @return Trust score [0.0, 1.0]
   */
  float Get(Ipv6Address address);

  /**
   * Apply trust decay to a node.
   * @param address Node address
   * @param decay_amount Amount to decay [0.0, 1.0]
   */
  void Decay(Ipv6Address address, float decay_amount);

  /**
   * Get number of entries in trust table.
   */
  uint32_t GetSize();

 private:
  static const uint32_t MAX_ENTRIES = 64;  // Max neighbors to track
  MarthrTrustEntry m_entries[MAX_ENTRIES];
  uint32_t m_count;

  MarthrTrustEntry *FindEntry(Ipv6Address address);
  MarthrTrustEntry *CreateEntry(Ipv6Address address);
  float Clamp(float value);
};

}  // namespace ns3

#endif  // MARTHR_TRUST_TABLE_H
