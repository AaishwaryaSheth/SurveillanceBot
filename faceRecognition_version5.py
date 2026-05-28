#final firebase face detect
import os
import firebase_admin
from firebase_admin import storage
import face_recognition
import cv2 as cv
import numpy as np

from firebase_config import initialize_firebase


known_face_encodings = []
known_face_names = []


def load_known_faces():
    initialize_firebase()
    bucket = storage.bucket()  # Access the storage bucket
    blobs = bucket.list_blobs(prefix="face_recognize/known_faces")  # Access images from the specified folder in Firebase Storage
    
    for blob in blobs:
        if blob.name.endswith(".jpg"):  # Ensure we are loading only image files
            image_url = blob.public_url  # Get the public URL of the image
            image_data = cv.imdecode(np.frombuffer(blob.download_as_bytes(), np.uint8), cv.IMREAD_COLOR)  # Load image from URL
            known_face_encodings.append(face_recognition.face_encodings(image_data)[0])  # Encode the image
            print(f"Loaded face: {os.path.splitext(os.path.basename(blob.name))[0]}")  # Debug print
            known_face_names.append(os.path.splitext(os.path.basename(blob.name))[0])  # Use filename (without extension) as name

def recognize_faces_fun(video_data):
    rgb_frame = cv.cvtColor(video_data, cv.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    recognized_faces = []

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        print(f"Face encoding: {face_encoding}, Matches: {matches}")  # Debug print
        name = "naruto's bro"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        else:
            print(f"Unknown face detected: {face_encoding}")  # Debug print for unknown face
        
        recognized_faces.append((name, (top, right, bottom, left))) 

    return recognized_faces