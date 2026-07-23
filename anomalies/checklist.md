# Checklist MARTHR — Tâches restantes et corrections

**Projet :** MARTHR (MANET-Trust-Aware Hierarchical Routing Protocol)
**Dernière mise à jour :** 2026-07-22

---

## RÈGLES GÉNÉRALES À SUIVRE

### Langage et style
- **Commentaires en français** — c'est volontaire, ne pas les signaler comme erreurs
- **Code style humain** — alignement variable, pas trop rigide
- **Ne jamais ajouter de commentaires IA** : `claude`, `chatGPT`, `opencode`, `copilot`, `AI-generated`, etc.

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

## ANOMALIES IDENTIFIÉES (opencode.md + VSCODE.md)

### Critique (3)
| # | Source | Description | Statut |
|---|--------|-------------|--------|
| C1 | VSCODE | Pipeline reproduce_project.py échoue (KeyError: pdr) | ⏳ |
| C2 | VSCODE | NS-3 skeleton non fonctionnel (hardcoded values) | ℹ️ Futur |
| C3 | OpenCode | Claims manuscrit incohérents avec données réelles | ⏳ |

### Haute (5)
| # | Source | Description | Statut |
|---|--------|-------------|--------|
| H1 | OpenCode | Figures avec valeurs hardcodées (generate_ieee_figures.py) | ⏳ |
| H2 | OpenCode | generate_ablation_figure.py crash (colonnes) | ✅ Corrigé |
| H3 | VSCODE | Données synthétiques dans generate_sample_dataset.py | ✅ Corrigé |
| H4 | VSCODE | Scripts pipeline non stabilisés | ⏳ |
| H5 | OpenCode | compute_rank() identité | ✅ Corrigé |

### Moyenne (6)
| # | Source | Description | Statut |
|---|--------|-------------|--------|
| M1 | VSCODE | Chemins absolus dans scripts | ⏳ |
| M2 | VSCODE | Provenance données insuffisamment documentée | ⏳ |
| M3 | VSCODE | Incohérence métriques sample vs campagnes | ⏳ |
| M4 | OpenCode | generate_missing_figures.py valeurs hardcodées | ⏳ |
| M5 | OpenCode | Tables/results_table.tex pas à jour | ⏳ |
| M6 | OpenCode | Tables/ablation_table.tex pas à jour | ⏳ |

### Basse (2)
| # | Source | Description | Statut |
|---|--------|-------------|--------|
| B1 | VSCODE | Bibliographie à vérifier plus finement | ⏳ |
| B2 | OpenCode | Fichiers .bak à supprimer | ⏳ |

---

## TÂCHES DE CORRECTION

### Priorité 1 — Critique

- [ ] **C1: Corriger reproduce_project.py**
  - Mettre à jour le pipeline pour utiliser les nouveaux scripts
  - Supprimer les dépendances aux anciennes colonnes (pdr, latency)
  - Compiler main.tex au lieu de main_simple.tex

- [ ] **C3: Corriger les claims du manuscrit**
  - Les valeurs trust=0.79, latency=0.13 ne correspondent pas aux données réelles
  - Mettre à jour tables/results_table.tex avec les vraies valeurs
  - Mettre à jour le texte du manuscrit

- [ ] **Régénérer les données avec compute_rank corrigé**
  ```bash
  python3 scripts/run_simulation_campaign.py
  python3 scripts/regenerate_tables.py
  python3 scripts/generate_sample_dataset.py
  ```

### Priorité 2 — Haute

- [ ] **H1: Corriger generate_ieee_figures.py**
  - Supprimer les valeurs hardcodées
  - Utiliser les données des CSV campagne

- [ ] **H4: Stabiliser les scripts pipeline**
  - Vérifier que tous les scripts fonctionnent ensemble
  - Mettre à jour reproduce_project.py

- [ ] **M5: Mettre à jour tables/results_table.tex**
  - Utiliser les données réelles des campagnes

- [ ] **M6: Mettre à jour tables/ablation_table.tex**
  - Utiliser les données réelles de table2_ablation.csv

### Priorité 3 — Moyenne

- [ ] **M1: Rendre les scripts portables**
  - Utiliser des chemins relatifs au lieu de chemins absolus

- [ ] **M2: Documenter la provenance des données**
  - Mettre à jour data/README_DATA_PROVENANCE.md

- [ ] **M3: Aligner les métriques sample vs campagnes**
  - S'assurer que marthr_sample.csv utilise les mêmes colonnes que les campagnes

- [ ] **M4: Corriger generate_missing_figures.py**
  - Utiliser des données réelles au lieu de valeurs hardcodées

### Priorité 4 — Basse

- [ ] **B1: Vérifier la bibliographie**
  - Chaque référence a un DOI valide
  - Pas de placeholders

- [ ] **B2: Supprimer les fichiers .bak**
  ```bash
  rm -f manuscript/*.bak
  ```

---

## VALIDATION FINALE

Avant de considérer le projet prêt :

- [ ] `python3 scripts/reproduce_project.py` fonctionne
- [ ] Le manuscrit compile sans erreur
- [ ] Le PDF a minimum 8 pages
- [ ] Il y a minimum 12 figures
- [ ] Les données dans les tableaux correspondent aux CSV
- [ ] Pas de mots-clés IA dans le code
- [ ] L'archive de publication est créée
