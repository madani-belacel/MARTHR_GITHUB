# Nettoyage du dépôt MARTHR pour publication GitHub

Guide de nettoyage du dépôt `/home/madani/MARTHR` avant publication sur GitHub.

---

## Objectif

Préparer le dépôt MARTHR pour une publication GitHub propre, reproductible et prête à l'emploi.

---

## Instructions de nettoyage

### 1. Supprimer les traces d'IA

Supprimer toutes les mentions d'outils IA :
- `claude`, `chatGPT`, `opencode`, `copilot`, etc.
- Garder les commentaires en français avec style humain
- Rendre le code comme s'il avait été écrit par un humain

### 2. Supprimer les fichiers inutiles

- Scripts de test unitaires (`test_*.py`)
- Fichiers de build artificiels (`__pycache__/`, `*.pyc`)
- Fichiers temporaires et caches
- Doublons de données non nécessaires à la publication

### 3. Conserver les éléments essentiels

- **Données de campagne :**
  - `data/raw/`
  - `data/estimated/`
  - `data/estimated/simulations/`
- **Scripts de reproduction :**
  - `scripts/run_simulation_campaign.py`
  - `scripts/run_pipeline_local.sh`
  - `scripts/statistics/compute_statistics.py`
- **Scripts de simulation :**
  - `scripts/marthr_simulator.py`
  - `scripts/generate_sample_dataset.py`
- **Documentation :**
  - `README.md`
  - `MASTER_TRACKER.md`
  - `anomalies/`

### 4. Vérifier la reproductibilité

- S'assurer que la simulation peut être relancée avec `python3 scripts/run_simulation_campaign.py`
- Vérifier que les données sont générées correctement
- Conserver les logs de campagne

### 5. Formatage du code

- Ajouter un peu de décalage dans l'alignement (2 espaces pour certaines lignes)
- Les boucles `for` et `if` ne sont pas strictement alignées
- Style naturel, pas trop rigide

### 6. Créer l'archive de publication

Créer `publish_ready/MARTHR_publish.tar.gz` contenant :
- Tout le code source
- Les données et figures
- Les scripts de reproduction
- **Exclure** le manuscrit (`manuscript/`) car il sera publié séparément

---

## Structure du dépôt MARTHR

```
/home/madani/MARTHR/
├── README.md                    # Documentation principale
├── MASTER_TRACKER.md           # Suivi du projet
├── PROJECT_PROPOSAL.md         # Proposition du projet
├── code_source/                # Code source principal
│   ├── simulations/
│   │   └── scripts/
│   └── tests/
├── scripts/                    # Scripts de simulation et analyse
│   ├── marthr_simulator.py     # Simulateur MARTHR
│   ├── run_simulation_campaign.py
│   ├── generate_sample_dataset.py
│   └── statistics/
├── data/                       # Données
│   ├── raw/
│   └── estimated/
│       └── simulations/
├── manuscript/                 # Manuscrit LaTeX (exclu de l'archive)
│   ├── main_simple.tex
│   ├── sections/
│   ├── Figures/
│   └── bib/
├── ns3_setup/                  # Configuration NS3
├── anomalies/                  # Rapports d'anomalies
└── conversation_opencode_vscode/ # Documentation interne
```

---

## Checkliste de nettoyage

- [ ] Toutes les mentions d'IA supprimées
- [ ] Scripts de test unitaires supprimés
- [ ] Fichiers temporaires nettoyés
- [ ] Code formaté proprement
- [ ] README.md à jour
- [ ] Simulation relancable
- [ ] Archive créée sans manuscrit
- [ ] Vérification finale effectuée

---

## Commandes de nettoyage rapides

```bash
# Supprimer les caches Python
find /home/madani/MARTHR -type d -name "__pycache__" -exec rm -rf {} +
find /home/madani/MARTHR -name "*.pyc" -delete

# Supprimer les fichiers temporaires
find /home/madani/MARTHR -name "*.tmp" -delete
find /home/madani/MARTHR -name "*.bak" -delete

# Créer l'archive
tar -czf /home/madani/MARTHR/publish_ready/MARTHR_publish.tar.gz \
  --exclude='manuscript' \
  --exclude='.venv' \
  --exclude='conversation_opencode_vscode' \
  -C /home/madani MARTHR
```
