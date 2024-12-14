import cv2
import numpy as np
import os

# Schritt 1: Bild von der Webcam aufnehmen und speichern
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Fehler: Webcam nicht gefunden oder kann nicht geöffnet werden.")
    exit()

ret, frame = cam.read()
if ret:
    image_path = "webcam_image.png"
    cv2.imwrite(image_path, frame)
    print(f"Bild erfolgreich gespeichert als {image_path}")
else:
    print("Fehler: Konnte kein Bild von der Webcam aufnehmen.")

cam.release()
cv2.destroyAllWindows()

# Schritt 2: Bild einlesen und in RGB konvertieren
image_bgr = cv2.imread(image_path)
if image_bgr is None:
    print("Fehler: Konnte das gespeicherte Bild nicht laden.")
    exit()

# Umwandlung von BGR nach RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Schritt 3: Bild auf eine Höhe von 1 Pixel zuschneiden
# Nehmen wir z.B. die erste Zeile (Zeile 0)
image_1px = image_rgb[0:1, :640]  # Höhe = 1, Breite = 640

# Schritt 4: RGB-Werte für jeden Pixel ausgeben, in ein normales Array umwandeln
rgb_values = []
for col_idx, pixel in enumerate(image_1px[0]):  # Nur eine Zeile
    # Konvertiere np.uint8-Werte zu normalen Python-Integern
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
    rgb_values.append((r, g, b))
    print(f"Pixel {col_idx}: R={r}, G={g}, B={b}")

# Benutzer gibt den Namen der Kunststoffart ein
Name = input("Kunststoffart: ")

# Erstelle eine Liste mit Name und den RGB-Werten
liste = [Name, rgb_values]

# Konvertiere die Liste in einen String, der in die Datei geschrieben wird
# Konvertiere den Namen und RGB-Werte in String-Format
rgb_str = ', '.join([f"({r:03}, {g:03}, {b:03})" for r, g, b in rgb_values])  # Formatierte RGB-Werte
liste_str = f"{Name}: {rgb_str}"


# Funktion, um in die Datei zu schreiben
def write_to_dataset(liste_str, file_name="Dataset"):
    # Überprüfen, ob die Datei existiert
    if not os.path.exists(file_name):
        # Datei erstellen
        with open(file_name, "w") as file:
            file.write("Dataset:\n")  # Optionale Header-Zeile
            print(f"Datei '{file_name}' erstellt.")

    # Daten an die Datei anhängen
    with open(file_name, "a") as file:
        file.write(liste_str + "\n")
        print(f"Daten hinzugefügt: {liste_str}")


# Beispielprogramm
if __name__ == "__main__":
    # In die Datei schreiben
    write_to_dataset(liste_str)

print("Done!")


