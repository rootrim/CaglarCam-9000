from cv2 import rectangle


def drawFaces(img, faces):
    copy = img.copy()
    for x, y, w, h in faces:
        copy = rectangle(copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return copy
