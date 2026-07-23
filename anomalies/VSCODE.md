# Audit global MARTHR — Ré-audit du 23 juillet 2026

**Périmètre :** dépôt `/home/madani/MARTHR`  
**Méthodologie :** [METHODOLOGIE_EVALUATION.md](METHODOLOGIE_EVALUATION.md)  
**Filtres :** [message-IA.md](message-IA.md)  
**Mode :** lecture seule ; aucun fichier du projet n’a été modifié pendant l’audit.

Les commentaires français, les dossiers d’audit et les trackers internes ont été exclus conformément aux instructions.

## Résumé exécutif

| Sévérité | Nombre |
|----------|-------:|
| Critique | 3 |
| Haute | 7 |
| Moyenne | 6 |
| Basse | 3 |

Le projet a progressé depuis l’audit précédent : les modules C sont présents, les campagnes MARTHR et MRHOF sont archivées, le clamp ETX `[0,1]` a été retiré et le doublon de section du manuscrit a été corrigé. L’ablation est également reconnue explicitement comme non contrôlée.

Le projet ne constitue toutefois toujours pas une évaluation comparative publiable. Les blocages principaux sont : figures encore alimentées par des constantes, baseline MRHOF et analyse statistique incomplètes, pipeline de reproduction non fiable, ablation non contrôlée, tableaux CSV/LaTeX divergents, incohérences C/Python/NS-3 et scaffold NS-3 non fonctionnel.

**Verdict :** prototype algorithmique intéressant, mais non publiable comme étude comparative expérimentale en l’état.

## 1. État des corrections depuis l’audit précédent

### Corrections ou améliorations confirmées

- Les modules C de contexte, confiance, score, rang, OCP et journalisation sont présents dans [code_source](../code_source), avec un [Makefile](../code_source/Makefile#L1-L20) et des tests.
- Le script de campagne [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L1-L49) prévoit 20 seeds et les sorties contiennent huit campagnes MARTHR et trois campagnes MRHOF.
- [estimate_etx()](../scripts/marthr_simulator.py#L365-L370) retourne maintenant $1/\mathrm{PRR}$ sans clamp supérieur à 1.
- Le doublon de section `Protocol Design` n’est plus présent dans [main.tex](../manuscript/main.tex#L101-L103).
- La limitation méthodologique de l’ablation est reconnue dans [main.tex](../manuscript/main.tex#L361-L370).

### Corrections insuffisantes

La correction du clamp ETX élimine l’anomalie locale, mais ne rend pas la baseline comparable : sélection dépendante de l’ordre, absence de validation DAG, métriques différentes et pipeline statistique cassé subsistent.

## 2. Anomalies critiques

### C1 — Figures scientifiques encore générées par constantes codées en dur

**Statut : encore présent.**

Dans [generate_missing_figures.py](../scripts/generate_missing_figures.py#L80-L161), les figures utilisent directement :

- `weights = [0.48, 0.35, 0.17]` ;
- les coordonnées `x` et `y` d’une frontière de Pareto ;
- `overhead = [0.08, 0.11, 0.16, 0.19]` ;
- `detection = [0.71, 0.77, 0.91, 0.88]`.

Le script ne charge aucun CSV de campagne pour ces sorties, référencées notamment dans [main.tex](../manuscript/main.tex#L125-L143) et [main.tex](../manuscript/main.tex#L316-L344).

**Conséquence :** l’overhead, la détection et la frontière de Pareto ne sont pas traçables vers une expérience. Les valeurs doivent être considérées comme illustratives, et non comme résultats expérimentaux.

**Action :** relier chaque figure à un CSV, un script, des paramètres et des seeds ; supprimer ou requalifier les figures hardcodées ; produire un manifeste figure → données → commande.

### C2 — Baseline MRHOF non intégrée correctement

**Statut : encore présent, malgré la correction ETX.**

Dans [marthr_simulator.py](../scripts/marthr_simulator.py#L314-L352), la sélection du parent est séquentielle et ne garantit pas explicitement un minimum global parmi tous les candidats. MARTHR et MRHOF ne vérifient pas non plus qu’un parent possède un rang strictement inférieur, qu’il est connecté à la racine ou qu’aucun cycle n’est introduit.

La baseline écrit `trust = 0.0`, `mcs = 1.0 - etx` et un `qos_latency` dérivé dans [marthr_simulator.py](../scripts/marthr_simulator.py#L386-L390). Ces colonnes ne sont donc pas des métriques communes directement comparables avec MARTHR.

En outre, `baseline_mrhof()` utilise `self.simulations_dir`, attribut non initialisé dans [analyze_campaigns.py](../scripts/analyze_campaigns.py#L40-L63), alors que le constructeur initialise `self.campaign_dir`.

**Conséquence :** les comparaisons MRHOF et les tests de Mann–Whitney ne sont pas démontrés.

**Action :** réparer le chargement, comparer seulement des métriques communes, utiliser les mêmes scénarios/seeds/topologies/durées, sélectionner le meilleur parent indépendamment de l’ordre, vérifier le DAG et agréger par seed avant les tests.

### C3 — Pipeline de reproduction non fiable

**Statut : encore présent.**

[reproduce_project.py](../scripts/reproduce_project.py#L12-L30) enchaîne campagne, tables, dataset d’exemple, statistiques, analyse et figures. Il appelle notamment [analyze_campaigns.py](../scripts/reproduce_project.py#L20-L24), dont la baseline est défectueuse.

Les contrôles de [reproduce_project.py](../scripts/reproduce_project.py#L32-L56) vérifient seulement un sous-ensemble des sorties et ne contrôlent pas seeds, valeurs manquantes, bornes, connectivité, cycles, cohérence des scénarios, CSV ↔ LaTeX, statistiques ou provenance des figures.

Le pipeline peut aussi réécrire [data/raw/marthr_sample.csv](../data/raw/marthr_sample.csv) via [generate_sample_dataset.py](../scripts/generate_sample_dataset.py#L63-L83), alors que [README_DATA_PROVENANCE.md](../data/README_DATA_PROVENANCE.md#L64-L67) décrit les données brutes comme immuables.

**Action :** séparer les données brutes et synthétiques, ajouter des répertoires de sortie et options de saut, arrêter le pipeline sur erreur, générer des métadonnées par campagne et tester deux exécutions indépendantes.

## 3. Manuscrit

### H1 — Ablation non contrôlée

**Sévérité : Haute — statut : reconnue, mais non corrigée méthodologiquement.**

[regenerate_tables.py](../scripts/regenerate_tables.py#L48-L96) compare des campagnes qui changent simultanément topologie, durée, pertes, mobilité, énergie, menace, contexte et nombre potentiel de nœuds : lossless pour le modèle complet, lossy sans trust, energy stress sans énergie et mobility sans QoS.

Le MCS de `w/o QoS` est supérieur à celui de Full MARTHR dans [ablation_table.tex](../manuscript/tables/ablation_table.tex#L10-L15), mais cela ne permet aucune conclusion causale puisque les scénarios diffèrent.

**Action :** conserver mêmes scénario, topologie, seeds, trafic, durée et liens ; désactiver un seul terme du MCS à la fois.

### H4 — `qos_latency` n’est pas une latence réseau mesurée

**Sévérité : Haute.**

La valeur enregistrée dans [marthr_simulator.py](../scripts/marthr_simulator.py#L292-L306) est principalement `last_qos`, ou `1.0 - last_mcs`. Elle ne mesure ni timestamps émission/réception, ni délai bout en bout, ni moyenne ou percentile. Pourtant la figure est nommée `Latency Comparison` dans [main.tex](../manuscript/main.tex#L292-L300), avec une conclusion sur la latence à [main.tex](../manuscript/main.tex#L302-L304).

**Action :** mesurer une vraie latence ou renommer la colonne en `qos_proxy` et retirer les claims de latence.

### H7 — Claims plus forts que les preuves

Les formulations suivantes dépassent les résultats actuellement démontrés :

- « complete implementation in C » à [main.tex](../manuscript/main.tex#L25-L31) ;
- « proper statistical analysis » à [main.tex](../manuscript/main.tex#L31-L36) ;
- performance de détection d’attaque à [main.tex](../manuscript/main.tex#L336-L344) ;
- routes autour de nœuds compromis à [main.tex](../manuscript/main.tex#L342-L344) ;
- espace de compromis Pareto à [main.tex](../manuscript/main.tex#L350-L358) ;
- décisions plus équilibrées que la baseline à [main.tex](../manuscript/main.tex#L314-L318).

Ces claims ne sont pas supportés par des traces de paquets, une baseline valide, une optimisation Pareto, une mesure d’overhead ou une mesure de détection.

**Action :** soit produire les expériences manquantes, soit présenter honnêtement le manuscrit comme une proposition accompagnée d’une simulation exploratoire.

## 4. Code source et implémentations

### H2 — Incohérences Python, C et NS-3

**Sévérité : Haute.**

#### Confiance inconnue

- Python retourne `0.5` dans [marthr_simulator.py](../scripts/marthr_simulator.py#L80-L83).
- C retourne `0.0` dans [marthr_trust.c](../code_source/marthr_trust.c#L97-L104).
- NS-3 retourne `0.5` dans [marthr-trust-table.cc](../ns3_setup/marthr-trust-table.cc#L104-L110).

#### Poids

C et Python partent notamment de `0.35/0.40/0.25` dans [marthr_context.c](../code_source/marthr_context.c#L8-L23) et [marthr_simulator.py](../scripts/marthr_simulator.py#L22-L43). NS-3 part de `0.35/0.33/0.32` et applique une logique différente dans [marthr-context.cc](../ns3_setup/marthr-context.cc#L19-L78). C/Python ne normalisent que si la somme dépasse 1, tandis que NS-3 normalise systématiquement si la somme est positive.

#### Rang

C/Python calculent $1-\mathrm{MCS}+0.1h$ dans [marthr_rank.c](../code_source/marthr_rank.c#L4-L15) et [marthr_simulator.py](../scripts/marthr_simulator.py#L130-L143). NS-3 utilise directement le MCS et considère qu’un rang plus élevé est meilleur dans [marthr-rank.cc](../ns3_setup/marthr-rank.cc#L27-L50).

#### OCP C

[marthr_ocp.c](../code_source/marthr_ocp.c#L25-L41) utilise `metric->rank` comme nombre de hops, alors que [marthr_rank.c](../code_source/marthr_rank.c#L4-L15) reçoit explicitement `hop_count`.

**Action :** définir une spécification normative commune et des vecteurs de tests partagés couvrant confiance, poids, normalisation, rang, hops et sens de comparaison.

### H3 — Scaffold NS-3 non fonctionnel comme protocole de routage

**Sévérité : Haute — statut : encore présent mais correctement documenté comme scaffold.**

Le README indique explicitement un scaffold dans [README_NS3_MARTHR.md](../ns3_setup/README_NS3_MARTHR.md#L1-L10). Dans [marthr-routing-protocol.cc](../ns3_setup/marthr-routing-protocol.cc#L42-L76) :

- `RouteInput()` retourne toujours `false` ;
- `BuildRoute()` utilise la gateway `0.0.0.0` ;
- `UpdateMetrics()` utilise `trust=0.8`, `energy=0.7`, `qos=0.9` ;
- la table de confiance et le rang ne sélectionnent ni parent ni forwarding.

**Action :** ne pas présenter NS-3 comme validation ; implémenter découverte, métriques de liens, sélection de parent, rang, forwarding, routes IPv4, traces et scénario exécutable.

### H5 — Attaques et mobilité non simulées au niveau paquets

**Sévérité : Haute.**

Le scénario d’attaque modifie directement les tables de confiance dans [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L86-L116), sans paquets envoyés, reçus ou supprimés, ni taux de détection, faux positifs ou faux négatifs. La mobilité déplace les coordonnées dans [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L150-L180), sans trafic ni livraison bout en bout.

**Action :** introduire un modèle événementiel de trafic et distinguer confiance, détection, PDR et sélection de route.

### M5 — Rang aplati par clamp

**Sévérité : Moyenne.**

Le rang $1-\mathrm{MCS}+0.1h$ est borné à 1 dans [marthr_simulator.py](../scripts/marthr_simulator.py#L130-L143) et [marthr_rank.c](../code_source/marthr_rank.c#L4-L15). Pour des chemins longs, la pénalité de saut disparaît et des chemins différents peuvent recevoir `1.0`.

**Action :** séparer rang interne non borné et score normalisé d’affichage, ou adopter une échelle conforme à RPL.

## 5. Données

### M1 — CSV et tableaux LaTeX incohérents

**Sévérité : Moyenne.**

[table2_ablation.csv](../data/estimated/table2_ablation.csv#L1-L5) indique notamment `w/o Trust` avec énergie `0.0001` et MCS `0.6247`, ainsi que `w/o QoS` avec énergie `0.5146` et MCS `0.7042`. [ablation_table.tex](../manuscript/tables/ablation_table.tex#L10-L15) affiche respectivement énergie `0.0872`, MCS `0.6245`, énergie `0.5501` et MCS `0.7044`.

Le tableau [results_table.tex](../manuscript/tables/results_table.tex#L8-L15) diverge aussi des valeurs de l’abstract dans [main.tex](../manuscript/main.tex#L25-L31).

**Action :** générer les `.tex` depuis une source CSV unique et ajouter un test CSV ↔ LaTeX.

### M2 — Provenance contradictoire

**Sévérité : Moyenne.**

[README_DATA_PROVENANCE.md](../data/README_DATA_PROVENANCE.md#L5-L12) annonce huit scénarios et 20 seeds, décrit un dataset d’exemple de 288 lignes et affirme que les données brutes sont immuables. Pourtant [generate_sample_dataset.py](../scripts/generate_sample_dataset.py#L11-L62) régénère directement [marthr_sample.csv](../data/raw/marthr_sample.csv) à partir de trois scénarios, et les campagnes écrivent directement dans `data/estimated/simulations` sans logs bruts ni configuration JSON versionnée.

**Action :** séparer `raw`, `synthetic`, `estimated` et `illustrative`, puis ajouter version, paramètres, seed, hash, date et dépendances.

### M3 — Nombre de campagnes annoncé incorrect

**Sévérité : Moyenne.**

La liste contient huit campagnes MARTHR et trois MRHOF dans [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L248-L266), mais le message final affiche `len(results)/8` dans [run_simulation_campaign.py](../scripts/run_simulation_campaign.py#L274-L278).

**Action :** afficher séparément réussites MARTHR, réussites MRHOF, total et échecs.

### M4 — Agrégation statistique fragile

Les moyennes sont calculées sur des lignes pouvant mélanger nœuds, timestamps et seeds dans [regenerate_tables.py](../scripts/regenerate_tables.py#L20-L43). La sélection du dernier timestamp est globale dans [regenerate_tables.py](../scripts/regenerate_tables.py#L52-L76), ce qui est fragile pour des campagnes de durées différentes.

**Action :** définir l’unité expérimentale, agréger nœud → seed → scénario, puis rapporter intervalles de confiance et tailles d’effet.

## 6. Reproductibilité

| Élément | État |
|---|---|
| Structure du dépôt | Présente et relativement claire |
| Simulateur Python | Cohérent à la lecture statique, exécution non confirmée |
| Baseline MRHOF | Présente, mais comparaison incomplète et analyse cassée |
| Modules et tests C | Présents, compilation/exécution non confirmées |
| Scaffold NS-3 | Présent, non intégré dans un workspace NS-3 |
| Campagnes CSV | Présentes, provenance incomplète |
| Figures issues de CSV | Traçabilité partielle |
| Figures hardcodées | Toujours présentes |
| Tables CSV → LaTeX | Divergentes |
| Mann–Whitney | Annoncé, mais pipeline défectueux |
| Reproduction bout en bout | Non démontrée |

Les vérifications effectuées sont statiques : inventaire, lecture des fichiers clés, comparaison des formules, inspection des CSV/tableaux, recherche de constantes et de claims sensibles. Les commandes `python3 scripts/reproduce_project.py`, `make`, tests C, `pdflatex`/`latexmk`, compilation NS-3 et campagne complète n’ont pas été exécutées dans cet audit ; elles sont donc **non vérifiées**, et non considérées comme réussies.

## 7. Figures et tableaux

Les figures de comparaison, énergie, confiance, rang et ablation existent, ainsi que les figures PNG d’architecture, contexte, DODAG, Pareto, overhead et détection. Leur présence ne garantit pas leur validité scientifique.

[generate_ieee_figures.py](../scripts/generate_ieee_figures.py#L1-L39) lit certains CSV, mais ne vérifie pas systématiquement les colonnes obligatoires ; plusieurs écarts-types calculés ne sont pas utilisés ; la figure d’ablation utilise la complexité des scénarios dans [generate_ieee_figures.py](../scripts/generate_ieee_figures.py#L163-L190) ; la figure de latence utilise `ax.legend()` sans série explicitement étiquetée dans [generate_ieee_figures.py](../scripts/generate_ieee_figures.py#L119-L142). Les figures supplémentaires restent hardcodées dans [generate_missing_figures.py](../scripts/generate_missing_figures.py#L80-L161).

## 8. Bibliographie

### B1 — Métadonnées et statut des références à vérifier

**Sévérité : Basse.**

[references.bib](../manuscript/bib/references.bib#L1-L140) contient des références historiques pertinentes et plusieurs prépublications arXiv. Il manque souvent DOI, statut de publication et vérification systématique des métadonnées. La référence MRHOF est décrite comme `RPL Objective Function 0` dans [references.bib](../manuscript/bib/references.bib#L24-L30), alors que le manuscrit l’utilise comme baseline MRHOF.

**Action :** vérifier les sources primaires, DOI, titres, auteurs et statut RFC/article/preprint ; distinguer clairement ces catégories.

### B2 — Artefacts générés non distingués des sources

**Sévérité : Basse.**

Le dépôt contient des auxiliaires LaTeX et de nombreuses figures générées sans manifeste reliant systématiquement chaque artefact à son script et à ses données.

**Action :** documenter le statut de chaque artefact et exclure les sorties intermédiaires régénérables du suivi.

### B3 — Tests C insuffisants pour la conformité scientifique

**Sévérité : Basse.**

Les tests [test_marthr_core.c](../code_source/tests/test_marthr_core.c#L1-L66) et [test_marthr_rank.c](../code_source/tests/test_marthr_rank.c#L1-L60) vérifient surtout l’absence de crash, les bornes et quelques cas simples. Ils ne couvrent pas la conformité C ↔ Python, les contextes complets, les cycles, la capacité de table, la monotonicité des hops ni les sorties CSV.

## 9. Actions de correction prioritaires

### Priorité 0 — Avant toute soumission

1. Supprimer ou requalifier les figures hardcodées.
2. Réparer ou retirer la comparaison MRHOF.
3. Corriger `baseline_mrhof()` et ajouter des tests d’exécution.
4. Régénérer les tableaux depuis les CSV courants.
5. Renommer `qos_latency` ou mesurer une vraie latence.
6. Retirer les claims de détection, overhead et Pareto non démontrés.
7. Requalifier précisément le C et NS-3.

### Priorité 1 — Évaluation scientifique

1. Utiliser une baseline MRHOF réellement comparable.
2. Conserver mêmes scénarios, seeds, topologies et durées.
3. Implémenter une ablation à facteur unique.
4. Produire PDR, délai, overhead, énergie et détection à partir d’événements réseau.
5. Agréger par seed et rapporter p-values, tailles d’effet et intervalles de confiance.
6. Ajouter détection de cycles et vérification de connectivité.

### Priorité 2 — Conformité inter-implémentations

1. Définir une spécification normative unique.
2. Unifier confiance inconnue, poids, normalisation, rang, hops et sens de comparaison.
3. Ajouter des vecteurs de test partagés Python/C/NS-3.

### Priorité 3 — Reproductibilité

1. Séparer données brutes, synthétiques, estimées et illustratives.
2. Ajouter configuration, version, hash et seed à chaque campagne.
3. Faire échouer le pipeline dès qu’une sortie ou colonne est incohérente.
4. Ajouter un manifeste figure/table.
5. Exécuter deux reproductions complètes dans un environnement propre.
6. Compiler le manuscrit depuis zéro et archiver le log.

## 10. Verdict final

**Statut au 23 juillet 2026 : prototype prometteur, mais non publiable comme étude expérimentale comparative.**

Les corrections récentes ont amélioré la structure, restauré les composants C, ajouté les campagnes et corrigé le calcul ETX. Elles n’ont pas résolu les points déterminants : figures partiellement hardcodées, baseline MRHOF non démontrée, pipeline statistique cassé, ablation non contrôlée, incohérences CSV–LaTeX, divergences C–Python–NS-3, métriques QoS proxy et scaffold NS-3 non fonctionnel comme protocole de routage.

Le projet peut devenir une contribution crédible après une révision expérimentale et reproductible substantielle.
