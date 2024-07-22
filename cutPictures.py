import cv2
import os
import shutil


def detect_and_crop_face(image_path, output_path, face_cascade):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If no faces are detected, return False
    if len(faces) == 0:
        return False

    # Crop the first face found (you can modify this to handle multiple faces if needed)
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        cv2.imwrite(output_path, face)
        break

    return True


def process_images(input_folder, output_folder, face_cascade):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.jpeg'):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Detect and crop the face
            if detect_and_crop_face(image_path, output_path, face_cascade):
                print(f"Processed and moved: {filename}")
            else:
                print(f"No face detected in: {filename}")


def main():
    # Paths for the input and output directories
    input_folder = '../faces'
    output_folder = 'CutFaces'

    # Load OpenCV's pre-trained Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Process images
    process_images(input_folder, output_folder, face_cascade)


if __name__ == "__main__":
    main()
