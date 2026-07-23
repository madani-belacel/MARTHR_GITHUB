#include "marthr-trust-table.h"

#include "ns3/log.h"
#include "ns3/simulator.h"

NS_LOG_COMPONENT_DEFINE("MarthrTrustTable");
NS_OBJECT_ENSURE_REGISTERED(MarthrTrustTable);

namespace ns3 {

TypeId MarthrTrustTable::GetTypeId() {
  static TypeId tid =
      TypeId("ns3::MarthrTrustTable")
          .SetParent<Object>()
          .SetGroupName("Routing")
          .AddConstructor<MarthrTrustTable>();
  return tid;
}

MarthrTrustTable::MarthrTrustTable() : m_count(0) {
  for (uint32_t i = 0; i < MAX_ENTRIES; ++i) {
    m_entries[i].trust_score = 0.5f;  // Default: neutral
    m_entries[i].successes = 0;
    m_entries[i].failures = 0;
    m_entries[i].last_seen = Seconds(0.0);
  }
}

MarthrTrustTable::~MarthrTrustTable() {}

void MarthrTrustTable::Initialize() {
  m_count = 0;
  for (uint32_t i = 0; i < MAX_ENTRIES; ++i) {
    m_entries[i].trust_score = 0.5f;
    m_entries[i].successes = 0;
    m_entries[i].failures = 0;
  }
}

MarthrTrustEntry *MarthrTrustTable::FindEntry(Ipv6Address address) {
  for (uint32_t i = 0; i < m_count; ++i) {
    if (m_entries[i].node_address == address) {
      return &m_entries[i];
    }
  }
  return nullptr;
}

MarthrTrustEntry *MarthrTrustTable::CreateEntry(Ipv6Address address) {
  if (m_count >= MAX_ENTRIES) {
    // Table full - remove least recently used
    uint32_t oldest_idx = 0;
    Time oldest_time = m_entries[0].last_seen;
    for (uint32_t i = 1; i < m_count; ++i) {
      if (m_entries[i].last_seen < oldest_time) {
        oldest_time = m_entries[i].last_seen;
        oldest_idx = i;
      }
    }
    m_entries[oldest_idx].node_address = address;
    m_entries[oldest_idx].trust_score = 0.5f;
    m_entries[oldest_idx].successes = 0;
    m_entries[oldest_idx].failures = 0;
    m_entries[oldest_idx].last_seen = Simulator::Now();
    return &m_entries[oldest_idx];
  }
  m_entries[m_count].node_address = address;
  m_entries[m_count].trust_score = 0.5f;
  m_entries[m_count].successes = 0;
  m_entries[m_count].failures = 0;
  m_entries[m_count].last_seen = Simulator::Now();
  return &m_entries[m_count++];
}

float MarthrTrustTable::Clamp(float value) {
  if (value < 0.0f) return 0.0f;
  if (value > 1.0f) return 1.0f;
  return value;
}

void MarthrTrustTable::UpdateSuccess(Ipv6Address address,
                                      float link_quality) {
  MarthrTrustEntry *entry = FindEntry(address);
  if (!entry) {
    entry = CreateEntry(address);
  }
  entry->last_seen = Simulator::Now();
  entry->successes++;
  // Update: 70% of previous + 30% of new quality
  entry->trust_score =
      Clamp(entry->trust_score * 0.7f + link_quality * 0.3f);
}

void MarthrTrustTable::UpdateFailure(Ipv6Address address) {
  MarthrTrustEntry *entry = FindEntry(address);
  if (!entry) {
    entry = CreateEntry(address);
  }
  entry->last_seen = Simulator::Now();
  entry->failures++;
  // Penalty: reduce by 15%
  entry->trust_score = Clamp(entry->trust_score - 0.15f);
}

float MarthrTrustTable::Get(Ipv6Address address) {
  MarthrTrustEntry *entry = FindEntry(address);
  if (!entry) {
    return 0.5f;  // Unknown node: neutral trust
  }
  return entry->trust_score;
}

void MarthrTrustTable::Decay(Ipv6Address address, float decay_amount) {
  MarthrTrustEntry *entry = FindEntry(address);
  if (!entry) {
    return;  // No entry to decay
  }
  entry->trust_score = Clamp(entry->trust_score - decay_amount);
}

uint32_t MarthrTrustTable::GetSize() { return m_count; }

}  // namespace ns3
