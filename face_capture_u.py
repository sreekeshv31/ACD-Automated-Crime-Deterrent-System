import cv2
import os
import pyrebase
print("About to take a picture.....") 

videoCaptureObject = cv2.VideoCapture(0) #Input for Video to take the snap
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("/home/pi/Desktop/picamerasnaps/newimage.jpg",frame) #Directory to save the image in jpg format
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()

print("Picture taken") #Message indicating the Picture was taken
config = {
    "apiKey": "AIzaSyAMwIKmL7b-bJd1Jgy9u4zLlNBr5gsGeYo",
    "authDomain": "pulse-rate-aac0d.firebaseapp.com",
    "databaseURL": "https://pulse-rate-aac0d.firebaseio.com",
    "projectId": "pulse-rate-aac0d",
    "storageBucket": "pulse-rate-aac0d.appspot.com",
    "messagingSenderId": "491398874108",
    "appId": "1:491398874108:web:1ca1c2c8c464e5e83e6879",
    "measurementId": "G-04JLPT9W4F"
} #Config file containing the API key for firebase and domain URL for the database
print("About upload picture")
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
path_on_cloud ="images/newimage1.jpg" #Path to cloud storage where the file have to be uploaded
path_local = "/home/pi/Desktop/picamerasnaps/newimage.jpg" #Local path where the file is saved locally
storage.child(path_on_cloud).put(path_local)
print("Uploaded successfully!!!") #Message showing the file have been uploaded


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("/home/pi/Desktop/Final_Review/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
