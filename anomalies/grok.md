Audit Global MARTHR — Rapport d'Évaluation 2026-07-23

Expertise : Évaluation de projets scientifiques en réseaux ad hoc (MANET), reproductibilité, qualité IEEE.

Résumé Exécutif

| Sévérité | Nombre (restantes) | Impact |
|----------|---------------------|--------|
| Critique | 2 | Bloque publication / reproductibilité |
| Haute | 4 | Affaiblit significativement les claims |
| Moyenne | 5 | Améliorations nécessaires |
| Basse | 3 | Cosmétique / maintenance |

Probabilité de publication IEEE après corrections : 70-80% (bon potentiel scientifique, mais pipeline fragile et incohérences persistantes). Le projet montre une idée solide (MCS context-aware unifiant trust/energy/QoS) avec implémentations C/Python cohérentes, mais souffre de problèmes classiques de "prototype académique" : données partielles, hardcoding résiduel, et claims non pleinement soutenus.

Anomalies Identifiées

Critique (2)
C1: Pipeline reproduce_project.py fragile et partiellement obsolète (scripts/reproduce_project.py:21-33)  
Appelle de nombreux scripts (run_simulation_campaign.py, generate_ieee_figures.py, etc.) qui peuvent échouer sur KeyError (ex: anciennes colonnes comme pdr).  
Dépendance à latexmk sans flag --skip-latex robuste.  
Impact** : Reproductibilité compromise (C1 dans checklist.md).  
Correction** : Mettre à jour pour chemins relatifs, flags optionnels, et tester end-to-end. Regénérer données via run_simulation_campaign.py.

C2: Incohérences persistantes claims manuscrit vs. données (manuscript/main.tex ~lignes abstract/résultats)  
Abstract cite trust=0.4593, energy=0.5327, MCS=0.6321, latency=0.3679 — cohérent avec sample.csv, mais ablation et baselines (MRHOF) manquent de comparaison empirique complète.  
Tableau ablation utilise "proxies de scénarios" (pas ablation contrôlée réelle).  
Impact** : Claims trop affirmatifs sans preuves statistiques solides (Mann-Whitney mentionnées mais pas toujours appliquées).  
Correction** : Mettre à jour tables/results_table.tex + ablation_table.tex avec regenerate_tables.py; clarifier limites dans texte.

Haute (4)
H1: Figures partiellement hardcodées / non fully tracées (scripts/generate_ieee_figures.py et similaires)  
Checklist (H1) et opencode.md signalent valeurs hardcodées résiduelles. Certaines figures (PNG/PDF mix) ne sont pas 100% générées des CSV campagnes.  
Correction* : Utiliser exclusivement données CSV (data/estimated/).

H2: Pas de baseline MRHOF empirique complète (malgré implémentation MrhofNode dans marthr_simulator.py)  
Manuscrit positionne vs. MRHOF/RPL mais comparaison descriptive. MRHOF est simulé mais pas systématiquement rapporté dans tables/figures.  
Impact** : Faiblesse majeure pour IEEE (manque de "outperforms baseline").  
Correction** : Intégrer runs MRHOF dans campagnes et updater figures/tables.

H3: Limites de données (seeds, scénarios hétérogènes)  
marthr_sample.csv : ~4 seeds (pas 20). Scénario hétérogène (aérien/sol) non implémenté dans simulateur.  
Correction** : Archiver données complètes (20 seeds) et étendre simulateur.

H4: Incohérences C vs. Python (MAX_ENTRIES, OCP rank legacy)  
Résolues partiellement (selon opencode.md), mais vérifier alignement post-corrections.

Moyenne (5)
M1**: Chemins absolus / portabilité scripts (M1 checklist).  
M2**: Documentation provenance données insuffisante (data/README_DATA_PROVENANCE.md).  
M3**: Mélange formats figures (PNG/PDF); certaines non référencées.  
M4**: Bibliographie : ~24 refs, quelques incomplètes, auto-citation nettoyée mais vérifier DOIs récents 2020-2026.  
M5**: Tests unitaires C bons mais couverture incomplète (cas limites).

Basse (3)
Nettoyage .bak, artefacts dev (conversation_opencode_vscode/), .gitignore manquant.  
Commentaires français OK (règle projet).  
Structure globale bonne (un seul main.tex).

Points Forts
Idée scientifique solide** : MCS context-aware + adaptation dynamique est une contribution pertinente (gap dans littérature trust/energy/QoS unifié + ablation).
Implémentations modulaires (C99 + Python port fidèle).
Pipeline de reproduction existant + données CSV tracées.
Manuscrit bien structuré IEEE (~8+ pages potentiel), équations claires, figures nombreuses (>12 potentiellement).
Tests unitaires passent; simulateur fonctionnel.

Recommandations & Plan d'Action Prioritaire (Priorité 1)

Exécuter pipeline complet : cd /project && python3 scripts/reproduce_project.py (fixer erreurs en cours de route). Regénérer tables/figures.
Corriger C1/C2 : Mettre à jour manuscrit + tables avec vraies valeurs post-campagne.
Implémenter/renforcer baseline : Runs MRHOF systématiques + stats (Mann-Whitney).
Validation finale :
   reproduce_project.py → succès.
   main.pdf ≥8 pages, ≥12 figures référencées.
   Tables match CSV.
   Bibliographie ≥25 refs réelles avec DOIs.
Nettoyage : rm *.bak; .gitignore; README_DATA_PROVENANCE.md complet.

Verdict : Projet prometteur avec base reproductible, mais nécessite 1-2 jours de corrections ciblées pour atteindre le niveau soumission IEEE conference. Suivre METHODOLOGIE_EVALUATION.md et checklist.md. Le potentiel est réel — focus sur cohérence données/texte/baseline.

Prêt à assister pour corrections spécifiques (ex: debug script, régénération données, édition LaTeX). Fournir logs d'exécution si besoin.
