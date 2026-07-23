#ifndef MARTHR_ROUTING_HELPER_H
#define MARTHR_ROUTING_HELPER_H

#include "ns3/object-factory.h"
#include "ns3/ipv4-routing-helper.h"
#include "marthr-routing-protocol.h"

namespace ns3 {

class MarthrRoutingHelper : public Ipv4RoutingHelper {
 public:
  MarthrRoutingHelper();
  MarthrRoutingHelper* Copy() const override;
  Ptr<Ipv4RoutingProtocol> Create(Ptr<Node> node) const override;
  void Set(std::string name, const AttributeValue& value);

 private:
  ObjectFactory m_factory;
};

}  // namespace ns3

#endif  // MARTHR_ROUTING_HELPER_H
