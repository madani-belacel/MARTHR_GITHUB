# Méthodologie d'évaluation et de nettoyage du projet MARTHR

Ce document décrit la méthodologie pour évaluer, auditer et nettoyer le projet MARTHR (MANET-Trust-Aware Hierarchical Routing Protocol).

Conçu pour être suivi par un agent IA lors d'un audit global ou d'un nettoyage du projet.

---

## 1. Objectif

Évaluer et corriger le projet MARTHR en vérifiant :
- la qualité scientifique globale,
- la structure du manuscrit,
- la cohérence entre code, données, figures et texte,
- la reproductibilité,
- la qualité de la bibliographie,
- la capacité du projet à être publié dans une revue de haut niveau.

---

## 2. Philosophie de l'évaluation

1. **Vérifier avant de conclure** — Toute affirmation doit être étayée par une preuve.
2. **Séparer potentiel scientifique et faiblesses techniques** — Un projet peut avoir une bonne idée mais être fragile expérimentalement.
3. **Être honnête, constructif et précis** — Identifier ce qui empêche une publication de qualité.

---

## 3. Étapes d'audit du projet MARTHR

### Étape 1 — Comprendre la structure

Lire la structure du projet :

```
/home/madani/MARTHR/
├── README.md
├── MASTER_TRACKER.md
├── code_source/          # Code source principal
├── scripts/              # Scripts de simulation et analyse
│   ├── marthr_simulator.py
│   ├── run_simulation_campaign.py
│   └── statistics/
├── data/                 # Données
│   ├── raw/
│   └── estimated/
├── manuscript/           # Manuscrit LaTeX
│   ├── main.tex
│   ├── sections/
│   └── Figures/
├── ns3_setup/            # Configuration NS3
└── anomalies/            # Rapports d'anomalies
```

---

### Étape 2 — Lire les documents de cadrage

Lire dans l'ordre :
1. `README.md`
2. `MASTER_TRACKER.md`
3. `PROJECT_PROPOSAL.md`
4. `anomalies/opencode.md` (anomalies identifiées)

---

### Étape 3 — Analyser le manuscrit

Vérifier `manuscript/main.tex` :
- structure logique du papier,
- clarté de la contribution MARTHR,
- qualité de la rédaction,
- cohérence des arguments,
- adéquation au journal cible.

Sections à vérifier :
- titre et résumé,
- introduction et positionnement,
- revue de littérature,
- méthodologie MARTHR,
- résultats et discussion,
- limites et conclusion.

---

### Étape 4 — Examiner le code source

Fichiers principaux à analyser :
- `scripts/marthr_simulator.py` — Simulateur MARTHR
- `scripts/run_simulation_campaign.py` — Campagnes de simulation
- `scripts/generate_sample_dataset.py` — Génération de données
- `ns3_setup/marthr-routing-protocol.cc` — Implémentation NS3

Vérifications :
- cohérence du design logiciel,
- modularité,
- logique de calcul (ScoreEngine, RankEngine, TrustTable),
- présence de placeholders ou d'anomalies,
- possibilité de reproduire les expériences.

---

### Étape 5 — Vérifier les données

Inspecter :
- `data/raw/` — Données brutes
- `data/estimated/simulations/` — Résultats de simulation
- Fichiers CSV : colonnes, nombre de lignes, cohérence

Questions clés :
- les données existent-elles réellement ?
- sont-elles cohérentes ?
- les figures sont-elles alimentées par des données réelles ?

---

### Étape 6 — Vérifier la reproductibilité

Vérifier que :
- `python3 scripts/run_simulation_campaign.py` s'exécute
- Les scripts génèrent des résultats cohérents
- La documentation est à jour

---

### Étape 7 — Évaluer les figures et tableaux

Vérifier dans `manuscript/Figures/` :
- pertinence scientifique,
- lisibilité,
- cohérence avec les données,
- capacité à supporter les conclusions.

---

### Étape 8 — Vérifier la bibliographie

Inspecter `manuscript/bib/` :
- références réelles et valides,
- métadonnées cohérentes,
- références récentes et pertinentes,
- pas de références douteuses.

---

### Étape 9 — Produire le rapport d'audit

Synthétiser :
- points forts,
- faiblesses majeures,
- anomalies critiques,
- actions de correction prioritaires,
- probabilité de publication après amélioration.

---

## 4. Commandes utiles

### 4.1 Lister les fichiers du projet

```bash
find /home/madani/MARTHR -maxdepth 3 -type f | sort
```

### 4.2 Rechercher des placeholders

```bash
grep -rn "TODO\|TBD\|placeholder\|ESTIMATED" /home/madani/MARTHR/scripts/
```

### 4.3 Vérifier la compilation LaTeX

```bash
cd /home/madani/MARTHR/manuscript && pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

### 4.4 Exécuter les simulations

```bash
cd /home/madani/MARTHR && python3 scripts/run_simulation_campaign.py
```

### 4.5 Vérifier les données CSV

```bash
head -20 /home/madani/MARTHR/data/estimated/simulations/campaign_*.csv
```

---

## 5. Types d'anomalies recherchées

### 5.1 Anomalies structurelles
- fichiers manquants,
- incohérence entre dossiers et contenu,
- documentation obsolète.

### 5.2 Anomalies de manuscrit
- texte trop affirmatif,
- incohérences entre résultats et discussion,
- figures mal justifiées.

### 5.3 Anomalies de code
- placeholders non remplacés,
- logique non robuste,
- dépendances mal documentées.

### 5.4 Anomalies de données
- données absentes ou incohérentes,
- fichiers de sortie vides,
- provenance non traçable.

### 5.5 Anomalies de reproductibilité
- scripts non exécutables,
- étapes de traitement mal décrites.

### 5.6 Anomalies de bibliographie
- références douteuses,
- DOI manquants.

---

## 6. Checklist d'audit rapide

Avant de valider le projet MARTHR :

- [ ] Structure du projet claire
- [ ] Manuscrit cohérent et bien organisé
- [ ] Résultats soutenus par des données réelles
- [ ] Scripts exécutables
- [ ] Figures et tableaux traçables
- [ ] Reproductibilité démontrable
- [ ] Bibliographie propre et pertinente
- [ ] Limites honnêtes
- [ ] Conclusions ne dépassent pas les preuves

---

## 7. Nettoyage du dépôt

Objectifs :
- Vérifier que la documentation est à jour
- Conserver données et scripts de reproduction
- S'assurer que le README est complet

---

## 8. Conclusion

Cette méthodologie permet d'évaluer le projet MARTHR de manière rigoureuse et de le préparer pour une publication de qualité.

L'agent IA doit :
1. Suivre les étapes dans l'ordre
2. Documenter chaque anomalie trouvée
3. Proposer des corrections précises
4. Vérifier que les corrections sont effectives
