## Motivations

J'ai crée ce petit projet car j'avais envie, d'une part, de consolider mes connaissances en probabilités et, d'autre part, de replonger dans le beau monde de la classification d'images. J'ai découvert la classification d'images durant ma première année de licence, dans un cours de Sciences des données, et cela m'avais complètement fasciné. 
J'étais émerveillé par le fait qu'on puisse manipuler une image d'un chiffre afin de d'émettre une prédiction grâce aux probabilités et au classifieur de Bayes.
Cela m'a alors poussé à recoder from scratch le classifieur de Bayes (pour des données discrètes et des données continues).
On peut trouver le fichier notebook `theorie_mathematique.ipynb` contenant la **théorie mathématique** et **le code from scratch** du classifieur de Bayes (continues ou discrètes) dans le dossier `notebooks/`.

Ce projet est donc une **mini application de classification d’images** basée sur **4 modèles de Machine Learning** développés grâce à `scikit-learn` (GaussianNB, MultinomialNB, BernoulliNB, KNeighborsClassifier).


## Fonctionnement du projet

1. Importer des images de chiffre dans le dossier `data/Images/`
2. Exéctuter le script python intitulé `camera_predictions.py`, contenu dans le dossier `useful_functions/`.
3. Le script va mobiliser 4 modèles entraînés qui vont chacun donner une prédiction de chaque image contenue dans le dossier `data/Images/`.
4. Une fenêtre va s'ouvrir en vous affichant d'une part vos images et d'autre part la prédiction donné par chaque modèle.



## Installation du projet dans son PC




---

## Application de Classification d'images


---

## Fonctionnement général du projet

1. **Ajoutez vos images** à classifier dans le dossier :

   ``` Console
   data/Images/
   ```



