# Message pour un agent IA — Audit Global MARTHR

Voici le prompt à envoyer à un autre agent IA pour effectuer un audit global du projet MARTHR.

---

## Prompt à copier-coller

```
Tu es un expert en évaluation de projets scientifiques. Effectue un audit global du projet MARTHR situé à /home/madani/MARTHR.

## Méthodologie à suivre

Suis exactement la méthodologie décrite dans /home/madani/MARTHR/anomalies/METHODOLOGIE_EVALUATION.md.

## Instructions importantes

1. **Ne signale PAS les commentaires en français comme des erreurs** — le projet utilise le français comme langue de documentation, c'est volontaire.

2. **Ne signale PAS les noms de fichiers comme `anomalies/opencode.md` ou `conversation_opencode_vscode/`** — ce sont des artefacts du développement, pas des erreurs.

3. **Concentre-toi sur** :
   - La cohérence scientifique (code ↔ manuscrit ↔ données)
   - Les bugs dans le code
   - Les données fabriquées vs réelles
   - La reproductibilité
   - La qualité bibliographique
   - Les claims non supportés par les données

4. **Ignore** :
   - Les commentaires en français (c'est normal)
   - Les noms de dossiers d'audit (anomalies/, conversation_opencode_vscode/)
   - Les fichiers de suivi interne (MASTER_TRACKER.md, etc.)

## Étapes à suivre

1. Lis la structure du projet (find, ls)
2. Lis les documents de cadrage (README.md, MASTER_TRACKER.md)
3. Analyse le manuscrit (main.tex, main_ieee_complete.tex, main_simple.tex)
4. Examine le code source (scripts/marthr_simulator.py et tous les .py)
5. Vérifie les données (data/)
6. Vérifie la reproductibilité (essaie de lancer les scripts)
7. Évalue les figures et tableaux
8. Vérifie la bibliographie
9. Produis un rapport complet

## Format de sortie

Enregistre ton rapport dans /home/madani/MARTHR/anomalies/opencode.md avec cette structure :

```
# Audit Global MARTHR — Rapport [date]

## Résumé Exécutif
| Sévérité | Nombre |
|----------|--------|
| Critique | X |
| Haute | X |
| Moyenne | X |
| Basse | X |

## 1. Structure du projet
## 2. Manuscrit
## 3. Code source
## 4. Données
## 5. Reproductibilité
## 6. Figures
## 7. Bibliographie
## 8. Actions de correction recommandées
```

## Règles de sévérité

- **Critique** : Empêche la publication ou la reproductibilité
- **Haute** : Affaiblit significativement le projet
- **Moyenne** : À améliorer mais pas bloquant
- **Basse** : Amélioration cosmétique

## Contraintes

- Ne modifie AUCUN fichier — audit seulement
- Sois précis avec les numéros de ligne
- Justifie chaque anomalie trouvée
- Propose des actions de correction concrètes
```

---

## Comment l'utiliser

1. Ouvre une nouvelle session avec l'autre agent IA
2. Colle le prompt ci-dessus
3. L'agent doit avoir accès en lecture au dossier `/home/madani/MARTHR/`
4. Le rapport sera enregistré dans `anomalies/opencode.md`
