# SmbMath

<p align="center">
    <a href='https://www.smb33.fr/' target='_blank'><img src="./src/icons/logo.svg"  width="120"></a>
</p>

Extension LibreOffice Writer : Outils mathématiques pour l'Ensemble Scolaire Sainte-Marie Bastide à Bordeaux.

> **Attention** : cette extension est expérimentale, conservez une copie de vos documents avant de l'utiliser. Le créateur ne peut être tenu responsable de la perte de données.

## Installation

1. Télécharger la dernière version : [smbmath.oxt](https://github.com/obook/SmbMath/raw/main/smbmath.oxt)
2. Dans LibreOffice Writer, menu **Outils > Gestionnaire des extensions**
3. Cliquer sur **Ajouter** et sélectionner le fichier `smbmath.oxt`
4. Redémarrer LibreOffice

Télécharger LibreOffice : [en anglais](https://www.libreoffice.org/download/) | [en français](https://fr.libreoffice.org/download/telecharger-libreoffice/)

## Fonctionnalités

Un menu **SmbMath** est ajouté dans la barre de menus de Writer avec :

- **Insérer Formule** : ouvre l'éditeur StarMath
- **Formulaires** : insertion rapide de formules prédéfinies (voir ci-dessous)
- **Synchroniser** : applique une police, une taille et des paramètres uniformes à toutes les formules du document
- **Options** : choix du mode d'insertion (texte ou objet OLE)

### Formules disponibles

| Formule | Description |
|---------|-------------|
| Angle | Notation d'angle `widehat{ABC}` |
| Comparaison | Inégalités |
| Ensembles | Ensembles de nombres N, Z, D, Q, R, C |
| Equivalence | Double flèche `A <=> B` |
| Exposant | Mise en exposant `A^B` |
| Expression | Expression avec retour à la ligne |
| Fonction | Notation fonction `f:x -> 2x+3` |
| Fraction | Fraction `a/b` |
| Fraction en ligne | Fraction en ligne (taille réduite) |
| Implication | Flèche d'implication `A => B` |
| Indice | Mise en indice `A_B` |
| Opérations | Addition, soustraction, multiplication, division |
| Racine carrée | Racine carrée `sqrt(a)` |
| Relation | Appartenance, non-appartenance, complémentaire |
| Système | Système d'équations |
| Vecteur | Notation vecteur `vec{AB}` |
| Vecteur Coordonnées | Vecteur avec coordonnées |

### Synchronisation

L'outil de synchronisation permet d'uniformiser toutes les formules OLE d'un document :
- Police (par défaut : **CMU Serif**)
- Taille de police
- Taille relative des exposants/indices (%)
- Taille relative des limites (%)

La police **CMU Serif** (Computer Modern) est recommandée. Elle peut être téléchargée sur [checkmyworking.com](https://www.checkmyworking.com/cm-web-fonts/).

## Capture d'écran

<p align="center">
    <img src="./media/Screenshot_20230809_121126.png"  width="400">
</p>

## Licence

[GNU General Public License v3](./src/registration/license.txt)
