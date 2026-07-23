#ifndef MARTHR_OCP_H
#define MARTHR_OCP_H

#include "marthr_context.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
  float trust;
  float energy;
  float qos;
  float rank;
  marthr_context_t context;
} marthr_ocp_metric_t;

void marthr_ocp_init(marthr_ocp_metric_t *metric);
float marthr_ocp_score(const marthr_ocp_metric_t *metric);
float marthr_ocp_rank(const marthr_ocp_metric_t *metric);

#ifdef __cplusplus
}
#endif

#endif
