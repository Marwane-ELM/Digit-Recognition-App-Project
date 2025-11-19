# Motivations

J'ai crée ce petit projet car j'avais envie, d'une part, de **consolider mes connaissances en probabilités** et, d'autre part, de **replonger dans le beau monde de la classification d'images**. 

J'ai découvert la classification d'images durant ma première année de licence, dans un cours de Sciences des données, et cela m'avais complètement fasciné.  
J'étais émerveillé par le fait qu'on puisse manipuler une image d'un chiffre afin de d'émettre une prédiction grâce aux probabilités et au classifieur de Bayes.

Cela m'a alors poussé, d'une part, à **recoder from scratch** le classifieur de Bayes (pour des données discrètes et des données continues), et d'autre part, à entraîner 4 modèles avec scikit-learn afin de créer une petite interface graphique dans laquelle on affiche les prédictions de chaque images donénes par l'utilisateur.

Vous pouvez trouver le fichier notebook `theorie_mathematique.ipynb` contenant la **théorie mathématique** et **le code from scratch** du classifieur de Bayes (continues ou discrètes), que j'ai codé, dans le dossier `notebooks/`.

Ce projet est donc une **interface python (Tkinter) de classification d’images** basée sur **4 modèles de Machine Learning** développés grâce à `scikit-learn` (GaussianNB, MultinomialNB, BernoulliNB, KNeighborsClassifier)
  
  
# Résumé global du projet

* Vous importez des images de chiffre dans le dossier `data/Images/`
2. Vous exéctutez le script python intitulé `camera_predictions.py`, contenu dans le dossier `useful_functions/`.
3. Le script va traiter chaque image en faisant appel à d'autres scripts (utilisant des fonctions d'`opencv`)
4. Ensuite, 4 modèles entraînés vont chacun donner une prédiction de chaque image contenue dans le dossier `data/Images/`.
5. Une fenêtre va s'ouvrir en vous affichant d'une part vos images et d'autre part la prédiction donné par chacun des modèles.

Les images doivent être sur **fond blanc**, **claires**, **bien centrées** et les chiffres bien **visibles** et **gras**. Les modèles ne sont pas parfait donc **soyez indulgents** avec la qualité des prédictions. 😅 

  
  
# Installation du projet

<blockquote>
Ce dépôt utilise Git LFS  pour gérer les artefacts des modèles stockés dans `saved_models/`.
Les modèles enregistrés au format `.joblib` sont lourds et ne peuvent pas être stockés directement sur GitHub.
</blockquote>

**Voici les 4 étapes à suivre pour l'installation :**

#### 1/ Installez Git LFS sur votre machine (si vous ne l'avez pas)
``` Bash
git lfs install
```

#### 2/ Clonez le dépôt complet
``` Bash
git clone https://github.com/TonPseudo/Digit-Recognition-App-Project.git
```

#### 3/ Entrer dans le dossier `Digit-Recognition-App-Project`
``` Bash
cd Digit-Recognition-App-Project
```

#### 4/ Téléchargez les gros fichiers (modèles, données, etc.)
``` Bash
git lfs pull
```


# Création de l'environnement virtuel Python

#### 1/ Créez un environement virtuel python
``` Bash
python -m venv venv
```

#### 2/ Activer cet environnement

- Linux/MacOs :
``` Bash
source venv/bin/activate
```

- Windows :
``` Bash
venv\Scripts\activate
```

#### 3/ Installez quelques librairies nécéssaires dans l'environnement virtuel
``` Bash
pip install -r requirements.txt
```
  
  
# Exécution de l'application ***(interface Tkinter)***

#### 1. Placer vos images à classer dans :
   ``` Bash
   data/Images/
   ```

#### 2. Rendez vous dans le dossier `useful_functions/`
  ``` Bash
  cd useful_functions
  ```

#### 3. Exécuter le script python `camera_predictions.py`
  ``` Bash
  python camera_preditions.py
  ```
 **Attendez un petit peu de temps et une fenêtre de ce type s'ouvrira :**

### INSERTION IMAGES



# Arborescence de fichiers du projet 📂

``` Bash
Digit-Recognition-App-Project/
│
├── data/
│   ├── Images/               Dossier contenant les images à prédire
│   └── ...                   Autres
│
├── saved_models/             Modèles ML stockés via Git LFS (.joblib)
│
├── notebooks/                Fichiers notebooks d entraînements et de théorie mathématiques
│
├── useful_functions/         Scripts pythons (dont interface Tkinter)
│   ├── camera_predictions.py
│   └── preprocessing_utils.py
│
├── requirements.txt        Librairies utiles
├── .gitattributes          fichiers suivis par LFS
├── .gitignore
└── README.md

```
   





