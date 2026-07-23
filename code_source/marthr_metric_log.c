#include "marthr_metric_log.h"

void marthr_metric_log(const marthr_metric_entry_t *entry, FILE *out) {
  if (entry == NULL || out == NULL) {
    return;
  }

  fprintf(out,
          "node=%u parent=%u rank=%.4f trust=%.4f energy=%.4f qos_latency=%.4f mcs=%.4f\n",
          entry->node_id,
          entry->parent_id,
          entry->rank,
          entry->trust,
          entry->energy,
          entry->qos_latency,
          entry->mcs_score);
}
