#include "marthr-routing-protocol.h"

#include "ns3/ipv4-l3-protocol.h"
#include "ns3/log.h"
#include "ns3/string.h"
#include "ns3/uinteger.h"

namespace ns3 {

NS_LOG_COMPONENT_DEFINE("MarthrRoutingProtocol");
NS_OBJECT_ENSURE_REGISTERED(MarthrRoutingProtocol);

TypeId MarthrRoutingProtocol::GetTypeId() {
  static TypeId tid = TypeId("ns3::MarthrRoutingProtocol")
                          .SetParent<Ipv4RoutingProtocol>()
                          .SetGroupName("Routing")
                          .AddConstructor<MarthrRoutingProtocol>();
  return tid;
}

MarthrRoutingProtocol::MarthrRoutingProtocol()
    : m_ipv4(nullptr),
      m_context(CreateObject<MarthrContext>()),
      m_score(CreateObject<MarthrScore>()),
      m_trustTable(CreateObject<MarthrTrustTable>()),
      m_rank(CreateObject<MarthrRank>()),
      m_enabled(true) {}

MarthrRoutingProtocol::~MarthrRoutingProtocol() {}

void MarthrRoutingProtocol::SetIpv4(Ptr<Ipv4> ipv4) {
  m_ipv4 = ipv4;
}

Ptr<Ipv4Route> MarthrRoutingProtocol::RouteOutput(Ptr<Packet> packet,
                                                  const Ipv4Header& header,
                                                  Ptr<NetDevice> outInterface,
                                                  Socket::SocketErrno& sockerr) {
  sockerr = Socket::ERROR_NOTERROR;
  return BuildRoute(header, outInterface);
}

bool MarthrRoutingProtocol::RouteInput(Ptr<const Packet> packet,
                                       const Ipv4Header& header,
                                       Ptr<const NetDevice> idev,
                                       const UnicastForwardCallback& ucb,
                                       const MulticastForwardCallback& mcb,
                                       const LocalDeliveryCallback& lcb,
                                       const ErrorCallback& ecb) {
  UpdateMetrics(header);
  return false;
}

void MarthrRoutingProtocol::NotifyInterfaceUp(uint32_t interface) {}
void MarthrRoutingProtocol::NotifyInterfaceDown(uint32_t interface) {}
void MarthrRoutingProtocol::NotifyAddAddress(uint32_t interface,
                                              Ipv4InterfaceAddress address) {}
void MarthrRoutingProtocol::NotifyRemoveAddress(uint32_t interface,
                                                 Ipv4InterfaceAddress address) {}
void MarthrRoutingProtocol::PrintRoutingTable(Ptr<OutputStreamWrapper> stream,
                                              Time::Unit unit) const {}

Ptr<Ipv4Route> MarthrRoutingProtocol::BuildRoute(const Ipv4Header& header,
                                                 Ptr<NetDevice> outInterface) {
  Ptr<Ipv4Route> route = Create<Ipv4Route>();
  route->SetDestination(header.GetDestination());
  route->SetGateway(Ipv4Address("0.0.0.0"));
  route->SetOutputDevice(outInterface);
  return route;
}

void MarthrRoutingProtocol::UpdateMetrics(const Ipv4Header& header) {
  float trust = 0.8f;
  float energy = 0.7f;
  float qos = 0.9f;
  float score = m_score->ComputeScore(trust, energy, qos, m_context,
                                      MarthrContext::SAFETY_HIGH,
                                      MarthrContext::THREAT_NORMAL,
                                      MarthrContext::ENERGY_NORMAL);
  NS_LOG_DEBUG("MARTHR route update: dest=" << header.GetDestination() << " score=" << score);
}

}  // namespace ns3
