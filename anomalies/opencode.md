# Audit Global MARTHR — Rapport 2026-07-23

## Résumé Exécutif

| Sévérité | Nombre |
|----------|--------|
| Critique | 14 |
| Haute | 10 |
| Moyenne | 14 |
| Basse | 5 |
| **Total** | **43** |

**Score de reproductibilité : 3/10** — Le simulateur fonctionne mais le pipeline de reproduction est cassé, la documentation contient des affirmations fausses, et la baseline MRHOF est buggée.

**Verdict général :** Le projet MARTHR a un potentiel scientifique réel (concept MCS multi-critères intéressant) mais présente des faiblesses techniques majeures qui empêchent actuellement une publication de qualité. Le code ns3 est fondamentalement incohérent avec les implémentations C et Python, 5 figures contiennent des données fabriquées, le pipeline de reproduction est cassé, et le manuscrit contient des claims contradictoires avec ses propres résultats.

---

## 1. Structure du Projet

### 1.1 Vue d'ensemble

Le projet suit une structure bien organisée avec séparation claire entre code source (C, Python, ns3), données, scripts, et manuscrit. La documentation de cadrage est complète (README, MASTER_TRACKER, EXECUTION_PLAN, PROJECT_PROPOSAL).

### 1.2 Anomalies structurelles

| # | Sévérité | Description |
|---|----------|-------------|
| S-1 | Moyenne | Le README référence `sections/` (sections LaTeX) mais ce dossier n'existe pas dans `manuscript/` |
| S-2 | Moyenne | Le README référence `scripts/regenerate_base_csvs.py` et `scripts/generate_marthr_figures.py` — aucun des deux n'existe |
| S-3 | Moyenne | Le README référence `scripts/statistics/compute_ablation_stats.py` — n'existe pas |
| S-4 | Moyenne | Le README référence `internal/METHODOLOGY_AUDIT.md` et `internal/compile.sh` — n'existent pas |

---

## 2. Manuscrit

### 2.1 Anomalies critiques

| # | Ligne(s) | Description |
|---|----------|-------------|
| M-1 | 82–85 | **Section `Protocol Design` dupliquée** — deux `\section{Protocol Design}` consécutifs généreront deux titres dans le PDF |
| M-2 | 25 vs 273 | **Abstract affirme "outperforming MRHOF"** alors que le tableau de résultats (ligne 273) dit explicitement "should not be interpreted as a comparison against MRHOF". Le abstract contredit les résultats. |
| M-3 | 36 | **2 références mentionnées sans `\cite{}`** — OLSR (clausen2003optimized) et MRHOF (gnaneswaran2012mrhof) sont mentionnés dans le texte mais jamais cités avec `\cite`. Ils apparaîtront comme `[?]` dans le PDF. |

### 2.2 Anomalies hautes

| # | Ligne(s) | Description |
|---|----------|-------------|
| M-4 | — | **16 entrées orphelines dans references.bib** — jamais citées dans le manuscrit (16/37 = 43% du fichier .bib inutilisé) |
| M-5 | 269–316 | **7 références arXiv 2025–2026 non vérifiables** — sans DOI, ni volume, ni pages. Les IDs arXiv (2606.xxxxx = juin 2026) sont dans un futur proche. Impossible de confirmer leur existence réelle sans accès web à arXiv. |
| M-6 | 359–370 | **Ablation "scenario-proxied" qualifiée trompeusement d'"ablation study"** — chaque variante utilise un scénario différent (pas de contrôle), ce n'est pas une vraie ablation |
| M-7 | ablation l.12 | **MCS de "w/o QoS" (0.7044) > Full MARTHR (0.6284)** — supprimer QoS améliore le MCS, contradictoire avec le claim que les trois critères sont bénéfiques ensemble |

### 2.3 Anomalies moyennes

| # | Ligne(s) | Description |
|---|----------|-------------|
| M-8 | 36 | OLSR décrit comme "infrastructure-oriented" — incorrect, OLSR est un protocole ad hoc conçu spécifiquement pour les MANETs (RFC 3626) |
| M-9 | — | Pas de section "Acknowledgments" (attendue pour IEEE) |
| M-10 | — | Pas de "Data availability statement" |
| M-11 | 59 | Claim "reinforcement learning approaches have been proposed" sans citation |
| M-12 | 324 | "MARTHR produces more uniform rank distributions" — "more uniform" par rapport à quoi ? Aucune baseline dans la figure |
| M-13 | 335 | "context-aware adaptation does not introduce excessive control overhead" — sans comparaison quantitative |
| M-14 | 357 | "MARTHR explores a wider range of operating points" — figure Pareto ne montre que MARTHR, pas de comparaison |

---

## 3. Code Source

### 3.1 Anomalies critiques

| # | Fichier | Ligne(s) | Description |
|---|---------|----------|-------------|
| C-1 | `ns3_setup/marthr-rank.cc` | 50 | **`IsBetter()` logique INVERSÉE** — ns3 dit "higher is better" alors que C et Python disent "lower is better". Toute décision de routage ns3 est inversée. |
| C-2 | `ns3_setup/marthr-rank.cc` | 28–31 | **`ComputeRank()` ne contient PAS l'inversion MCS ni la pénalité de sauts** — retourne directement le MCS brut, contrairement à C (`1-mcs + hop*0.1`) et Python |
| C-3 | `ns3_setup/marthr-context.cc` | 20–22 | **Poids de contexte de base DIFFÉRENTS** — ns3: (0.35, 0.33, 0.32) vs C/Python: (0.35, 0.40, 0.25) |
| C-4 | `code_source/marthr_context.c` vs `code_source/marthr_core.py` | 44–49 vs 33–34 | **Incohérence normalisation poids** — C: normalise seulement si somme > 1.0; Python: normalise TOUJOURS. Résultats MCS différents pour tout contexte où somme < 1.0 |
| C-5 | `ns3_setup/marthr-routing-protocol.cc` | 72–81 | **`UpdateMetrics()` utilise des valeurs HARDCODEES** — trust=0.8, energy=0.7, qos=0.9 toujours identiques. Aucune métrique réelle extraite. |
| C-6 | `ns3_setup/marthr-routing-protocol.cc` | 25, 72–81 | **Objet `MarthrTrustTable` jamais utilisé** dans le protocole — créé mais jamais appelé. De même pour `m_rank`. |
| C-7 | `ns3_setup/marthr-trust-table.h` vs `marthr-routing-protocol.h` | — | **Incohérence Ipv4 vs Ipv6** — le routage utilise Ipv4 mais la table de confiance utilise Ipv6Address. Mapping impossible. |
| C-8 | `code_source/marthr_core.py` | 65 | **`update_failure()` pénalité MULTIPLICATIVE (*0.8) vs SOUSTRACTIVE (-0.15)** — different de C, ns3 et simulator |
| C-9 | `code_source/marthr_core.py` | 70 | **Noeud inconnu = 0.0 vs 0.5** — C retourne 0.0, marthr_simulator retourne 0.5 (neutre), ns3 retourne 0.5. Le modèle de confiance n'est pas cohérent. |
| C-10 | `ns3_setup/marthr-routing-protocol.cc` | 43–52 | **`RouteInput()` retourne TOUJOURS `false`** — le protocole ns3 ne fait aucun routage intelligent |

### 3.2 Anomalies hautes

| # | Fichier | Description |
|---|---------|-------------|
| C-11 | ns3 headers vs C headers | **Conflit de header guards** — `MARTHR_CONTEXT_H`, `MARTHR_RANK_H`, `MARTHR_SCORE_H` identiques entre C et ns3 |
| C-12 | `marthr_ocp.c` vs `marthr_rank.c` | **Duplication de code** — `marthr_ocp_rank()` et `marthr_compute_ocp_rank()` implémentent la même logique |
| C-13 | `run_simulation_campaign.py:252–256` | **MRHOF scenario "attack" sans simulation réelle d'attaque** — juste 5% perte paquets, pas de noeuds malveillants |
| C-14 | `run_simulation_campaign.py:287` | **Compteur de succès inexact** — affiche "8 scenarios" alors qu'il y en a 11 |
| C-15 | `analyze_campaigns.py:48–53` | **`baseline_mrhof()` lève TOUJOURS RuntimeError** — Table 1 ne peut jamais être générée |

### 3.3 Tableau de cohérence MCS

| Critère | C | Python (core) | Python (simulator) | ns3 |
|---------|---|---------------|---------------------|-----|
| Poids base (NORMAL) | 0.35/0.40/0.25 | 0.35/0.40/0.25 | N/A | **0.35/0.33/0.32** |
| Inversion MCS dans rang | Oui (1-mcs) | Oui | Oui | **NON** |
| Pénalité sauts | Oui (hop×0.1) | Oui | Oui | **NON** |
| IsBetter | lower better | lower better | lower better | **higher better** |
| Trust failure penalty | -0.15 | ×0.8 | -0.15 | -0.15 |
| Trust inconnu | 0.0 | 0.0 | 0.5 | 0.5 |

---

## 4. Données

### 4.1 Nature des données

Les données sont issues d'un **simulateur Python simplifié** (`marthr_simulator.py`), pas de simulations réelles ns3 ni de capteurs physiques. Les scénarios sont des grilles synthétiques (5×5 à 8×8) avec bruit gaussien. Les données ne sont pas "fabriquées" au sens inventées, mais elles sont **simulées** et **reproductibles** grâce à `random.seed()`.

### 4.2 Anomalies de données

| # | Sévérité | Description |
|---|----------|-------------|
| D-1 | Critique | **`MrhofSimulator` ne sélectionne JAMAIS de parent** — MRHOF baseline = vide (mcs=0.0, rank=1.0 partout). La comparaison MRHOF vs MARTHR est biaisée. |
| D-2 | Haute | **README dit "trust = 0.0" mais les données montrent ~0.45–0.50** — note obsolète dans `README_DATA_PROVENANCE.md:78` |
| D-3 | Haute | **Noms de scénarios incohérents** — CSV brut: `lossless, lossy, attack` vs CSV estimated: `lossless_baseline, lossy_network, attack_high_threat` |
| D-4 | Haute | **`simulation_log.txt` orphelin** — 3 lignes seulement, valeurs sans rapport avec les CSV (trust=0.81 vs ~0.5 dans CSV) |
| D-5 | Moyenne | **`metric_summary.csv` utilise `latency` vs `qos_latency` ailleurs** — schéma incohérent |
| D-6 | Moyenne | **`summary_stats.csv` ne couvre que 3/8 scénarios** — incomplet |
| D-7 | Moyenne | **`convergence_time` toujours = 0** dans le CSV brut — métrique inutile/non implémentée |
| D-8 | Moyenne | **`table3_summary.csv` contient 10 scénarios** (dont 3 MRHOF) non documentés |

---

## 5. Reproductibilité

### 5.1 Pipeline de reproduction

**`reproduce_project.py` est cassé.** Il référence 10 scripts qui n'existent pas dans `scripts/` :

```
❌ scripts/regenerate_tables.py
❌ scripts/statistics/summary_stats.py
❌ scripts/statistics/analyze_metrics.py
❌ scripts/analyze_campaigns.py
❌ scripts/generate_latex_table.py
❌ scripts/generate_ieee_figures.py
❌ scripts/generate_missing_figures.py
❌ scripts/generate_ablation_figure.py
❌ scripts/generate_scientific_figure.py
❌ scripts/generate_simple_plot.py
```

Seuls `run_simulation_campaign.py` et `generate_sample_dataset.py` existent réellement.

### 5.2 Score de reproductibilité

| Composant | Statut |
|-----------|--------|
| Simulateur MARTHR | ✅ Fonctionnel |
| Simulateur MRHOF | ❌ Buggé (jamais de parent sélectionné) |
| Pipeline de reproduction | ❌ Cassé (10 scripts manquants) |
| Documentation de provenance | ⚠️ Partiellement obsolète |
| Données CSV | ✅ Présentes et structurées |
| Figures | ⚠️ 5/16 avec données fabriquées |

---

## 6. Figures

### 6.1 Inventaire

16 figures référencées dans `main.tex`, 16 fichiers existants dans `manuscript/Figures/` — correspondance parfaite.

### 6.2 Anomalies

| # | Sévérité | Description |
|---|----------|-------------|
| F-1 | Haute | **5 figures avec données purement fabriquées** (hardcodées dans `generate_missing_figures.py`) : `marthr_dodag_trust.png`, `marthr_pareto_frontier.png`, `marthr_control_overhead.png`, `marthr_attack_detection.png`, `marthr_context_weights.png` |
| F-2 | Haute | **`baseline_comparison.csv` manquant** — `plot_baseline_comparison.py` crashera au runtime |
| F-3 | Moyenne | **`summary_stats.csv` couvre 3/8 scénarios** — figures "scientific" et "summary" incomplètes |
| F-4 | Moyenne | **3 scénarios sans aucune visualisation** (mobility_dynamic, qos_sensitive, mixed_attack_energy) |
| F-5 | Basse | `ax.legend()` sans label dans `figure4_latency_comparison()` — warning matplotlib |
| F-6 | Basse | Redondance `tick_labels` dans `figure5_rank_distribution()` |

---

## 7. Bibliographie

### 7.1 Statistiques

| Métrique | Valeur |
|----------|--------|
| Total entrées .bib | 37 |
| Entrées citées | 21 |
| Entrées orphelines | 16 (43%) |
| Références arXiv non vérifiables | 7 |
| Warnings BibTeX | 1 (`@rfc` non géré par IEEEtran.bst) |

### 7.2 Problèmes

| # | Sévérité | Description |
|---|----------|-------------|
| B-1 | Haute | **7 références arXiv 2025–2026** sans DOI, volume, ni pages — impossibles à vérifier |
| B-2 | Moyenne | **Type `@rfc` non reconnu** par IEEEtran.bst — `winter2012rpl` traité comme `@misc` |
| B-3 | Moyenne | **Auteurs "and others"** dans 12 entrées — réduit la traçabilité |
| B-4 | Basse | 16 entrées orphelines alourdissent inutilement le fichier .bib |

---

## 8. Actions de Correction Recommandées

### Priorité 1 — Critique (avant tout autre travail)

| # | Action | Impact |
|---|--------|--------|
| A-1 | **Corriger le code ns3** — aligner `IsBetter()`, `ComputeRank()`, poids de contexte, et intégrer `TrustTable` et `Rank` dans le protocole | Le ns3 est actuellement inutilisable |
| A-2 | **Corriger `MrhofSimulator`** — le clamp à [0,1] détruit l'ETX. Utiliser une plage non bornée ou ajuster la logique de sélection de parent | Baseline MRHOF = vide |
| A-3 | **Réécrire ou supprimer `reproduce_project.py`** — aligner sur les scripts existants | Pipeline de reproduction cassé |
| A-4 | **Supprimer le duplicata de section "Protocol Design"** dans `main.tex:82–85` | Deux titres dans le PDF |
| A-5 | **Corriger l'abstract** — supprimer "outperforming MRHOF" ou reformuler les résultats | Claim contradictoire avec les résultats |

### Priorité 2 — Haute

| # | Action | Impact |
|---|--------|--------|
| A-6 | **Ajouter `\cite{}` pour OLSR et MRHOF** dans `main.tex:36` | Références affichées comme `[?]` |
| A-7 | **Remplacer les données fabriquées** dans `generate_missing_figures.py` par des données issues des CSV | 5 figures sans base empirique |
| A-8 | **Régénérer ou restaurer `baseline_comparison.csv`** | Script crash |
| A-9 | **Corriger la pénalité de trust** dans `marthr_core.py` (×0.8 → -0.15) pour aligner avec C | Incohérence de calcul |
| A-10 | **Unifier la valeur de trust pour noeud inconnu** (0.0 vs 0.5) entre toutes les implémentations | Comportement imprévisible |
| A-11 | **Corriger la normalisation des poids** dans `marthr_context.c` (ou Python) pour aligner | Résultats MCS différents |
| A-12 | **Vérifier les 7 références arXiv** sur arXiv.org | Risque de références fabriquées |
| A-13 | **Renommer "ablation study" en "scenario-proxied component analysis"** dans le manuscrit | Terminologie trompeuse |
| A-14 | **Supprimer les 16 entrées orphelines** de `references.bib` ou les citer | Fichier .bib inutilement alourdi |

### Priorité 3 — Moyenne

| # | Action | Impact |
|---|--------|--------|
| A-15 | **Unifier les noms de scénarios** entre CSV, README et scripts | Traçabilité brisée |
| A-16 | **Mettre à jour `README_DATA_PROVENANCE.md`** — corriger "trust = 0.0" | Documentation fausse |
| A-17 | **Supprimer ou documenter `simulation_log.txt`** | Fichier orphelin |
| A-18 | **Compléter `summary_stats.csv`** avec les 8 scénarios | Données incomplètes |
| A-19 | **Supprimer la duplication de header guards** entre C et ns3 | Conflits potentiels |
| A-20 | **Supprimer la duplication `marthr_ocp_rank`** | Code maintenu en double |
| A-21 | **Corriger le compteur de succès** dans `run_simulation_campaign.py:287` | Affichage erroné |
| A-22 | **Corriger `analyze_campaigns.py`** — implémenter `baseline_mrhof()` | Script inutilisable |
| A-23 | **Ajouter section "Acknowledgments" et "Data availability"** | Standard IEEE |
| A-24 | **Corriger la description d'OLSR** — n'est pas "infrastructure-oriented" | Erreur factuelle |
| A-25 | **Corriger `ax.legend()` orphelin** dans `generate_ieee_figures.py` | Warning matplotlib |

### Priorité 4 — Basse

| # | Action | Impact |
|---|--------|--------|
| A-26 | Supprimer redondance `tick_labels` dans `figure5_rank_distribution()` | Code inutile |
| A-27 | Supprimer `set_xticks()` dupliqué dans `generate_ieee_figures.py:73–74` | Code inutile |
| A-28 | Ajouter `#include <stdio.h>` dans `test_marthr_core.c` | Dépendance implicite |
| A-29 | Initialiser alpha/beta/gamma dans `marthr_ocp.c:22–23` | Style défensif |
| A-30 | Documenter `scenarios.py` avec des seeds fixes | Reproductibilité mineure |

---

## Conclusion

Le projet MARTHR présente une idée scientifique intéressante (routing multi-critères avec trust adaptatif) mais souffre de problèmes techniques fondamentaux qui empêchent actuellement une publication de qualité :

1. **Le code ns3 est inachevé et incohérent** — il ne représente pas fidèlement le protocole MARTHR
2. **Le pipeline de reproduction est cassé** — 10 scripts référencés n'existent pas
3. **5 figures contiennent des données fabriquées** — inacceptable pour un papier scientifique
4. **Le manuscrit contient des claims contradictoires** — abstract vs résultats
5. **La baseline MRHOF est buggée** — la comparaison est biaisée en faveur de MARTHR

**Probabilité de publication après amélioration : 40–60%** — nécessite un travail substantiel de correction technique avant de pouvoir soumettre.

---

*Rapport généré le 2026-07-23 par audit opencode*
*Méthodologie suivie : anomalies/METHODOLOGIE_EVALUATION.md*
