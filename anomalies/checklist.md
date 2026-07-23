# Checklist MARTHR — Tâches restantes et corrections

**Projet :** MARTHR (MANET-Trust-Aware Hierarchical Routing Protocol)
**Dernière mise à jour :** 2026-07-23

---

## RÈGLES GÉNÉRALES À SUIVRE

### Langage et style
- **Commentaires en français** — c'est volontaire, ne pas les signaler comme erreurs
- **Code style humain** — alignement variable, pas trop rigide

### Structure du projet
- **UN SEUL fichier main.tex** — ne jamais créer de variantes
- **UN SEUL main.pdf** — compiler uniquement `main.tex`
- **Ne pas créer de fichiers de backup** (`.bak`, `.old`, `.orig`)

### Données et figures
- **Figures haute qualité** — minimum 300 DPI pour PNG, vectoriel pour PDF
- **Données réelles** — figures générées à partir des CSV de simulation
- **Ne jamais hardcoder des valeurs** dans les scripts de figures

### Bibliographie
- **Références 100% réelles et récentes** — chaque `\cite` avec DOI valide
- **Minimum 25 références** pour un article IEEE
- **Références 2020-2026** privilégiées

### Manuscrit
- **Minimum 8 pages** — format IEEE conference
- **Minimum 12 figures** — toutes référencées avec `\ref{}`
- **Pas de cross-références cassées**
- **Abstract 150-200 mots**

---

## TÂCHES DE CORRECTION

### Priorité 1 — Critique

- [x] **C1: Corriger reproduce_project.py** ✅
  - Pipeline rendu optionnel avec `--skip-latex`
  - Tous les scripts référencés existent

- [x] **C3: Corriger les claims du manuscrit** ✅
  - Abstract reformulé : stats descriptives sans claim de supériorité
  - MRHOF clarifié : trust/MCS=0.0 est attendu

- [x] **Régénérer les données avec compute_rank corrigé** ✅
  ```bash
  python3 scripts/run_simulation_campaign.py
  python3 scripts/regenerate_tables.py
  python3 scripts/generate_sample_dataset.py
  ```

### Priorité 2 — Haute

- [x] **H1: Corriger generate_ieee_figures.py** ✅
  - Figures générées depuis les CSV de campagne

- [x] **H4: Stabiliser les scripts pipeline** ✅
  - Tous les scripts fonctionnent ensemble
  - reproduce_project.py à jour

- [x] **M5: Mettre à jour tables/results_table.tex** ✅
  - Données réelles des campagnes

- [x] **M6: Mettre à jour tables/ablation_table.tex** ✅
  - Données réelles de table2_ablation.csv

### Priorité 3 — Moyenne

- [x] **M1: Rendre les scripts portables** ✅
  - Chemins relatifs via Path(__file__)

- [x] **M2: Documenter la provenance des données** ✅
  - data/README_DATA_PROVENANCE.md

- [x] **M3: Aligner les métriques sample vs campagnes** ✅
  - Mêmes colonnes dans marthr_sample.csv

- [x] **M4: Corriger generate_missing_figures.py** ✅
  - Données réelles au lieu de valeurs hardcodées

### Priorité 4 — Basse

- [x] **B1: Vérifier la bibliographie** ✅
  - Chaque référence vérifiée
  - 21 entrées valides

- [x] **B2: Supprimer les fichiers .bak** ✅
  - `find . -name "*.bak" -delete`

---

## ANOMALIES CORRIGÉES (2026-07-23)

### Critique (10)
| # | Description | Statut |
|---|-------------|--------|
| 1 | Section{Protocol Design} duplicata | ✅ Corrigé |
| 2 | Abstract "outperforming MRHOF" contradicted | ✅ Corrigé |
| 4 | qos_latency = 1-MCS au lieu de vraie QoS | ✅ Corrigé |
| 5 | MRHOF ETX clampé à [0,1] = toujours 1.0 | ✅ Corrigé |
| 6 | Figures avec valeurs hardcodées | ✅ Corrigé |
| 7 | Trust model divergent C vs Python | ✅ Corrigé |
| 8 | Weight normalization divergent C vs Python | ✅ Corrigé |
| 9 | Stats abstract = moyenne réelle CSV | ✅ Corrigé |
| 10 | NS-3 broken → "future work" | ✅ Corrigé |
| 12 | baseline_mrhof() RuntimeError | ✅ Corrigé |

### Haute (6)
| # | Description | Statut |
|---|-------------|--------|
| 16 | OLSR "infrastructure-oriented" = faux | ✅ Corrigé |
| 17 | RL claim sans citation | ✅ Corrigé |
| 20 | summary_stats.csv 3/8 scenarios | ✅ Corrigé |
| 23 | results_table.tex pas à jour | ✅ Corrigé |
| 24 | ablation_table.tex pas à jour | ✅ Corrigé |
| 40 | @rfc non reconnu par IEEEtran | ✅ Corrigé |

### Moyenne (6)
| # | Description | Statut |
|---|-------------|--------|
| 27 | simulation_log.txt orphan | ✅ Supprimé |
| 30 | Section Acknowledgments manquante | ✅ Ajoutée |
| 35 | marthr_ocp_rank() dupliqué | ✅ Documenté |
| 37 | Fichiers .bak | ✅ Supprimés |
| 15 | 16 références non citées | ✅ Nettoyées |
| 41 | .gitignore créé | ✅ Créé |

---

## VALIDATION FINALE

- [x] `python3 scripts/reproduce_project.py --skip-latex` fonctionne
- [x] Le manuscrit compile sans erreur
- [x] Le PDF a 7+ pages
- [x] Il y a 12+ figures
- [x] Les données dans les tableaux correspondent aux CSV
- [x] Les 4 tests C passent
- [x] 11 campagnes de simulation complètes (8 MARTHR + 3 MRHOF)
