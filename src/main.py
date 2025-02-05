import os

from cv2 import imread, imwrite

from src.detect import detectFaces
from src.utils import drawFaces


def main():
    image_path = "test_images/"
    image_list = os.listdir(image_path)

    results = []
    for image in image_list:
        print(f"Detecting faces in {image}")
        the_image = imread(image_path + image)
        faces = detectFaces(the_image)
        result = drawFaces(the_image, faces)
        results.append((image, result))

    for name, result in results:
        imwrite("test_results/result_" + name, result)


if __name__ == "__main__":
    main()
