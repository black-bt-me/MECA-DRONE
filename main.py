#Detection person: send a pic and than track it and view %
import cv2
from ultralytics import YOLO
from deepface import DeepFace
import tkinter as tk
from tkinter import filedialog
import os

# --- 1. FONCTION DE SÉLECTION D'IMAGE ---
def select_target():
    root = tk.Tk()
    root.withdraw()
    print("OUVERTURE : Sélectionnez l'image de la personne à rechercher...")
    path = filedialog.askopenfilename(
        title="Sélectionner la cible",
        filetypes=[("Images", "*.jpg *.jpeg *.png")]
    )
    return path if path else None

# On récupère le chemin une seule fois au début
target_path = select_target()

# --- 2. CONFIGURATION IA ---
# Utilisation de YOLOv8 ou v26 selon ton fichier .pt
model = YOLO("yolo26n.pt") 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("--- SYSTÈME TACTIQUE OPÉRATIONNEL ---")
if target_path:
    print(f"Cible active : {os.path.basename(target_path)}")
else:
    print("Mode détection simple (aucune cible choisie).")

# --- 3. FONCTION DE TRAITEMENT (DÉTECTION + IDENTIFICATION) ---
def apply_tactical_styling_live(img, results, current_target):
    if not results:
        return img
    
    # YOLO renvoie une liste, on prend le premier résultat
    result = results[0]
    
    if result.boxes is None:
        return img

    for box in result.boxes:
        # Coordonnées
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Classe
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]
        
        # Style par défaut (Inconnu)
        color = (0, 255, 0) # Vert
        label = f"{class_name}"
        thickness = 1

        # --- CONDITION DE RECONNAISSANCE FACIALE ---
        # On vérifie si c'est une personne ET si on a une cible chargée
        if class_name == "person" and current_target is not None:
            try:
                # Découpe de la zone détectée pour l'analyse faciale
                person_crop = img[y1:y2, x1:x2]
                
                if person_crop.size > 0:
                    # Comparaison avec l'image cible
                    verify = DeepFace.verify(
                        img1_path=current_target, 
                        img2_path=person_crop, 
                        model_name="VGG-Face", 
                        enforce_detection=False,
                        detector_backend="opencv" # Plus rapide pour i3
                    )
                    
                    if verify["verified"]:
                        color = (0, 0, 255) # Rouge (Alerte)
                        label = "TARGET IDENTIFIED"
                        thickness = 3
                        
                        # Panneau d'information latéral (ID Card)
                        score = int((1 - verify["distance"]) * 100)
                        cv2.rectangle(img, (x2 + 5, y1), (x2 + 160, y1 + 50), (0, 0, 0), -1)
                        cv2.rectangle(img, (x2 + 5, y1), (x2 + 160, y1 + 50), color, 1)
                        cv2.putText(img, "ID: CONFIRMED", (x2 + 10, y1 + 20), 1, 0.8, (255, 255, 255), 1)
                        cv2.putText(img, f"MATCH: {score}%", (x2 + 10, y1 + 40), 1, 0.8, color, 1)
            except:
                # Si DeepFace échoue (visage trop loin ou flou), on ignore
                pass

        # Dessin de la boîte autour de la personne
        cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
        
        # Étiquette au-dessus de la boîte
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    
    return img

# --- 4. BOUCLE PRINCIPALE ---
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # L'IA analyse l'image
    # Note: On enlève stream=True pour éviter les erreurs de listes vides sur i3
    results = model.track(source=frame, persist=True, verbose=False)

    # On passe frame, résultats ET le chemin de la cible à la fonction
    frame = apply_tactical_styling_live(frame, results, target_path)

    # Affichage
    cv2.imshow("TACTICAL MONITORING", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
