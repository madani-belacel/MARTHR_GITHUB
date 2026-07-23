# Audit MARTHR — Rapport ultra-détaillé (vérification indépendante)

**Date :** 2026-07-23
**Auditeur :** Claude (vérification directe des fichiers du dépôt public `madani-belacel/MARTHR_GITHUB`)
**Portée :** analyse basée uniquement sur les fichiers que j'ai pu récupérer et lire intégralement. Voir section 0 pour les limites d'accès.

---

## 0. Limites d'accès — à lire en premier

Mon outil de récupération web ne peut ouvrir que des URL déjà rencontrées via une recherche ou un fetch précédent — les liens internes profonds du dépôt (fichiers dans `code_source/`, `scripts/reproduce_project.py`, `manuscript/tables/*.tex`, `data/estimated/*.csv`) ne sont donc **pas accessibles** depuis mon environnement actuel, et la recherche web ne les indexe pas.

**Fichiers effectivement lus en entier :**
- `README.md`
- `manuscript/main.tex` (texte complet)
- `manuscript/bib/references.bib` (35 entrées)
- `scripts/marthr_simulator.py` (code complet)
- `anomalies/opencode.md` (audit interne précédent, 2026-07-23)
- `data/raw/marthr_sample.csv` (1440 lignes, intégral)

**Fichiers NON vérifiés par moi (nécessitent un upload direct pour analyse) :**
- `code_source/*.c/.h` (marthr_ocp.c, marthr_rank.c, marthr_trust.c, marthr_context.c, marthr_score.c, marthr_metric_log.c)
- `code_source/tests/*.c`
- `scripts/reproduce_project.py`, `scripts/run_simulation_campaign.py`, `scripts/regenerate_tables.py`, `scripts/generate_sample_dataset.py`, `scripts/generate_ieee_figures.py`, etc.
- `manuscript/tables/results_table.tex`, `manuscript/tables/ablation_table.tex`
- `data/estimated/*.csv` (summary_stats.csv, table2_ablation.csv, table3_summary.csv)
- Toutes les figures elles-mêmes (rendu visuel)

Pour une analyse *réellement* complète du code C, du pipeline et des tableaux, le plus fiable est que tu uploades ces fichiers directement dans la conversation (zip du repo, ou fichiers un par un) — je pourrai alors les lire dans mon environnement sandbox sans restriction et faire des vérifications ligne à ligne, y compris exécuter les scripts Python.

Ce qui suit est donc une analyse **ultra-détaillée de ce qui est vérifiable aujourd'hui**, avec deux découvertes critiques nouvelles.

---

## 1. Cohérence formelle manuscrit ↔ code Python — vérifiée ligne par ligne

J'ai comparé chaque formule du manuscrit à l'implémentation Python correspondante.

### 1.1 Poids contextuels (Section III-B du manuscrit vs `MarthrContext.adapt_weights()`)

| Dimension | Manuscrit | Code Python | Statut |
|---|---|---|---|
| Safety CRITICAL | (0.60, 0.20, 0.20) | `alpha, beta, gamma = 0.60, 0.20, 0.20` | ✅ identique |
| Safety HIGH | (0.45, 0.30, 0.25) | `0.45, 0.30, 0.25` | ✅ identique |
| Safety NORMAL | (0.35, 0.40, 0.25) | `0.35, 0.40, 0.25` | ✅ identique |
| Safety BEST_EFFORT | (0.30, 0.50, 0.20) | `0.30, 0.50, 0.20` (branche `else`) | ✅ identique |
| Threat HIGH | (+0.05, 0, +0.03) | `alpha += 0.05; gamma += 0.03` | ✅ identique |
| Threat LOW | (0, +0.04, 0) | `beta += 0.04` | ✅ identique |
| Threat NORMAL | aucun ajustement | aucune branche | ✅ identique |
| Energy CRITICAL | (−0.03, +0.08, 0) | `beta += 0.08; alpha -= 0.03` | ✅ identique |
| Energy SUFFICIENT | (0, −0.03, +0.02) | `beta -= 0.03; gamma += 0.02` | ✅ identique |
| Energy NORMAL | aucun ajustement | aucune branche | ✅ identique |
| Renormalisation | « si la somme dépasse 1 » | `if total > 1.0 + 1e-5: normalize` | ✅ identique (ne gère que le cas > 1, comme annoncé) |

**Conclusion 1.1 :** Le simulateur Python implémente exactement ce que décrit le manuscrit. Aucune divergence trouvée ici — contrairement à l'anomalie M1 précédente (qui concernait `marthr_ocp.c`, un fichier que je n'ai pas pu lire).

### 1.2 Modèle de confiance (Eq. 2-4 du manuscrit vs `MarthrTrustTable`)

- Succès : manuscrit `T_new = clamp(0.7·T_old + 0.3·L_q)` vs code `entry['trust_score'] * 0.7 + link_quality * 0.3` → ✅ identique
- Échec : manuscrit `T_new = clamp(T_old − 0.15)` vs code `trust_score - 0.15` → ✅ identique
- Décroissance : manuscrit `γ_d = 0.002` vs code `trust_table.decay(other_id, 0.002)` → ✅ identique

### 1.3 Rang et hystérésis (Eq. 5-6)

- Rang : manuscrit `(1−MCS) + 0.1·hop_count` vs code `inverted_mcs + hop_count * 0.1` → ✅ identique
- **Vérifié empiriquement sur les données réelles** (pas seulement sur le code) : ligne `seed=0, lossless, node=2 : mcs=0.6875, rank=0.4125`. Calcul : `(1−0.6875)+0.1×1 = 0.4125`. Exact. Testé sur plusieurs dizaines de lignes du CSV, toujours exact.
- Hystérésis : manuscrit `θ_h = 0.05` vs code `hysteresis=0.05` → ✅ identique

**Conclusion générale section 1 :** la partie Python du projet est honnête et cohérente avec le manuscrit. C'est un point positif fort — ce n'est pas le cas généralement observé dans les projets où les résultats sont fabriqués after-the-fact.

---

## 2. 🔴 NOUVELLE ANOMALIE CRITIQUE — `qos_latency` n'est pas une mesure de QoS

Dans `marthr_simulator.py`, deux choses distinctes existent :

1. `compute_qos(link_quality, distance, hop_count)` — une vraie fonction qui calcule le QoS à partir de la qualité de lien, du nombre de sauts et de la distance. **Cette fonction n'est jamais loggée dans le CSV final.**
2. `log_metrics()` écrit :
   ```python
   'qos_latency': round(1.0 - self.last_mcs, 4) if self.last_mcs > 0 else 1.0
   ```
   C'est-à-dire : `qos_latency = 1 − MCS`. Une simple transformation arithmétique du score composite, pas une mesure indépendante.

**Preuve empirique** (CSV) : pour chaque ligne, `qos_latency = round(1 - mcs, 4)` exactement — vérifié sur l'échantillon complet.

**Pourquoi c'est grave pour la publication :** Le manuscrit consacre une sous-section entière (« Latency and QoS », Figure 4, `fig4_latency_comparison.pdf`) à présenter cette colonne comme une observation de latence réseau. En réalité, comme `MCS = α·trust + β·energy + γ·qos`, la colonne `qos_latency` est **mécaniquement corrélée** avec le trust et l'énergie par construction — ce n'est pas une variable indépendante mesurée, c'est du bruit dérivé. Toute conclusion tirée de cette figure (« MARTHR maintains competitive latency behavior ») n'est pas soutenue par une vraie mesure de latence.

**Action de correction concrète :**
- Soit remplacer la colonne par la vraie sortie de `compute_qos()` (déjà écrite mais jamais loggée — il suffit d'ajouter `qos = self.compute_qos(...)` au retour de `update_parent()` et de le stocker sur le nœud pour le logger),
- Soit renommer honnêtement la colonne et la figure (« MCS complement », pas « latency/QoS ») et retirer les affirmations de mesure QoS indépendante.

---

## 3. 🔴 NOUVELLE ANOMALIE CRITIQUE — Les statistiques de l'abstract semblent être une seule ligne brute, pas une moyenne

L'abstract du manuscrit affirme :
> *"mean trust 0.4593, mean residual energy 0.5327, mean MCS 0.6321, and mean normalized latency 0.3679"*

J'ai recherché ces valeurs exactes dans `data/raw/marthr_sample.csv` (1440 lignes). Résultat troublant :

- La ligne `seed=0, scenario=lossless, node_id=9, parent=10` contient : `rank=0.4679, trust=0.5078, energy=0.0, qos_latency=0.3679, mcs=0.6321`.

**`mcs=0.6321` et `qos_latency=0.3679` correspondent EXACTEMENT, chiffre pour chiffre, aux « mean MCS » et « mean normalized latency » de l'abstract** — alors que ce sont des valeurs individuelles d'une seule ligne (un seul nœud, un seul seed, un seul scénario), pas une moyenne sur les 1440 observations.

C'est extrêmement improbable comme coïncidence sur 4 décimales. Deux hypothèses, à vérifier en urgence :
1. Le script qui calcule les « means » de l'abstract (probablement dans `scripts/statistics/` ou `regenerate_tables.py` — que je n'ai pas pu lire) agrège sur un sous-ensemble erroné (ex. une seule ligne, un seul nœud, ou un bug d'indexation qui sélectionne un enregistrement au lieu de faire `.mean()`).
2. Coïncidence pure — peu plausible vu la précision à 4 décimales sur deux valeurs simultanément.

**Recommandation :** avant toute soumission, il faut recalculer manuellement (`pandas.read_csv(...).mean()`) les 4 statistiques de l'abstract à partir de `data/raw/marthr_sample.csv` (ou du fichier `data/estimated/summary_stats.csv` s'il agrège correctement) et vérifier qu'elles correspondent à une vraie moyenne sur l'ensemble des scénarios/seeds, pas à un artefact d'un seul enregistrement. C'est le genre d'erreur qui, si elle se confirme, remettrait en cause la fiabilité de **tous** les chiffres du papier, pas seulement ceux de l'abstract.

---

## 4. Bibliographie — vérification élargie

- **35 entrées** dans `references.bib`, mais seulement ~21 sont réellement citées (`\cite{}`) dans `main.tex`. Entrées jamais citées : `clausen2003optimized`, `gnaneswaran2012mrhof`, `chang2004maximum`, `hu2002ariadne`, `marti2000mitigating`, `hanzo2007qos`, `de2003high`, `karp2000gpsr`, `heinzelman2000energy`, `li2001qos`, `liu2004trust`, `djenouri2012energy`, `baccelli2013study`, `gelenbe1993routing`, `zeng2012energy`, `mohseni2016review`. À nettoyer ou à citer réellement.
- **Échantillon vérifié réel** : `yuan2026fuzzy` (arXiv:2606.26124, « Enhancing FANET Routing Resilience... ») — titre et auteurs confirmés via recherche web, correspondance exacte.
- Aucun DOI sur les entrées `@article{...arxiv...}` — normal pour des preprints arXiv, mais en contradiction avec l'exigence du checklist interne (« chaque référence a un DOI valide »). À assouplir cette règle ou remplacer par les versions publiées si elles existent.
- L'auto-référence `marthr2026` signalée dans l'audit précédent (M3/B1) n'apparaît plus dans le fichier que j'ai récupéré — cohérent avec la correction annoncée.

---

## 5. Contradiction abstract / corps du texte (déjà signalée, confirmée)

Abstract : *"outperforming MRHOF in trust-aware and energy-aware scenarios."*
Corps du texte (Section Résultats) : *"The values are descriptive simulator measurements and should not be interpreted as a comparison against MRHOF."*

Ces deux phrases se contredisent directement. Combinée avec la découverte de la section 3 (statistiques d'abstract potentiellement mal calculées), je recommande de **réécrire entièrement l'abstract** pour qu'il reflète le même degré de prudence que le corps du texte, une fois les vraies moyennes recalculées.

---

## 6. Ce que je ne peux confirmer ni infirmer (accès manquant)

- Le statut réel de `marthr_ocp.c` (l'anomalie M1 est-elle vraiment corrigée dans le C, ou seulement dans le Python que j'ai vérifié ?)
- La cohérence `MAX_ENTRIES` C vs Python (anomalie C1 de l'audit interne)
- Le contenu de `data/estimated/summary_stats.csv`, `table2_ablation.csv`, `table3_summary.csv` — notamment l'anomalie D2 (écarts-types identiques suspects entre `lossless` et `lossy`)
- Si `scripts/reproduce_project.py` s'exécute réellement sans erreur
- Le contenu réel des `tables/results_table.tex` et `tables/ablation_table.tex` (correspondent-ils aux CSV ?)
- Les valeurs MRHOF « suspectes » mentionnées en fin de l'audit interne (rank 0.96, MCS 0.04)

---

## 7. Évaluation globale mise à jour

**Points positifs confirmés :**
- Le simulateur Python est honnête et cohérent avec le manuscrit sur toutes les formules vérifiables.
- La bibliographie contient majoritairement des références réelles.
- Le manuscrit est généralement rédigé avec prudence (hedging systématique).
- Les 20 seeds annoncés sont bien réels et vérifiables dans le CSV.

**Points bloquants nouveaux à corriger avant toute soumission :**
1. **Critique** — Recalculer et vérifier les statistiques de l'abstract (section 3) : risque de moyenne mal calculée sur tout le papier.
2. **Critique** — Corriger ou renommer honnêtement `qos_latency` (section 2) : la figure de latence actuelle ne mesure pas ce qu'elle prétend mesurer.
3. **Haute** — Résoudre la contradiction abstract/corps sur la comparaison MRHOF (section 5).
4. **Moyenne** — Nettoyer la bibliographie (entrées non citées).

**Recommandation finale :** uploade-moi les fichiers `code_source/*.c`, `scripts/reproduce_project.py`, `scripts/regenerate_tables.py` (ou équivalent), et `data/estimated/*.csv` pour que je puisse compléter l'audit avec les mêmes standards de preuve (vérification empirique, pas seulement lecture).
