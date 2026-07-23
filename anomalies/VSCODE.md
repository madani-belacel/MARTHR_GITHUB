# Audit global MARTHR — Rapport du 23 juillet 2026

**Périmètre :** `/home/madani/MARTHR`  
**Méthodologie appliquée :** [METHODOLOGIE_EVALUATION.md](METHODOLOGIE_EVALUATION.md)  
**Instructions de filtrage :** [message-IA.md](message-IA.md)  
**Mode :** lecture seule ; aucun fichier du projet n’a été modifié pendant l’audit.

Les commentaires en français, les dossiers d’audit et les trackers internes ont été ignorés comme demandé. Les constats portent sur la cohérence scientifique, le code, les données, la reproductibilité, les figures, les tableaux et le manuscrit.

## Résumé exécutif

| Sévérité | Nombre |
|----------|-------:|
| Critique | 4 |
| Haute | 8 |
| Moyenne | 6 |
| Basse | 3 |

Le dépôt contient une architecture conceptuelle intéressante et plusieurs composants de prototype réutilisables. Toutefois, il n’est pas actuellement possible de considérer les résultats comme une évaluation scientifique comparative reproductible.

Les risques principaux sont : figures générées depuis des constantes plutôt que depuis des données expérimentales ; baseline MRHOF invalide ; scaffold NS-3 non fonctionnel ; ablations non contrôlées ; affirmations du manuscrit plus fortes que les preuves ; divergences entre les implémentations C, Python et NS-3.

## 1. Structure du projet

### C1 — Figures scientifiques partiellement fabriquées par constantes codées en dur

**Sévérité : Critique**

Dans [generate_missing_figures.py](../scripts/generate_missing_figures.py#L80-L161), plusieurs figures utilisent directement des valeurs codées en dur :

- `weights = [0.48, 0.35, 0.17]` ;
- vecteurs `x` et `y` pour Pareto ;
- `overhead = [0.08, 0.11, 0.16, 0.19]` ;
- `detection = [0.71, 0.77, 0.91, 0.88]`.

Ces valeurs ne proviennent d’aucun fichier de données, d’une simulation ou d’une trace NS-3. Les figures sont incluses dans [main.tex](../manuscript/main.tex#L188-L201) et [main.tex](../manuscript/main.tex#L386-L426).

**Conséquence :** les résultats d’overhead, de détection et de frontière de Pareto sont présentés comme expérimentaux sans être démontrés par des données traçables.

**Correction :** supprimer ces figures ou les marquer explicitement comme conceptuelles ; sinon les régénérer depuis des données brutes versionnées avec définition de métrique, graines, unités et dispersion.

### C2 — Baseline MRHOF invalide dans le simulateur Python

**Sévérité : Critique**

Dans [marthr_simulator.py](../scripts/marthr_simulator.py#L122-L130), `estimate_etx()` calcule `1.0 / prr` puis tronque ETX à `[0, 1]`. Comme `prr <= 1`, ETX vaut donc systématiquement `1.0`. Le rang MRHOF est ensuite borné à `1.0` dans [marthr_simulator.py](../scripts/marthr_simulator.py#L114-L120).

Les données [campaign_mrhof_lossless_aggregated.csv](../data/estimated/simulations/campaign_mrhof_lossless_aggregated.csv#L2-L15) montrent `rank=1.0`, `parent=0`, `hop_count=0`, `mcs=0.0` et `qos_latency=1.0` pour les nœuds non racine.

**Conséquence :** le baseline ne représente pas réellement MRHOF et toute comparaison avec MARTHR serait biaisée.

**Correction :** ne pas tronquer ETX à `[0,1]` ; séparer ETX, rang RPL et scores normalisés de visualisation ; vérifier connectivité, sélection de parents, hops, PDR, délai, énergie et convergence.

### C3 — Intégration NS-3 non fonctionnelle

**Sévérité : Critique**

Dans [marthr-routing-protocol.cc](../ns3_setup/marthr-routing-protocol.cc#L36-L51), `RouteInput()` met à jour les métriques puis retourne toujours `false`. Dans [marthr-routing-protocol.cc](../ns3_setup/marthr-routing-protocol.cc#L53-L60), `BuildRoute()` utilise une gateway `0.0.0.0` et ne sélectionne aucun parent, ne consulte pas la table de trust et ne calcule pas de route selon le rang. Les valeurs `trust=0.8`, `energy=0.7` et `qos=0.9` sont codées en dur dans [marthr-routing-protocol.cc](../ns3_setup/marthr-routing-protocol.cc#L62-L73).

Le README précise qu’il s’agit d’un scaffold à intégrer dans un vrai workspace NS-3 : [README_NS3_MARTHR.md](../ns3_setup/README_NS3_MARTHR.md#L3-L10).

**Correction :** présenter NS-3 comme prototype non fonctionnel jusqu’à l’implémentation de la découverte de voisins, sélection de parent, calcul de rang, forwarding, routes, métriques et traces CSV. Ajouter un scénario exécutable et un test de livraison de paquets.

### C4 — Figures de résultats non reliées de manière fiable aux données

**Sévérité : Critique**

Le manuscrit présente comparaison MARTHR/MRHOF, détection, Pareto et overhead dans [main.tex](../manuscript/main.tex#L235-L247) et [main.tex](../manuscript/main.tex#L386-L418). Pourtant [regenerate_tables.py](../scripts/regenerate_tables.py#L19-L22) et [compare_with_baseline.py](../scripts/compare_with_baseline.py#L4-L17) refusent de produire une comparaison MRHOF indépendante, tandis que les figures d’overhead et de détection reposent sur des constantes.

**Correction :** créer un manifeste figure/table → source → script → statut ; supprimer du manuscrit les figures sans source expérimentale traçable.

## 2. Manuscrit

### Affirmations insuffisamment supportées

- « Complete implementation in C and C++ » dans [main.tex](../manuscript/main.tex#L23-L31) : remplacer par prototype C portable et scaffold NS-3 initial.
- « Outperforming MRHOF » dans [main.tex](../manuscript/main.tex#L23-L31) : retirer tant qu’une comparaison valide n’est pas produite.
- « Attack detection performance » dans [main.tex](../manuscript/main.tex#L398-L407) : les valeurs sont codées en dur.
- « Pareto frontier » dans [main.tex](../manuscript/main.tex#L409-L418) : aucune optimisation multi-objectifs démontrée ne produit les points.
- « Twenty seeds per scenario » : la configuration à 20 graines ne compense pas les baselines invalides, les scénarios non comparables ou la dépendance des observations.

### H1 — Ablation non contrôlée

**Sévérité : Haute**

[regenerate_tables.py](../scripts/regenerate_tables.py#L52-L96) utilise des scénarios différents pour `Full MARTHR`, `w/o Trust`, `w/o Energy` et `w/o QoS` : topologie, durée, pertes, mobilité, énergie et menaces varient simultanément. Le manuscrit le reconnaît partiellement dans [main.tex](../manuscript/main.tex#L344-L365), mais conserve une présentation d’évaluation expérimentale.

**Correction :** même topologie, mobilité, graines, pertes, trafic et durée ; désactiver un seul composant à la fois.

### M6 — Portée RPL/MANET insuffisamment stabilisée

**Sévérité : Moyenne**

Le manuscrit associe MANET, RPL, DODAG, OCP, MRHOF, NS-3 et Contiki-NG dans [main.tex](../manuscript/main.tex#L42-L72) et [main.tex](../manuscript/main.tex#L171-L185). RPL/MRHOF ciblent les LLN, tandis que le projet est aussi présenté comme protocole MANET général.

**Correction :** choisir une portée principale : Objective Function RPL pour LLN, protocole MANET, ou architecture générique avec validations séparées.

### B1 — Section dupliquée

**Sévérité : Basse**

[main.tex](../manuscript/main.tex#L105-L120) contient deux déclarations successives de `\section{Protocol Design}`.

**Correction :** supprimer le doublon et vérifier les signets PDF.

## 3. Code source

### H2 — Modèles de trust divergents

**Sévérité : Haute**

Le simulateur principal initialise un nœud inconnu à `0.5` et pénalise un échec de `0.15` dans [marthr_simulator.py](../scripts/marthr_simulator.py#L43-L65). [marthr_core.py](../code_source/marthr_core.py#L47-L70) retourne `0.0` pour un inconnu et applique une pénalité multiplicative `trust_score * 0.8`. Le C utilise `0.5` et une pénalité additive dans [marthr_trust.c](../code_source/marthr_trust.c#L31-L37) et [marthr_trust.c](../code_source/marthr_trust.c#L70-L73), tandis que NS-3 retourne `0.5` dans [marthr-trust-table.cc](../ns3_setup/marthr-trust-table.cc#L99-L105).

**Correction :** définir une spécification normative unique et ajouter des tests croisés C/Python/NS-3.

### H3 — Modèles de poids divergents

**Sévérité : Haute**

Les poids C/Python suivent l’architecture documentée dans [ARCHITECTURE_SPEC.md](../ARCHITECTURE_SPEC.md#L8-L17), [marthr_context.c](../code_source/marthr_context.c#L8-L28) et [marthr_simulator.py](../scripts/marthr_simulator.py#L18-L45). NS-3 initialise `0.35`, `0.33`, `0.32` et applique des ajustements différents dans [marthr-context.cc](../ns3_setup/marthr-context.cc#L19-L58).

**Correction :** centraliser les poids et tester quatre niveaux de sécurité, trois niveaux de menace et trois états énergétiques dans toutes les implémentations.

### H4 — Calcul du rang tronqué

**Sévérité : Haute**

Le rang `1 - MCS + 0.1 × hop_count` est borné à `[0,1]` dans [marthr_rank.c](../code_source/marthr_rank.c#L4-L18) et [marthr_simulator.py](../scripts/marthr_simulator.py#L136-L147). Pour plusieurs hops, la pénalité est aplatie à `1`.

**Correction :** conserver un rang non borné ou séparer rang interne et score normalisé ; tester la monotonicité avec le nombre de hops.

### H5 — Sélection de parent dépendante de l’ordre

**Sévérité : Haute**

Dans [marthr_simulator.py](../scripts/marthr_simulator.py#L177-L218), les voisins sont parcourus séquentiellement et le parent est remplacé dès qu’un candidat améliore le rang. `best_neighbor` ne conserve pas réellement le meilleur candidat global.

**Correction :** évaluer tous les voisins, filtrer les parents invalides, choisir le meilleur rang puis appliquer l’hystérésis une seule fois.

### H6 — Absence de contrainte DAG et de détection de cycles

**Sévérité : Haute**

Dans [marthr_simulator.py](../scripts/marthr_simulator.py#L177-L195), la sélection ne vérifie pas que le rang du parent est strictement inférieur à celui du nœud et ne valide pas le DAG.

**Correction :** imposer un parent strictement meilleur, détecter les cycles après chaque mise à jour et tester automatiquement la connectivité vers la racine pour chaque seed et timestamp.

### M4 — Métriques proxy présentées comme métriques réseau

**Sévérité : Moyenne**

Dans [marthr_simulator.py](../scripts/marthr_simulator.py#L228-L244), `qos_latency` vaut `1.0 - last_mcs` et non une latence mesurée ; `mcs` est le dernier score du parent courant. [README_DATA_PROVENANCE.md](../data/README_DATA_PROVENANCE.md#L26-L40) les décrit pourtant comme métriques de simulation générales.

**Correction :** renommer en métriques proxy ou mesurer délai d’émission/réception, délai bout-en-bout, moyenne, p95 et p99.

### M5 — Phénomènes réseau annoncés non réellement simulés

**Sévérité : Moyenne**

Le scénario d’attaque de [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L86-L116) force surtout des mises à jour de trust ; il ne mesure pas suppression de paquets, faux rapports de rang, PDR, détection ou faux positifs. Le scénario mobilité de [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L150-L180) déplace les coordonnées sans trafic ni paquets.

**Correction :** modéliser paquets envoyés/reçus/supprimés, retransmissions, messages de contrôle, détection, faux positifs et faux négatifs.

### B2 — Binaires compilés dans les tests

**Sévérité : Basse**

Le dossier [code_source/tests](../code_source/tests) contient des exécutables compilés (`test_marthr_core`, `test_marthr_rank`, `test_marthr_ablation`, `test_marthr_ocp`) avec les sources.

**Correction :** ignorer les binaires dans Git et les reconstruire dans le pipeline.

## 4. Données

### H8 — Provenance incomplète et absence de traces brutes

**Sévérité : Haute**

[README_DATA_PROVENANCE.md](../data/README_DATA_PROVENANCE.md#L5-L24) décrit des logs bruts et des CSV estimés, mais `data/raw/` contient principalement `marthr_sample.csv`. Les campagnes sont écrites directement dans `data/estimated/simulations/` par [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L20-L47), sans logs bruts correspondants.

Le document affirme que les données brutes sont immuables, alors que [generate_sample_dataset.py](../scripts/generate_sample_dataset.py#L77-L95) réécrit le fichier d’exemple. Il indique aussi que le trust est toujours nul, alors que les campagnes présentent des valeurs non nulles.

**Correction :** distinguer données générées, brutes, dérivées et pédagogiques ; archiver version, dépendances, configuration, seed, hash et provenance de chaque sortie ; corriger la documentation du trust.

### M1 — CSV et tableaux LaTeX incohérents

**Sévérité : Moyenne**

[table2_ablation.csv](../data/estimated/table2_ablation.csv#L2-L5) et [ablation_table.tex](../manuscript/tables/ablation_table.tex#L10-L15) contiennent des valeurs différentes, notamment pour l’énergie de `w/o Trust proxy`, le trust et l’énergie de `w/o QoS proxy`, et le MCS.

**Correction :** générer les `.tex` depuis les CSV et ajouter une vérification automatique CSV ↔ LaTeX.

### M2 — Nombre de campagnes contradictoire

**Sévérité : Moyenne**

[README_DATA_PROVENANCE.md](../data/README_DATA_PROVENANCE.md#L5-L9) décrit 8 scénarios, tandis que [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L256-L286) lance 8 scénarios MARTHR et 3 campagnes MRHOF mais annonce seulement `len(results)/8`.

**Correction :** distinguer 8 scénarios MARTHR, 3 campagnes baseline et 11 campagnes totales ; vérifier les fichiers attendus.

## 5. Reproductibilité

### H7 — Tests statistiques annoncés mais non exécutés

**Sévérité : Haute**

Le manuscrit affirme l’utilisation de Mann–Whitney dans [main.tex](../manuscript/main.tex#L220-L229), mais `baseline_mrhof()` lève une exception dans [analyze_metrics.py](../scripts/statistics/analyze_metrics.py#L40-L50). La fonction statistique existe, mais le pipeline actuel ne produit pas de comparaison valide ni ne vérifie les p-values.

**Correction :** exécuter effectivement les tests au niveau indépendant approprié, rapporter U, p-value, taille d’effet, intervalle de confiance et corrections pour comparaisons multiples ; ne pas traiter toutes les observations node×time comme réplicats indépendants.

### M3 — Reproduction insuffisamment validée

**Sévérité : Moyenne**

[reproduce_project.py](../scripts/reproduce_project.py#L38-L60) vérifie surtout l’existence des fichiers et ne vérifie pas le nombre de seeds, valeurs manquantes, bornes, connectivité, cycles, parents, cohérence scénarios, figures/tableaux ou tests statistiques.

**Correction :** ajouter des contrôles bloquants sur les seeds, lignes, colonnes, bornes, nœuds sans parent, cycles, reproductibilité et sorties attendues.

### Limites de vérification

Les éléments suivants n’ont pas été confirmés par exécution complète pendant l’audit : compilation C avec `make`, exécution complète de [reproduce_project.py](../scripts/reproduce_project.py), compilation LaTeX avec `latexmk`, compilation NS-3 dans une distribution complète, résultats des tests unitaires, validité externe des références arXiv, comparaison binaire des PDF et intégrité exhaustive de tous les CSV.

## 6. Figures et tableaux

La traçabilité figure → données → script n’est pas garantie. Les figures de contexte, overhead, détection et Pareto doivent être séparées entre schémas conceptuels et résultats expérimentaux. Les tableaux LaTeX doivent être régénérés automatiquement depuis les CSV et contrôlés avant chaque compilation.

## 7. Bibliographie

### B3 — Bibliographie à valider avec la cible IEEE

**Sévérité : Basse à Moyenne**

[references.bib](../manuscript/bib/references.bib) contient des entrées `@rfc` dont la compatibilité exacte avec IEEEtran n’a pas été confirmée par compilation. Plusieurs références arXiv de 2025–2026 doivent aussi être vérifiées indépendamment.

**Correction :** compiler avec BibTeX et traiter tous les warnings ; vérifier DOI, URL, titre, auteurs, pages et statut de publication ; ne pas présenter les prépublications comme état de l’art établi sans préciser leur statut.

## 8. Actions de correction recommandées

### Priorité 0 — Avant toute revendication expérimentale

1. Retirer ou marquer comme illustratives les figures produites par constantes.
2. Corriger ou retirer la comparaison MRHOF.
3. Corriger le baseline ETX/rang.
4. Clarifier que NS-3 est un scaffold.
5. Retirer du résumé les revendications de supériorité et de détection non démontrées.

### Priorité 1 — Rendre l’évaluation valide

1. Implémenter une campagne baseline fonctionnelle.
2. Créer des ablations contrôlées.
3. Produire PDR, délai, overhead, énergie et détection à partir d’événements réseau réels.
4. Agréger par seed, pas seulement par ligne node×time.
5. Exécuter et archiver les tests statistiques.
6. Ajouter un contrôle de cycles et de connectivité.

### Priorité 2 — Réconcilier les implémentations

1. Unifier poids, trust et conventions de rang entre C, Python et NS-3.
2. Ajouter des tests de conformité inter-implémentations.
3. Régénérer tous les tableaux et figures depuis une chaîne de données unique.

### Priorité 3 — Nettoyer la reproductibilité

1. Ajouter la provenance complète des données.
2. Distinguer données brutes, estimées, synthétiques et illustratives.
3. Ajouter un manifeste figure/table.
4. Ajouter les versions des dépendances et de l’environnement.
5. Faire échouer le pipeline si une sortie attendue est absente ou incohérente.

## Verdict final

**Statut actuel : prototype prometteur, mais non publiable comme étude expérimentale comparative sans corrections majeures.**

Le principal risque scientifique est la confusion entre prototype algorithmique, simulation synthétique, baseline expérimentale, scaffold NS-3, figures illustratives et résultats de campagne. Après correction des quatre anomalies critiques et des problèmes de baseline, d’ablation, de provenance et de cohérence inter-implémentations, le projet pourrait devenir une base reproductible pour une évaluation scientifique sérieuse.
