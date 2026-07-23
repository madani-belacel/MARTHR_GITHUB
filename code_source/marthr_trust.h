#ifndef MARTHR_TRUST_H
#define MARTHR_TRUST_H

typedef struct {
  unsigned int node_id;
  float trust_score;
  unsigned int failures;
  unsigned int successes;
  unsigned int last_seen;
} marthr_trust_entry_t;

typedef struct {
  marthr_trust_entry_t entries[64];
  unsigned int count;
} marthr_trust_table_t;

void marthr_trust_table_init(marthr_trust_table_t *table);
void marthr_trust_update_success(marthr_trust_table_t *table, unsigned int node_id, float link_quality);
void marthr_trust_update_failure(marthr_trust_table_t *table, unsigned int node_id);
void marthr_trust_decay(marthr_trust_table_t *table, unsigned int node_id, float decay_amount);
float marthr_trust_get(marthr_trust_table_t *table, unsigned int node_id);

#endif
