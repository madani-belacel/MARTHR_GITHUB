J'ai effectué un audit du **manuscrit PDF** que vous avez fourni. L'analyse ci-dessous est **fondée uniquement sur le contenu du manuscrit**, sans inspection du code source ni des données CSV. Les remarques concernant la reproductibilité ou la cohérence avec le code sont donc limitées à ce qui est affirmé dans le document.

# Audit global du manuscrit MARTHR

## Résumé exécutif

| Sévérité | Nombre |
| -------- | -----: |
| Critique |      5 |
| Haute    |      8 |
| Moyenne  |     11 |
| Basse    |      8 |

**Évaluation globale**

Le manuscrit présente une idée intéressante : un protocole de routage MANET multi-critères combinant confiance, énergie et QoS avec adaptation contextuelle. La structure générale est conforme à un article IEEE, mais plusieurs points empêchent actuellement une soumission solide :

* plusieurs affirmations expérimentales restent insuffisamment démontrées ;
* l'étude expérimentale demeure limitée ;
* certaines références bibliographiques méritent une vérification approfondie ;
* quelques incohérences de rédaction et de structure sont présentes.

Je situerais actuellement ce manuscrit au niveau **"révision majeure"** avant une soumission IEEE.

---

# Points forts

## 1. Sujet pertinent

Le problème traité est actuel :

* MANET
* sécurité
* confiance
* efficacité énergétique
* QoS

L'objectif scientifique est clair. 

---

## 2. Contribution bien identifiée

Les quatre contributions sont clairement énoncées :

* MCS
* adaptation contextuelle
* implémentation C
* pipeline reproductible



---

## 3. Formulation mathématique

Les équations sont simples et cohérentes :

* score MCS
* confiance
* decay
* rank
* hysteresis



---

## 4. Discussion honnête des limites

Le manuscrit reconnaît explicitement plusieurs limites (absence de testbed réel, intégration future avec Contiki-NG et NS-3, etc.), ce qui renforce sa crédibilité. 

---

# Anomalies critiques

## C1 — Le manuscrit ne comporte que 7 pages

Le PDF comporte 7 pages. Or un article IEEE complet vise généralement au moins 8 pages selon votre objectif de soumission.

Impact :

* faible maturité perçue
* espace insuffisant pour détailler l'évaluation

---

## C2 — Comparaison expérimentale insuffisante

Le manuscrit compare essentiellement MARTHR à MRHOF. 

Une comparaison expérimentale avec plusieurs protocoles (par exemple AODV, OLSR, DSR ou d'autres protocoles de confiance) renforcerait considérablement la valeur scientifique.

---

## C3 — Les revendications sont prudentes mais parfois peu démontrées

Le texte affirme notamment :

* meilleure résilience,
* décisions plus équilibrées,
* meilleure efficacité énergétique.

Cependant, les résultats présentés restent essentiellement descriptifs. 

Il manque des preuves quantitatives plus solides (tests de significativité effectivement rapportés, tailles d'effet, intervalles de confiance, etc.).

---

## C4 — Étude d'ablation non contrôlée

Le manuscrit indique lui-même que l'étude d'ablation repose sur des scénarios proxy et **ne constitue pas une véritable étude contrôlée**.  

Pour une publication IEEE, une ablation contrôlée est préférable.

---

## C5 — Reproductibilité affirmée mais non démontrée dans le manuscrit

Le texte mentionne un pipeline reproductible. 

Le manuscrit ne fournit cependant pas suffisamment d'éléments (versions logicielles, environnement, paramètres détaillés) pour qu'un lecteur puisse reproduire les résultats à partir du document seul.

---

# Anomalies de sévérité haute

## H1 — Double titre de section

Les sections suivantes apparaissent successivement :

* III. Protocol Design
* IV. Protocol Design



Il s'agit vraisemblablement d'une erreur de structuration.

---

## H2 — Évaluation limitée

Huit scénarios sont présentés, mais il manque des analyses sur :

* différentes densités de réseau,
* diverses mobilités,
* tailles de réseau supérieures,
* différents modèles radio.



---

## H3 — Analyse statistique incomplète

Le manuscrit indique l'utilisation du test de Mann–Whitney. 

En revanche, il ne présente pas les p-values, intervalles de confiance ou tailles d'effet.

---

## H4 — Les figures sont nombreuses mais certaines sont descriptives

Plusieurs légendes emploient des formulations prudentes telles que :

* "suggests"
* "appears"
* "should be interpreted..."



C'est scientifiquement prudent, mais cela traduit aussi une validation encore limitée.

---

## H5 — Plusieurs références très récentes sont des prépublications arXiv

Une partie de la bibliographie 2025–2026 correspond à des prépublications arXiv. 

Avant une soumission, il est recommandé de privilégier des articles évalués par les pairs lorsque c'est possible.

---

## H6 — Peu de comparaison avec l'état de l'art récent

La revue de littérature présente plusieurs familles de travaux, mais le manuscrit gagnerait à comparer plus explicitement MARTHR avec les méthodes multi-objectifs et adaptatives les plus récentes. 

---

## H7 — Résultats limités aux simulations

Le manuscrit indique lui-même qu'aucune validation sur banc d'essai réel n'a été réalisée. 

---

## H8 — Pas d'analyse de complexité

Il manque une analyse du coût :

* mémoire,
* temps,
* complexité algorithmique,
* surcharge de calcul.

---

# Anomalies moyennes

* Abstract assez dense ; vérifier qu'il respecte bien la longueur visée.
* Ajouter une notation mathématique récapitulative.
* Ajouter un tableau des paramètres de simulation.
* Détailler les paramètres du simulateur.
* Ajouter des intervalles de confiance.
* Ajouter une étude de sensibilité des poids α.
* Développer davantage la comparaison avec RPL.
* Mieux expliquer la justification des coefficients.
* Ajouter une analyse de coût énergétique théorique.
* Renforcer la discussion des limites.
* Ajouter une section "Threats to Validity".

---

# Bibliographie

## Points positifs

Les références historiques majeures sont présentes :

* CORE
* CONFIDANT
* AODV
* DSR
* RPL
* HEED



## Points à vérifier

Certaines références récentes sont des prépublications arXiv (2025–2026). Avant soumission, il serait utile de vérifier :

* leur publication éventuelle dans une conférence ou une revue ;
* l'exactitude des DOI (non visibles dans le PDF).

---

# Figures

Le manuscrit contient un nombre important de figures (jusqu'à la Figure 16), ce qui constitue un point positif.  

À partir du PDF seul, je ne peux toutefois pas vérifier :

* si elles proviennent effectivement des scripts ;
* si elles sont générées automatiquement ;
* si elles utilisent les données réelles des CSV ;
* si elles contiennent des valeurs codées en dur.

Ces vérifications nécessitent l'accès au code et aux données.

# Originalité scientifique

Le concept consistant à combiner :

* confiance,
* énergie,
* QoS,
* adaptation contextuelle,

est pertinent et constitue une contribution identifiable. 

En revanche, le manuscrit gagnerait à mettre davantage en évidence ce qui distingue MARTHR des approches multi-critères existantes. Une comparaison plus explicite avec les travaux les plus proches renforcerait la démonstration de nouveauté.

Concernant le **plagiat**, il n'est pas possible de conclure à partir du seul PDF. Une vérification fiable nécessite un logiciel spécialisé (par exemple iThenticate ou Turnitin). Je peux toutefois, si vous le souhaitez, relire le texte pour identifier les passages qui gagneraient à être reformulés afin d'améliorer leur originalité rédactionnelle.

# Évaluation finale

| Critère                           | Note (/10) |
| --------------------------------- | ---------: |
| Originalité                       |        8.5 |
| Qualité scientifique              |        7.5 |
| Implémentation décrite            |        8.5 |
| Expérimentation                   |        6.5 |
| Reproductibilité documentée       |        7.0 |
| Bibliographie                     |        7.5 |
| Qualité rédactionnelle            |        8.5 |
| Préparation à une soumission IEEE |        7.5 |

**Verdict :** le manuscrit présente une base solide et une contribution intéressante, mais il nécessite une **révision majeure** avant une soumission IEEE. Les priorités sont de renforcer la validation expérimentale, d'améliorer la comparaison avec l'état de l'art, de compléter l'analyse statistique, de corriger les incohérences de structure (notamment la double section « Protocol Design ») et de consolider la bibliographie récente.

