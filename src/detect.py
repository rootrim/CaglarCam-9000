from cv2 import cvtColor, CascadeClassifier, COLOR_BGR2GRAY


def detectFaces(img):
    face_cascade = CascadeClassifier("models/haarcascade_frontalface_default.xml")
    gray = cvtColor(img, COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(type(faces))
    print(type(faces[0]))
    print(type(faces[0][0]))
    return faces
