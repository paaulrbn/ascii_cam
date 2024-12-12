import cv2

# Fonction pour convertir une image en ASCII
def image_to_ascii(image, cols=200, scale=0.5, char_set=" .:-=+*#%@"):
    # Redimensionner l'image pour réduire la taille et la convertir en niveaux de gris
    width, height = image.shape[1], image.shape[0]
    aspect_ratio = height / width
    new_width = cols
    new_height = int(aspect_ratio * cols * scale)
    image = cv2.resize(image, (new_width, new_height))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convertir les pixels en caractères ASCII
    ascii_image = ""
    for row in image:
        for pixel in row:
            ascii_image += char_set[int(pixel / 255 * (len(char_set) - 1))]
        ascii_image += "\n"
    return ascii_image

# Paramètres de la caméra
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Convertir l'image en ASCII
    ascii_art = image_to_ascii(frame)

    # Afficher l'image ASCII dans la console
    print("\033c", end="")  # Efface la console
    print(ascii_art)

    # Appuyer sur 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra
cam.release()
cv2.destroyAllWindows()