## Motivations

J'ai crée ce petit projet car j'avais envie, d'une part, de consolider mes connaissances en probabilités et, d'autre part, de replonger dans le beau monde de la classification d'images. 

J'ai découvert la classification d'images durant ma première année de licence, dans un cours de Sciences des données, et cela m'avais complètement fasciné. 
J'étais émerveillé par le fait qu'on puisse manipuler une image d'un chiffre afin de d'émettre une prédiction grâce aux probabilités et au classifieur de Bayes.
Cela m'a alors poussé à **recoder from scratch** le classifieur de Bayes (pour des données discrètes et des données continues).

On peut trouver le fichier notebook `theorie_mathematique.ipynb` contenant la **théorie mathématique** et **le code from scratch** du classifieur de Bayes (continues ou discrètes) dans le dossier `notebooks/`.
Ce projet est donc une **mini application de classification d’images** basée sur **4 modèles de Machine Learning** développés grâce à `scikit-learn` (GaussianNB, MultinomialNB, BernoulliNB, KNeighborsClassifier).


## Fonctionnement rapide du projet

1. Vous importez des images de chiffre dans le dossier `data/Images/`
2. Vous exéctutez le script python intitulé `camera_predictions.py`, contenu dans le dossier `useful_functions/`.
3. Le script va mobiliser 4 modèles entraînés qui vont chacun donner une prédiction de chaque image contenue dans le dossier `data/Images/`.
4. Une fenêtre va s'ouvrir en vous affichant d'une part vos images et d'autre part la prédiction donné par chaque modèle.



## Installation du projet complet 

<blockquote>
Ce dépôt utilise Git LFS  pour gérer les artefacts de modèles stockés dans `saved_models/`.
Les modèles enregistrés au format `.joblib` sont lourds et ne peuvent pas être stockés directement sur GitHub.
</blockquote>

**Voici les 4 étapes à suivre pour l'installation :**

#### 1/ Installez Git LFS sur votre machine
``` Bash
git lfs install
```

#### 2/ Clonez le dépôt complet
``` Bash
git clone https://github.com/TonPseudo/Digit-Recognition-App-Project.git
```

#### 3/ Entrer dans le dossier
``` Bash
cd Digit-Recognition-App-Project
```

#### 4/ Téléchargez les gros fichiers (modèles, données, etc.)
``` Bash
git lfs pull
```


## Création de l'environnement Python


#### 1/ Créez un environement virtuel python
``` Bash
python -m venv venv
```

#### 2/ Activer cet environnement

- Linux/MacOs :
``` Bash
python -m venv venv
```

- Windows :
``` Bash
venv\Scripts\activate
```

#### 3/ Installez quelques librairies nécéssaires dans l'environnement virtuel
``` Bash
pip install -r requirements.txt
```


