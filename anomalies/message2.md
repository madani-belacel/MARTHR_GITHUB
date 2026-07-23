# Audit MARTHR — Prompt pour Claude

## Instructions

1. Créez le zip : `~/MARTHR_audit.zip` (655 KB, déjà prêt)
2. Collez le prompt ci-dessous dans Claude
3. Claude vous demandera d'uploader le zip — faites-le

---

## Prompt à copier-coller

```
Bonjour, je suis étudiant chercheur en réseaux (MANET) à l'Université de Mostaganem, Algérie. Mon projet MARTHR est un protocole de routage context-aware que je prépare pour une publication IEEE.

Je vous envoie un fichier zip (MARTHR_audit.zip) contenant TOUT le projet. Voici sa structure :

MARTHR_audit.zip/
├── code_source/          # Implémentation C (12 .c/.h + Makefile + 4 tests)
├── scripts/              # Simulateur Python + analyse + figures (17 .py)
├── manuscript/
│   ├── main.tex          # Manuscrit IEEE
│   ├── bib/references.bib
│   └── tables/           # results_table.tex + ablation_table.tex
├── data/
│   ├── raw/marthr_sample.csv
│   ├── estimated/*.csv + simulations/*.csv
│   └── README_DATA_PROVENANCE.md
├── anomalies/            # Rapports de suivi (opencode.md + checklist.md)
├── README.md
└── requirements.txt

## Ce que je vous demande

Un rapport d'audit ultra-détaillé. Pour CHAQUE fichier du zip, donnez :

1. Un résumé de ce que fait le fichier
2. CHAQUE problème trouvé (bug, incohérence, valeur hardcodée, etc.) avec le numéro de ligne exact
3. Les points positifs
4. La sévérité (Critique / Haute / Moyenne / Basse)

## Vérifications spécifiques

### Code C vs Python
Comparez les formules de calcul dans :
- code_source/marthr_ocp.c (fonction marthr_ocp_rank)
- code_source/marthr_rank.c (fonction marthr_compute_ocp_rank)
- scripts/marthr_simulator.py (classe MarthrNode, méthode compute_rank)
Est-ce que les 3 implémentent la même formule ? Sinon, lequel est correct ?

### Manuscrit vs Code
Lisez manuscript/main.tex et vérifiez que :
- Les équations décrites correspondent au code
- Les résultats présentés dans les tableaux correspondent aux CSV de data/
- Les légendes des figures sont honnêtes (pas de claims exagérés)
- L'abstract ne contient pas de claims non supportés par les données

### Données
Comparez :
- data/estimated/table3_summary.csv avec manuscript/tables/results_table.tex
- data/raw/marthr_sample.csv (combien de seeds ? combien de lignes ?)
- Les 11 CSV dans data/estimated/simulations/ (sont-ils cohérents entre eux ?)

### Bibliographie
Pour chaque référence dans manuscript/bib/references.bib :
- Le titre existe-t-il réellement sur Google Scholar ?
- Les auteurs sont-ils corrects ?
- Y a-t-il des références jamais citées dans main.tex ?

### Pipeline de reproduction
Lisez scripts/reproduce_project.py et vérifiez que tous les scripts existent et sont cohérents.

## Format de sortie

### Résumé exécutif
| Sévérité | Nombre |
|----------|--------|
| Critique | X |
| Haute | X |
| Moyenne | X |
| Basse | X |

### Détail par fichier
Pour chaque fichier : résumé + problèmes (avec lignes) + points positifs + sévérité

### Incohérences transversales
Listez TOUTES les incohérences entre fichiers différents

### 5 actions prioritaires avant soumission
```
