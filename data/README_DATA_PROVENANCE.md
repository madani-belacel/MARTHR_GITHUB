# Provenance des données MARTHR

## Pipeline de reproduction

### Étape 1 : Simulation
```bash
python3 scripts/run_simulation_campaign.py
```
- 8 scénarios × 20 seeds = 160 runs
- Fichiers générés : `data/estimated/simulations/campaign_*.csv`
- Métriques : trust, energy, qos_latency, mcs, hop_count

### Étape 2 : Régénération des tables
```bash
python3 scripts/regenerate_tables.py
```
- Fichiers générés :
  - `data/estimated/table1_comparison.csv`
  - `data/estimated/table2_ablation.csv`
  - `data/estimated/table3_summary.csv`
  - `data/estimated/baseline_comparison.csv`

### Étape 3 : Dataset d'exemple
```bash
python3 scripts/generate_sample_dataset.py
```
- Fichier généré : `data/raw/marthr_sample.csv`
- 288 lignes (9 nœuds × 32 pas de temps)

### Étape 4 : Statistiques
```bash
python3 scripts/statistics/summary_stats.py
```
- Fichier généré : `data/estimated/summary_stats.csv`

### Étape 5 : Figures
```bash
python3 scripts/generate_ieee_figures.py
python3 scripts/generate_missing_figures.py
python3 scripts/generate_ablation_figure.py
```
- Figures dans `manuscript/Figures/`

### Étape 6 : Compilation
```bash
cd manuscript && latexmk -pdf main.tex
```

## Structure des données

### Colonnes communes
- `seed` : graine aléatoire
- `scenario` : nom du scénario
- `node_id` : identifiant du nœud
- `parent` : identifiant du parent choisi
- `rank` : rang calculé (1.0 - mcs + hop_penalty)
- `trust` : score de confiance [0, 1]
- `energy` : énergie résiduelle normalisée [0, 1]
- `qos_latency` : latence QoS [0, 1]
- `mcs` : score multi-critères [0, 1]
- `hop_count` : nombre de sauts
- `convergence_time` : temps de convergence
- `packet_loss_rate` : taux de perte de paquets

### Scénarios
1. **lossless_baseline** : 5×5, pas de perte, pas d'attaque
2. **lossy_network** : 5×5, 20% perte de paquets
3. **attack_high_threat** : 5×5, 2 nœuds malveillants
4. **energy_stress** : 5×5, déplétion énergétique agressive
5. **stress_large_grid** : 8×8, tests de scalabilité
6. **mobility_dynamic** : 6×6, mobilité + 10% perte
7. **qos_sensitive** : 4×4, focus latence
8. **mixed_attack_energy** : 6×6, attaque + contraintes énergie

## Notes
- Les données brutes (`data/raw/`) sont immuables une fois générées
- Les données estimées (`data/estimated/`) sont régénérables depuis les données brutes
- Le trust est calculé dynamiquement par le modèle de confiance (BETA update) et varie entre 0.0 et 1.0 selon les interactions
