# SmbMath 2.0

## Corrections de bugs

- **Icône Fraction manquante** : le noeud image de FractionInline écrasait celui de Fraction (nom dupliqué dans Addons.xcu)
- **Fonctions dupliquées** : suppression de `LoadDialog`, `GetConfigAccess` et `MakePropertyValue` en double entre MainModule et SyncModule
- **Variable globale en collision** : `PGM_INIT` partagée entre les deux modules empêchait l'initialisation des valeurs par défaut de synchronisation
- **Formule Relation** : `%bêta` corrigé en `%beta` (caractère accentué non reconnu par StarMath)
- **Propriétés invalides** : suppression des propriétés `ImageIdentifier` et `URL="XXX"` mal placées dans le sous-menu Formulaire

## Nouvelles fonctionnalités

- **Menu "À propos"** : affiche le nom de l'auteur et le numéro de version
- **Barre d'outils** : ajout de la toolbar SmbMath avec les boutons Insérer Formule, Synchroniser et Options

## Améliorations

- **Menu Formulaire trié** : les 17 formules sont désormais classées par ordre alphabétique
- **Icône Options** : remplacée par une roue crantée (au lieu d'un point d'interrogation)
- **Icônes éclaircies** : fond gris plus clair sur l'ensemble des icônes pour une meilleure lisibilité
- **Boîte de dialogue Options** : taille réduite et ajustée à son contenu
- **README enrichi** : documentation complète avec instructions d'installation, liste des formules et description des fonctionnalités

## Nettoyage du code

- Suppression du code mort (`EXPOSANT_INDICE_SIZE_PERCENT`, `LIMIT_SIZE_PERCENT`)
- `Function Synchronize` corrigée en `Sub Synchronize`
- Suppression de la variable globale `PGM_INIT` inutile dans MainModule
