# Audit Global MARTHR — Rapport 2026-07-23 (mise à jour)

## Résumé Exécutif

| Sévérité | Nombre |
|----------|--------|
| Critique | 10 |
| Haute | 9 |
| Moyenne | 11 |
| Basse | 4 |
| **Total** | **34** |

**Évolution par rapport au premier audit (2026-07-23 matin) :**
- **9 anomalies corrigées** (M-1, M-2, M-3, M-4, C-4, C-8, D-4, Pipeline, D-2 partielle)
- **3 anomalies partiellement corrigées** (C-9, M-6, D-8)
- **25 anomalies persistantes**
- **9 nouvelles anomalies détectées**
- **Net : 43 → 34 anomalies** (réduction de 21%)

**Score de reproductibilité : 4/10** (amélioration mineure — pipeline corrigé mais baseline MRHOF toujours buggée)

---

## Bilan des Corrections

### Anomalies corrigées ✅

| ID | Description | Audit précédent |
|----|-------------|-----------------|
| M-1 | Section "Protocol Design" dupliquée | ✅ Supprimée |
| M-2 | Abstract "outperforming MRHOF" | ✅ Reformulé neutre |
| M-3 | Références OLSR/MRHOF sans `\cite{}` | ✅ Citations ajoutées |
| M-4 | 16 entrées orphelines dans .bib | ✅ Réduit à 23 entrées, 0 orphelin |
| C-4 | Incohérence normalisation poids C vs Python | ✅ Alignés |
| C-8 | `update_failure()` pénalité ×0.8 vs -0.15 | ✅ Aligné à -0.15 |
| D-4 | `simulation_log.txt` orphelin | ✅ Supprimé |
| Pipeline | `reproduce_project.py` référait scripts inexistants | ✅ Scripts existants |
| D-2 | README "trust = 0.0" | ✅ Reformulé |

### Anomalies partiellement corrigées ⚠️

| ID | Description | Résidu |
|----|-------------|--------|
| C-9 | Trust noeud inconnu 0.0 vs 0.5 | Python/ns3 = 0.5, mais C standalone = 0.0 |
| M-6 | Titre "Ablation Study" trompeur | Caveats ajoutés dans le texte, mais **titre reste "Ablation Study"** |
| D-8 | `table3_summary.csv` MRHOF non documenté | MRHOF supprimé, mais 5/8 scénarios seulement |

---

## 1. Manuscrit

### 1.1 Anomalies critiques

| # | Ligne(s) | Description | Statut |
|---|----------|-------------|--------|
| N-M1 | 25 vs tableau | **Incohérence Energy** — abstract: 0.5149, tableau: 0.5327 (écart 3.3%) | **NOUVEAU** |
| M-7 | ablation l.12 | **MCS "w/o QoS" (0.7044) > Full MARTHR (0.6284)** — paradoxe inexpliqué | **PERSISTE** |

### 1.2 Anomalies hautes

| # | Ligne(s) | Description | Statut |
|---|----------|-------------|--------|
| N-M2 | bib L31-36 | **Citation MRHOF pointe vers OF0** — `gnaneswaran2012mrhof` décrit OF0 (draft-ietf-roll-of0), pas MRHOF (RFC 6779) | **NOUVEAU** |
| M-5 | bib | **7 références arXiv 2025–2026 non vérifiables** — sans DOI, volume, ni pages | **PERSISTE** |

### 1.3 Anomalies moyennes

| # | Ligne(s) | Description | Statut |
|---|----------|-------------|--------|
| M-6/N-M7 | 356 | **Titre "Ablation Study" contredit les caveats internes** — le texte dit "not a controlled ablation" mais le titre dit "Ablation Study" | **PERSISTE** (partiel cor.) |
| N-M3 | 411 | **"The authors" (pluriel) vs auteur unique** — "Madani Belacel" seul à la ligne 16 | **NOUVEAU** |
| N-M4 | Figures | **2 figures orphelines** — `marthr_scientific_figure.png` et `marthr_ablation_figure.png` existent mais ne sont pas référencées dans `\includegraphics` | **NOUVEAU** |
| N-M6 | 257 | **Référence à table pour MRHOF inexistant** — le texte dit "reported as 0.0 in Table..." mais la table ne contient pas MRHOF | **NOUVEAU** |

### 1.4 Anomalies basses

| # | Description | Statut |
|---|-------------|--------|
| N-M5 | 9 entrées `and others` dans .bib (auteurs tronqués) | **NOUVEAU** |

### 1.5 Points positifs

- ✅ Structure complète : Abstract → Intro → Related Work → Protocol Design → Implementation → Evaluation → Results → Discussion → Conclusion → Acknowledgments
- ✅ 14/14 figures référencées existent
- ✅ 0 entrée orpheline dans .bib
- ✅ 0 warning BibTeX
- ✅ Cohérence Trust/Latency/MCS entre abstract et tableau

---

## 2. Code Source

### 2.1 Anomalies critiques (code ns3)

| # | Fichier | Ligne(s) | Description | Statut |
|---|---------|----------|-------------|--------|
| C-1 | `ns3_setup/marthr-rank.cc` | 50 | **`IsBetter()` logique INVERSÉE** — ns3: "higher is better" vs C/Python: "lower is better" | **PERSISTE** |
| C-2 | `ns3_setup/marthr-rank.cc` | 28–31 | **`ComputeRank()` sans inversion MCS ni pénalité sauts** — retourne MCS brut | **PERSISTE** |
| C-10 | `ns3_setup/marthr-routing-protocol.cc` | 43–52 | **`RouteInput()` retourne TOUJOURS `false`** — aucun paquet routé | **PERSISTE** |

### 2.2 Anomalies hautes

| # | Fichier | Ligne(s) | Description | Statut |
|---|---------|----------|-------------|--------|
| C-3 | `ns3_setup/marthr-context.cc` | 19–22 | **Poids de contexte ns3 différents** — (0.35, 0.33, 0.32) vs C/Python (0.35, 0.40, 0.25) | **PERSISTE** |
| C-5 | `ns3_setup/marthr-routing-protocol.cc` | 73–75 | **`UpdateMetrics()` valeurs HARDCODEES** — trust=0.8, energy=0.7, qos=0.9 toujours | **PERSISTE** |
| C-7 | `ns3_setup/marthr-trust-table.h` vs `routing-protocol.h` | — | **Incohérence Ipv4 vs Ipv6** — routage IPv4, trust table IPv6 | **PERSISTE** |
| C-15 | `scripts/analyze_campaigns.py` | 58 | **`baseline_mrhof()` crash systématique** — `self.simulations_dir` inexistant | **PERSISTE** |

### 2.3 Anomalies moyennes

| # | Fichier | Description | Statut |
|---|---------|-------------|--------|
| C-6 | `ns3_setup/marthr-routing-protocol.cc` | TrustTable instancié mais jamais utilisé | **PERSISTE** |
| C-11 | ns3 headers vs C headers | Conflit de header guards identiques | **PERSISTE** |
| C-13 | `run_simulation_campaign.py:252–256` | MRHOF "attack" sans simulation d'attaque réelle | **PERSISTE** |
| N-C1 | `generate_ieee_figures.py:153` | `ax.legend()` sans label (warning matplotlib) | **NOUVEAU** |
| N-C2 | `generate_ablation_figure.py:16–27` | Fallback avec données 0.0 si colonne `variant` absente | **NOUVEAU** |

### 2.4 Anomalies basses

| # | Fichier | Description | Statut |
|---|---------|-------------|--------|
| C-12 | `marthr_ocp.c` vs `marthr_rank.c` | Duplication de fonction rank | **PERSISTE** |
| C-14 | `run_simulation_campaign.py:287` | Compteur hardcoded "8" au lieu de 11 | **PERSISTE** |

### 2.5 Tableau de cohérence MCS

| Critère | C standalone | Python (core) | Python (simulator) | ns3 |
|---------|-------------|---------------|---------------------|-----|
| Poids base (NORMAL) | 0.35/0.40/0.25 | 0.35/0.40/0.25 | N/A | **0.35/0.33/0.32** |
| Inversion MCS | ✅ (1-mcs) | ✅ | ✅ | **❌ NON** |
| Pénalité sauts | ✅ (hop×0.1) | ✅ | ✅ | **❌ NON** |
| IsBetter | lower better | lower better | lower better | **higher better** |
| Trust failure | -0.15 | -0.15 | -0.15 | -0.15 |
| Trust inconnu | 0.0 | 0.5 | 0.5 | 0.5 |
| Normalisation | si >1.0 | si >1.0 | si >1.0 | toujours |

### 2.6 Recherche de placeholders

Aucun `TODO`, `FIXME`, `TBD`, `placeholder`, `ESTIMATED` trouvé dans les fichiers `.c`, `.h`, `.py`.

---

## 3. Données & Reproductibilité

### 3.1 Anomalies critiques

| # | Description | Statut |
|---|-------------|--------|
| D-1 | **`MrhofSimulator` ne sélectionne JAMAIS de parent** — MRHOF baseline = vide (mcs=0.0, rank=1.0 partout). Cause: rank candidat ≥ 1.8 > rank initial 1.0, et MRHOF n'accepte que les ranks inférieurs | **PERSISTE** |

### 3.2 Anomalies hautes

| # | Description | Statut |
|---|-------------|--------|
| D-6 | **`summary_stats.csv` ne couvre que 3/11 scénarios** (27%) — les 8 autres sont absents | **PERSISTE** |
| D-7 | **`convergence_time` toujours = 0** — bug: initialisé à -1 mais condition vérifie == 0 (jamais vraie) | **PERSISTE + NOUVEAU BUG** |
| N-D2 | **`generate_sample_dataset.py` ne produit que 3/8 scénarios** — manque energy_stress, stress_large_grid, mobility_dynamic, qos_sensitive, mixed_attack_energy | **NOUVEAU** |

### 3.3 Anomalies moyennes

| # | Description | Statut |
|---|-------------|--------|
| D-3 | **Noms de scénarios incohérents** — CSV brut: courts (`lossless`) vs estimated: longs (`lossless_baseline`) | **PERSISTE** |
| D-5 | **`metric_summary.csv`** utilise `latency`/`mcs_score` vs `qos_latency`/`mcs` ailleurs | **PERSISTE** |
| D-8 | **`table3_summary.csv`** ne couvre que 5/8 scénarios (MRHOF supprimé) | **PARTIEL corr.** |
| N-D3 | **`table2_ablation.csv`** — labels variantes incohérents avec noms de scénarios README | **NOUVEAU** |

### 3.4 Score de reproductibilité

| Composant | Statut |
|-----------|--------|
| Simulateur MARTHR | ✅ Fonctionnel |
| Simulateur MRHOF | ❌ Buggé (jamais de parent sélectionné) |
| Pipeline `reproduce_project.py` | ✅ Scripts référencés existent |
| Documentation provenance | ⚠️ Partiellement mise à jour |
| Données CSV | ✅ Présentes et structurées |
| Figures | ⚠️ 5/16 avec données fabriquées |

---

## 4. Figures

### 4.1 Inventaire

16 figures dans `manuscript/Figures/` — 14 référencées dans `main.tex`, 2 orphelines.

### 4.2 Anomalies

| # | Sévérité | Description | Statut |
|---|----------|-------------|--------|
| F-1 | Critique | **5 figures avec données purement fabriquées** (hardcodées dans `generate_missing_figures.py`) : `marthr_dodag_trust.png`, `marthr_pareto_frontier.png`, `marthr_control_overhead.png`, `marthr_attack_detection.png`, `marthr_context_weights.png` | **PERSISTE** |
| F-2 | Critique | **`baseline_comparison.csv` manquant** — `plot_baseline_comparison.py` crashera au runtime | **PERSISTE** |
| F-3 | Haute | **`summary_stats.csv` couvre 3/11 scénarios** — figures incomplètes | **PERSISTE** |
| F-4 | Haute | **8 scénarios sans aucune visualisation** | **PERSISTE** |
| F-5 | Basse | `ax.legend()` sans label dans `figure4_latency_comparison()` | **PERSISTE** |
| F-6 | Basse | Redondance `tick_labels` dans `figure5_rank_distribution()` | **PERSISTE** |

**Aucune anomalie de figures n'a été corrigée.**

---

## 5. Bibliographie

### 5.1 Statistiques

| Métrique | Avant | Après |
|----------|-------|-------|
| Total entrées .bib | 37 | 23 |
| Entrées citées | 21 | 23 |
| Entrées orphelines | 16 | **0** |
| Références arXiv | 7 | 7 |
| Warnings BibTeX | 1 | **0** |

### 5.2 Problèmes restants

| # | Sévérité | Description |
|---|----------|-------------|
| B-1 | Haute | **7 références arXiv 2025–2026** sans DOI — impossibles à vérifier |
| B-2 | Haute | **Citation MRHOF pointe vers OF0** — `gnaneswaran2012mrhof` décrit OF0, pas MRHOF |
| B-3 | Basse | 9 entrées `and others` (auteurs tronqués) |

---

## 6. Actions de Correction Recommandées

### Priorité 1 — Critique

| # | Action | Impact |
|---|--------|--------|
| A-1 | **Corriger le code ns3** — aligner `IsBetter()`, `ComputeRank()`, poids de contexte, intégrer TrustTable et Rank dans le protocole, corriger `RouteInput()` | Le ns3 est non-fonctionnel |
| A-2 | **Corriger `MrhofSimulator`** — le clamp à [0,1] détruit l'ETX. Ajuster rank initial ou logique de sélection | Baseline MRHOF = vide |
| A-3 | **Corriger l'incohérence Energy** dans le manuscrit — abstract (0.5149) vs tableau (0.5327) | Claim erroné |
| A-4 | **Corriger la citation MRHOF** — remplacer OF0 par la vraie référence MRHOF (RFC 6779) | Mauvaise référence |
| A-5 | **Remplacer les données fabriquées** dans `generate_missing_figures.py` par des données CSV | 5 figures sans base empirique |
| A-6 | **Régénérer ou restaurer `baseline_comparison.csv`** | Script crash |

### Priorité 2 — Haute

| # | Action | Impact |
|---|--------|--------|
| A-7 | **Vérifier les 7 références arXiv** sur arXiv.org | Risque de références fabriquées |
| A-8 | **Renommer "Ablation Study"** en "Scenario-Proxied Component Analysis" | Terminologie trompeuse |
| A-9 | **Supprimer les 2 figures orphelines** ou les référencer | Code mort |
| A-10 | **Corriger `convergence_time`** — le bug -1 vs 0 empêche tout calcul | Métrique inutile |
| A-11 | **Compléter `summary_stats.csv`** avec les 8+ scénarios | Données incomplètes |
| A-12 | **Corriger `analyze_campaigns.py`** — implémenter `baseline_mrhof()` | Script inutilisable |
| A-13 | **Unifier les noms de scénarios** entre CSV, README et scripts | Traçabilité brisée |
| A-14 | **Corriger la référence à table MRHOF** dans le texte (ligne 257) | Affirmation fausse |

### Priorité 3 — Moyenne

| # | Action | Impact |
|---|--------|--------|
| A-15 | Corriger "The authors" → "The author" dans les acknowledgments | Incohérence |
| A-16 | Ajouter une explication au paradoxe MCS "w/o QoS" > Full | Confusion lecteur |
| A-17 | Corriger `metric_summary.csv` — aligner `latency`/`mcs_score` | Schéma incohérent |
| A-18 | Corriger `ax.legend()` orphelin dans `generate_ieee_figures.py` | Warning |
| A-19 | Corriger `generate_ablation_figure.py` fallback | Figure trompeuse |
| A-20 | Corriger `table2_ablation.csv` labels variantes | Incohérence |

### Priorité 4 — Basse

| # | Action | Impact |
|---|--------|--------|
| A-21 | Supprimer redondance `tick_labels` dans `figure5_rank_distribution()` | Code fragile |
| A-22 | Supprimer `set_xticks()` dupliqué dans `generate_ieee_figures.py:73–74` | Code inutile |
| A-23 | Vérifier complétude des 9 entrées `and others` dans .bib | Auteurs tronqués |
| A-24 | Supprimer la duplication `marthr_ocp_rank` | Code maintenu en double |

---

## Conclusion

Le projet MARTHR a progressé depuis le premier audit : **9 anomalies corrigées** (dont 4 critiques : section dupliquée, abstract contradictoire, citations manquantes, .bib nettoyé). Le code C standalone et Python sont désormais plus cohérents (normalisation alignée, pénalité de trust unifiée).

Cependant, **les problèmes les plus bloquants persistent** :

1. **Le code ns3 reste non-fonctionnel** — IsBetter inversé, ComputeRank sans inversion, RouteInput retourne false, TrustTable inutilisé, UpdateMetrics hardcodé. Le ns3 ne peut pas produire de résultats publiables.

2. **La baseline MRHOF est toujours buggée** — aucun parent n'est jamais sélectionné, rendant toute comparaison MARTHR vs MRHOF invalide.

3. **5 figures contiennent des données fabriquées** — inacceptable pour un papier scientifique.

4. **Le pipeline de reproduction fonctionne** mais les données sous-jacentes sont incomplètes (3/11 scénarios dans summary_stats).

5. **De nouvelles anomalies manuscrit** sont apparues : incohérence Energy abstract/tableau, erreur de citation MRHOF→OF0.

**Probabilité de publication après amélioration : 50–65%** — progrès notable mais le code ns3 et la baseline MRHOF restent les blockers majeurs.

---

*Rapport généré le 2026-07-23 par audit opencode (mise à jour)*
*Méthodologie suivie : anomalies/METHODOLOGIE_EVALUATION.md*
*Comparaison avec le premier audit : anomalies/opencode.md (version initiale)*
