#final with fbd error
import sys
import cv2 as cv 
import numpy
import os
# Add the parent directory to the system path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from faceRecognition_version5 import load_known_faces, recognize_faces_fun
from firebase_config import initialize_firebase
from imageUpload_version3 import upload_image
from sms_send import send_sms


try:
    from sms_send import send_sms
    from faceRecognition_version5 import load_known_faces, recognize_faces_fun
except ModuleNotFoundError as e:
    print("Error importing face recognition modules:", e)
def main():
    load_known_faces()

    video_capture = cv.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, video_data = video_capture.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        recognized_faces = recognize_faces_fun(video_data)

        for name, (top, right, bottom, left) in recognized_faces:
           if name == "naruto's bro":  # Unknown face check
             cv.rectangle(video_data, (left, top), (right, bottom), (0, 0, 255), 2)
             cv.putText(video_data, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2) 
             unknown_face_image = video_data[top:bottom, left:right]

             try:
                    url = upload_image(unknown_face_image, "unknown_face_" + str(int(time.time())))
                    if url:
                        notification = f"Unknown face detected. Image URL: {url}"
                        send_sms(notification)
                    else:
                        print("Failed to upload image or generate URL.")
             except Exception as e:
                    print(f"Error handling unknown face: {e}")
           else:
              cv.rectangle(video_data, (left, top), (right, bottom), (102, 204, 255), 2)
              cv.putText(video_data, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 102, 0), 2)
              print("face trigged")
 
        cv.imshow("Video", video_data)
        key = cv.waitKey(1) & 0xFF
        if key==ord('n'):
            print("exit triggered...")
            break

    video_capture.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()