#ifndef MARTHR_ROUTING_PROTOCOL_H
#define MARTHR_ROUTING_PROTOCOL_H

#include "ns3/ipv4-routing-protocol.h"
#include "ns3/ipv4-address.h"
#include "ns3/ipv4-header.h"
#include "ns3/ipv4-route.h"
#include "ns3/net-device.h"
#include "ns3/node.h"
#include "ns3/object.h"
#include "ns3/ptr.h"
#include "ns3/socket.h"
#include "ns3/time.h"

#include "marthr-context.h"
#include "marthr-rank.h"
#include "marthr-score.h"
#include "marthr-trust-table.h"

namespace ns3 {

class MarthrRoutingProtocol : public Ipv4RoutingProtocol {
 public:
  static TypeId GetTypeId();
  MarthrRoutingProtocol();
  ~MarthrRoutingProtocol() override;

  void SetIpv4(Ptr<Ipv4> ipv4) override;
  Ptr<Ipv4Route> RouteOutput(Ptr<Packet> packet, const Ipv4Header& header,
                             Ptr<NetDevice> outInterface,
                             Socket::SocketErrno& sockerr) override;
  bool RouteInput(Ptr<const Packet> packet, const Ipv4Header& header,
                  Ptr<const NetDevice> idev,
                  const UnicastForwardCallback& ucb,
                  const MulticastForwardCallback& mcb,
                  const LocalDeliveryCallback& lcb,
                  const ErrorCallback& ecb) override;
  void NotifyInterfaceUp(uint32_t interface) override;
  void NotifyInterfaceDown(uint32_t interface) override;
  void NotifyAddAddress(uint32_t interface, Ipv4InterfaceAddress address) override;
  void NotifyRemoveAddress(uint32_t interface,
                            Ipv4InterfaceAddress address) override;
  void PrintRoutingTable(Ptr<OutputStreamWrapper> stream,
                         Time::Unit unit = Time::S) const override;

 private:
  Ptr<Ipv4> m_ipv4;
  Ptr<MarthrContext> m_context;
  Ptr<MarthrScore> m_score;
  Ptr<MarthrTrustTable> m_trustTable;
  Ptr<MarthrRank> m_rank;
  bool m_enabled;

  Ptr<Ipv4Route> BuildRoute(const Ipv4Header& header, Ptr<NetDevice> outInterface);
  void UpdateMetrics(const Ipv4Header& header);
};

}  // namespace ns3

#endif  // MARTHR_ROUTING_PROTOCOL_H
