# Audit MARTHR — Prompt à copier-coller

Collez le texte ci-dessous dans une session IA (Claude, ChatGPT, etc.) :

---

```
Je suis étudiant chercheur à l'Université Abdelhamid Ibn Badis de Mostaganem (Algérie). Mon projet MARTHR est un protocole de routage MANET que je prépare pour publication IEEE. J'ai besoin d'un audit complet et honnête.

Le code est sur GitHub : https://github.com/madani-belacel/MARTHR_GITHUB

## Ce que je veux

Un rapport d'audit détaillé qui couvre CHAQUE fichier du projet. Je veux que vous lisiez le code ligne par ligne, le manuscrit paragraph par paragraph, et les données CSV colonne par colonne.

## Comment accéder aux fichiers

Utilisez web_fetch pour lire les fichiers depuis GitHub. Voici les URLs de base :

https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/

Ajoutez le chemin du fichier après. Par exemple :
- Pour lire le manuscrit : https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/manuscript/main.tex
- Pour lire le simulateur : https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/scripts/marthr_simulator.py
- Pour lire les références : https://raw.githubusercontent.com/madani-belacel/MARTHR_GITHUB/main/manuscript/bib/references.bib

## Liste des fichiers à examiner

Commencez par lire la structure avec cette URL :
https://api.github.com/repos/madani-belacel/MARTHR_GITHUB/git/trees/main?recursive=1

Puis lisez CHAQUE fichier ci-dessous :

### Manuscrit (lire intégralement)
1. manuscript/main.tex
2. manuscript/bib/references.bib
3. manuscript/tables/results_table.tex
4. manuscript/tables/ablation_table.tex

### Code Python (lire chaque ligne)
5. scripts/marthr_simulator.py
6. scripts/run_simulation_campaign.py
7. scripts/regenerate_tables.py
8. scripts/generate_sample_dataset.py
9. scripts/compare_with_baseline.py
10. scripts/analyze_campaigns.py
11. scripts/generate_ieee_figures.py
12. scripts/generate_ablation_figure.py
13. scripts/generate_missing_figures.py
14. scripts/generate_latex_table.py
15. scripts/generate_scientific_figure.py
16. scripts/generate_simple_plot.py
17. scripts/plot_baseline_comparison.py
18. scripts/reproduce_project.py
19. scripts/statistics/summary_stats.py
20. scripts/statistics/analyze_metrics.py
21. scripts/scenarios.py

### Code C (lire chaque fichier)
22. code_source/marthr_ocp.c
23. code_source/marthr_ocp.h
24. code_source/marthr_rank.c
25. code_source/marthr_rank.h
26. code_source/marthr_trust.c
27. code_source/marthr_trust.h
28. code_source/marthr_score.c
29. code_source/marthr_score.h
30. code_source/marthr_context.c
31. code_source/marthr_context.h
32. code_source/marthr_metric_log.c
33. code_source/marthr_metric_log.h
34. code_source/Makefile
35. code_source/tests/test_marthr_core.c
36. code_source/tests/test_marthr_rank.c
37. code_source/tests/test_marthr_ablation.c
38. code_source/tests/test_marthr_ocp.c

### Données (vérifier colonnes et cohérence)
39. data/raw/marthr_sample.csv
40. data/estimated/summary_stats.csv
41. data/estimated/table2_ablation.csv
42. data/estimated/table3_summary.csv
43. data/estimated/simulations/campaign_lossless_baseline_aggregated.csv (lire les 5 premières lignes)
44. data/estimated/simulations/campaign_mrhof_lossless_aggregated.csv (lire les 5 premières lignes)
45. data/README_DATA_PROVENANCE.md

### Documentation
46. README.md
47. requirements.txt

## Structure du rapport

Pour CHAQUE fichier examiné, donnez :

### Fichier : [nom du fichier]
- **Résumé** : 2-3 phrases sur ce que fait ce fichier
- **Problèmes trouvés** : liste numérotée avec numéro de ligne exact
  - Problème 1 (ligne X) : description
  - Problème 2 (ligne X) : description
- **Points positifs** : ce qui est bien fait
- **Sévérité** : Critique / Haute / Moyenne / Basse

Ensuite, ajoutez une section transversale :

## Incohérences entre fichiers
Listez TOUTES les incohérences entre :
- Le manuscrit et le code (est-ce que le code fait ce que le texte décrit ?)
- Le code C et le code Python (est-ce que les formules sont identiques ?)
- Les données CSV et les tableaux LaTeX (est-ce que les valeurs correspondent ?)
- Les figures et les données (est-ce que les figures sont générées depuis les CSV ?)

## Bibliographie
Pour CHAQUE référence dans references.bib :
- Le titre existe-t-il réellement ?
- Les auteurs sont-ils corrects ?
- L'année est-elle correcte ?
- Le DOI est-il valide (si disponible) ?

## Reproductibilité
Le pipeline reproduce_project.py peut-il être exécuté sans erreur ?
Quels scripts dépendent les uns des autres ?

## Résumé exécutif final
| Catégorie | Nombre d'anomalies |
|-----------|-------------------|
| Critique | X |
| Haute | X |
| Moyenne | X |
| Basse | X |

## Recommandations prioritaires
Listez les 5 actions les plus urgentes à faire AVANT la soumission.
```
