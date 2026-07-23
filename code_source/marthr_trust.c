#include <stddef.h>

#include "marthr_trust.h"

static marthr_trust_entry_t *find_entry(marthr_trust_table_t *table, unsigned int node_id) {
  for (unsigned int i = 0; i < table->count; ++i) {
    if (table->entries[i].node_id == node_id) {
      return &table->entries[i];
    }
  }
  return NULL;
}

void marthr_trust_table_init(marthr_trust_table_t *table) {
  if (table == NULL) {
    return;
  }
  table->count = 0;
}

static float clamp_trust(float trust) {
  if (trust < 0.0f) {
    return 0.0f;
  }
  if (trust > 1.0f) {
    return 1.0f;
  }
  return trust;
}

static void update_entry_defaults(marthr_trust_entry_t *entry, unsigned int node_id) {
  entry->node_id = node_id;
  entry->trust_score = 0.5f;
  entry->failures = 0;
  entry->successes = 0;
  entry->last_seen = 0;
}

void marthr_trust_update_success(marthr_trust_table_t *table, unsigned int node_id, float link_quality) {
  if (table == NULL) {
    return;
  }

  marthr_trust_entry_t *entry = find_entry(table, node_id);
  if (entry == NULL) {
    if (table->count >= 64) {
      return;
    }
    entry = &table->entries[table->count++];
    update_entry_defaults(entry, node_id);
  }

  entry->successes += 1;
  entry->last_seen += 1;

  float weight = 0.3f;
  float score_from_link = clamp_trust(link_quality);
  entry->trust_score = clamp_trust(entry->trust_score * (1.0f - weight) + score_from_link * weight);
}

void marthr_trust_update_failure(marthr_trust_table_t *table, unsigned int node_id) {
  if (table == NULL) {
    return;
  }

  marthr_trust_entry_t *entry = find_entry(table, node_id);
  if (entry == NULL) {
    if (table->count >= 64) {
      return;
    }
    entry = &table->entries[table->count++];
    update_entry_defaults(entry, node_id);
  }

  entry->failures += 1;
  entry->last_seen += 1;

  float penalty = 0.15f;
  entry->trust_score = clamp_trust(entry->trust_score - penalty);
}

void marthr_trust_decay(marthr_trust_table_t *table, unsigned int node_id, float decay_amount) {
  if (table == NULL) {
    return;
  }

  marthr_trust_entry_t *entry = find_entry(table, node_id);
  if (entry == NULL) {
    return;
  }

  entry->trust_score = clamp_trust(entry->trust_score - decay_amount);
}

float marthr_trust_get(marthr_trust_table_t *table, unsigned int node_id) {
  if (table == NULL) {
    return 0.0f;
  }

  marthr_trust_entry_t *entry = find_entry(table, node_id);
  if (entry == NULL) {
    return 0.0f;
  }
  return entry->trust_score;
}
