# Audit MARTHR - Code + Manuscrit

Merci d'auditer l'ensemble du projet MARTHR disponible sur GitHub :
https://github.com/madani-belacel/MARTHR_GITHUB

## Ce qu'il faut vérifier

### Code source
- `code_source/` : cohérence entre le simulateur Python (`marthr_core.py`) et l'implémentation C (`marthr_ocp.c`, `marthr_trust.c`, `marthr_trust.h`)
- `scripts/` : simulateur (`marthr_simulator.py`), campagnes (`run_simulation_campaign.py`), analyse (`analyze_campaigns.py`), reproductibilité (`reproduce_project.py`)
- `tests/` : tests C (`test_marthr_ocp.c`)

### Données
- `data/raw/marthr_sample.csv` : dataset brut
- `data/estimated/` : statistiques résumées et résultats de campagnes
- Vérifier la cohérence entre les chiffres du code et les données produites

### Manuscrit
- `manuscript/main.tex` : texte scientifique
- `manuscript/bib/references.bib` : bibliographie (21 entrées)
- `manuscript/tables/` : tableaux LaTeX
- `manuscript/Figures/` : figures

## Points d'attention
1. Les valeurs du manuscrit (MCS, confiance, énergie, latence) correspondent-elles aux données CSV ?
2. Y a-t-il des références non citées dans le texte ?
3. Y a-t-il des affirmations non soutenues par les résultats ?
4. La section ablation est-elle correctement qualifiée (pas de vraies ablations contrôlées) ?
5. La conformité éthique et académique est-elle respectée ?
6. Les formules (trust, MCS, rang) sont-elles cohérentes entre le code et le manuscrit ?

## Format de réponse
Signalez chaque anomalie avec :
- **Fichier** et **ligne** concernée
- **Problème** identifié
- **Suggestion** de correction
