# Audit Global MARTHR — Prompt pour agent IA

**Projet :** MARTHR (MANET-Trust-Aware Hierarchical Routing Protocol)
**Repository :** https://github.com/madani-belacel/MARTHR_GITHUB
**Auteur :** Madani Belacel, Université Abdelhamid Ibn Badis de Mostaganem

---

## Contexte

Ce projet est un protocole de routage context-aware pour les réseaux MANET. Il combine confiance, énergie et QoS dans un score multi-critères (MCS). Le projet contient :
- Une implémentation C complète avec tests unitaires
- Un simulateur Python avec 11 scénarios de simulation
- Un manuscrit au format IEEE conference
- Des données de simulation générées par les scripts

Le projet utilise l'assistance IA (opencode) pendant le développement. C'est documenté dans le dossier `anomalies/`. Ce dossier contient les rapports d'audit et de suivi du projet — ce sont des artefacts de développement normaux, pas des erreurs.

---

## Prompt à copier-coller

```
Tu es un expert en évaluation de projets scientifiques dans le domaine des réseaux ad hoc (MANET/FANET). Effectue un audit complet du projet MARTHR.

## Accès au projet

Le code source est disponible sur GitHub : https://github.com/madani-belacel/MARTHR_GITHUB
Tu peux consulter les fichiers via web_fetch sur les URLs raw GitHub.

Commence par lire la structure du projet :
- https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/README.md
- https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/manuscript/main.tex
- https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/scripts/marthr_simulator.py
- https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/manuscript/bib/references.bib
- https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/data/raw/marthr_sample.csv
- https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/anomalies/opencode.md

## Objectif de l'audit

Vérifier la qualité scientifique et technique du projet pour préparer une soumission IEEE. L'audit doit être honnête et documenter les vraies faiblesses du projet.

## Étapes d'audit

### Étape 1 — Structure
- Lister les fichiers principaux
- Vérifier la cohérence de l'arborescence

### Étape 2 — Manuscrit (manuscript/main.tex)
- Structure du papier (intro, méthodologie, résultats, conclusion)
- Clarté de la contribution MARTHR
- Claims soutenus par des données réelles ?
- Conformité au format IEEE

### Étape 3 — Code source
- `scripts/marthr_simulator.py` : simulateur principal
- `code_source/` : implémentation C
- Vérifier la logique de calcul (ScoreEngine, RankEngine, TrustTable)
- Vérifier la cohérence entre le code Python et le code C

### Étape 4 — Données
- `data/raw/marthr_sample.csv` : données brutes
- `data/estimated/` : résultats de simulation
- Les données sont-elles générées par les scripts ou hardcodées ?
- Les valeurs dans les tableaux LaTeX correspondent-elles aux CSV ?

### Étape 5 — Figures
- Les figures dans `manuscript/Figures/` sont-elles générées à partir des données CSV ?
- Ou contiennent-elles des valeurs hardcodées ?
- Vérifier la qualité (résolution, lisibilité)

### Étape 6 — Bibliographie (manuscript/bib/references.bib)
- Chaque référence existe-t-elle réellement ?
- Les DOI sont-ils valides ?
- Y a-t-il des références inventées ou incomplètes ?

### Étape 7 — Reproductibilité
- Le pipeline de reproduction (`scripts/reproduce_project.py`) est-il fonctionnel ?
- Les scripts peuvent-ils être exécutés dans l'ordre ?

### Étape 8 — Comparaison avec les bases existantes
- Le manuscrit compare-t-il MARTHR avec des protocoles existants (MRHOF, AODV, RPL) ?
- La comparaison est-elle empirique ou uniquement descriptive ?

## Format de sortie

Produis un rapport avec cette structure :

## Résumé Exécutif
| Sévérité | Nombre |
|----------|--------|
| Critique | X |
| Haute | X |
| Moyenne | X |
| Basse | X |

Pour chaque anomalie :
- **ID** (ex: M1, C1, H1)
- **Sévérité** (Critique / Haute / Moyenne / Basse)
- **Description** claire du problème
- **Localisation** précise (fichier, ligne)
- **Impact** sur la publication
- **Action de correction** concrète

## Règles de sévérité
- **Critique** : Empêche la publication ou la reproductibilité
- **Haute** : Affaiblit significativement le projet
- **Moyenne** : À améliorer mais pas bloquant
- **Base** : Amélioration cosmétique

## Notes importantes

- Le projet utilise le français pour les commentaires du code. C'est normal, ne pas le signaler comme une erreur.
- Le dossier `anomalies/` contient des rapports de suivi du développement. Ce sont des artefacts de travail, pas des erreurs.
- Concentre-toi sur la cohérence scientifique : est-ce que le code produit bien les résultats décrits dans le manuscrit ?
```
