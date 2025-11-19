from tensorflow.keras.datasets import mnist
import numpy as np
import os

###############################################################################################################################
# Le script crée un dossier là où il est exécuté. Donc il vaut mieux se placer dans le dossier du projet "Digits_recognition"

os.makedirs("data", exist_ok=True)
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

###########################################################################################################################################
# On a regroupe les données entre elles pour que l'entraînement de chaque algo ML utilise son propre partionnement lors du train_test_split

x = np.concatenate((X_train, X_test), axis=0)
y = np.concatenate((Y_train, Y_test), axis=0)


############################
# Vectorisation des données
x = x.reshape((len(x), len(x[0])**2))


###########################################################
# On compresse dans "mnist_prepared.npz" le X_set et le Y_set

np.savez_compressed(
    "data/mnist_prepared.npz",
    X = x,    
    Y = y
)



#############################################################
print("✅ Données MNIST sauvegardées dans le dossier 'data/'")