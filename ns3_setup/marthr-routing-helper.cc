#include "marthr-routing-helper.h"

#include "ns3/ipv4-routing-protocol.h"
#include "ns3/log.h"

namespace ns3 {

MarthrRoutingHelper::MarthrRoutingHelper() {
  m_factory.SetTypeId("ns3::MarthrRoutingProtocol");
}

MarthrRoutingHelper* MarthrRoutingHelper::Copy() const {
  return new MarthrRoutingHelper(*this);
}

Ptr<Ipv4RoutingProtocol> MarthrRoutingHelper::Create(Ptr<Node> node) const {
  Ptr<MarthrRoutingProtocol> protocol = m_factory.Create<MarthrRoutingProtocol>();
  return protocol;
}

void MarthrRoutingHelper::Set(std::string name, const AttributeValue& value) {
  m_factory.Set(name, value);
}

}  // namespace ns3
