import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from image_preprocessing import traitement
from prediction import best_model, prediction_digit

##################################################

# Import des modèles
GaussianNB = best_model("../saved_models/GaussianNB_persistent/")
MultinomialNB = best_model("../saved_models/MultinomialNB_persistent/")
BernoulliNB = best_model("../saved_models/BernoulliNB_persistent/")
KNC = best_model("../saved_models/KNC_persistent/")

# Fenêtre principale
window = tk.Tk()
window.title("Prédictions Chiffres")
window.geometry("500x1000")

# --- 1. Frame principale ---
main_frame = tk.Frame(window)
main_frame.pack(fill="both", expand=True)

# --- 2. Canvas + Scrollbar ---
canvas = tk.Canvas(main_frame)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# --- 3. Frame à l'intérieur du Canvas ---
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# --- 4. Ajustement automatique de la zone scrollable ---
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", update_scrollregion)

# --- 5. Données à afficher ---
store_images = []
path_dossier_images = "../Data/images/"

for i, nom_fichier in enumerate(os.listdir(path_dossier_images)):

    # Extensions acceptées
    extension = ("jpg", "jpeg", "png", "heic")
    if not nom_fichier.lower().endswith(extension):
        continue

    # Chargement de l'image
    path_image = os.path.join(path_dossier_images, nom_fichier)
    image = Image.open(path_image).resize((200, 200))
    image = ImageTk.PhotoImage(image)
    store_images.append(image)

    # Traitement et prédictions
    image_traitee = traitement(path_image)
    prediction_GNB = prediction_digit(GaussianNB, image_traitee)
    prediction_MNB = prediction_digit(MultinomialNB, image_traitee)
    prediction_BNB = prediction_digit(BernoulliNB, image_traitee)
    prediction_KNC = prediction_digit(KNC, image_traitee)

    # --- Bloc contenant l’image + texte ---
    bloc = tk.Frame(scrollable_frame, bd=3, relief="groove", padx=10, pady=10)
    bloc.pack(fill="x", pady=10, padx=20)

    # Image à gauche
    lbl_image = tk.Label(bloc, image=image)
    lbl_image.grid(row=0, column=0, rowspan=4, padx=20)

    # Texte à droite
    lbl_gnb = tk.Label(bloc, text=f"GaussianNB : {prediction_GNB[0]}", anchor="w")
    lbl_mnb = tk.Label(bloc, text=f"MultinomialNB : {prediction_MNB[0]}", anchor="w")
    lbl_bnb = tk.Label(bloc, text=f"BernoulliNB : {prediction_BNB[0]}", anchor="w")
    lbl_knc = tk.Label(bloc, text=f"KNeighborsClassifier : {prediction_KNC[0]}", anchor="w")

    lbl_gnb.grid(row=0, column=1, sticky="w")
    lbl_mnb.grid(row=1, column=1, sticky="w")
    lbl_bnb.grid(row=2, column=1, sticky="w")
    lbl_knc.grid(row=3, column=1, sticky="w")


#### Scroll souris

def _on_mousewheel(event):
    if window.tk.call("tk", "windowingsystem") == "aqua":  # macOS
        canvas.yview_scroll(int(-1 * event.delta), "units")
    else:  # Windows / Linux
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def _on_linux_scroll(event):
    if event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")
        
canvas.bind_all("<MouseWheel>", _on_mousewheel)   # windows ou macOS
canvas.bind_all("<Button-4>", _on_linux_scroll)   # Linux scroll up
canvas.bind_all("<Button-5>", _on_linux_scroll)   # Linux scroll down

# Exécution
window.mainloop()
