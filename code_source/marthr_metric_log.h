#ifndef MARTHR_METRIC_LOG_H
#define MARTHR_METRIC_LOG_H

#include <stdio.h>

typedef struct {
  unsigned int node_id;
  unsigned int parent_id;
  float rank;
  float trust;
  float energy;
  float qos_latency;
  float mcs_score;
} marthr_metric_entry_t;

void marthr_metric_log(const marthr_metric_entry_t *entry, FILE *out);

#endif
