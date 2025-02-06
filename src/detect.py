from cv2 import cvtColor, CascadeClassifier, COLOR_BGR2GRAY


def detectFaces(img, cascade):
    cascade = CascadeClassifier(cascade)
    gray = cvtColor(img, COLOR_BGR2GRAY)
    detecteds = cascade.detectMultiScale(gray, 1.1, 4)
    return detecteds
