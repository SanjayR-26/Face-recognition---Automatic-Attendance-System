import face_recognition
import cv2
import numpy as np
import os
import threading
from datetime import datetime
import pickle
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

pickle_off = open ("datafile.txt", "rb")
data = pickle.load(pickle_off)
# print(data)
known_face_names = list(data.keys())
known_face_encodings = list(data.values())
#print(known_face_encodings)
 
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            IDname = name.split("_")
            dept = IDname[0]
            reg = IDname[1]
            _name = IDname[2]
            ID = name
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{ID},{dept},{reg},{_name},{dtString}\n')
 
def push(frame):
    now = datetime.now()
    dtString = now.strftime('%H.%M.%S')

    path = 'unknown'
    cv2.imwrite(f'{path}/{dtString}.jpg', frame)
    print('Pushed')


def recognize(frame):

    frameS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
    facesCurFrame = face_recognition.face_locations(frameS)
    encodesCurFrame = face_recognition.face_encodings(frameS,facesCurFrame)    

    if facesCurFrame:
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(known_face_encodings,encodeFace)
            faceDis = face_recognition.face_distance(known_face_encodings,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)

            y1,x2,y2,x1 = faceLoc    
            
            if faceDis[matchIndex]< 0.50:  
                name = known_face_names[matchIndex].upper()
                markAttendance(name)

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            else: 
                name = 'Unknown'
                push(frame)

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
                cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

    else:
            cv2.putText(frame,'no face found',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   
    # return cv2.imshow(previewName ,frame)
    return frame


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print ("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        rval, frame = cam.read()
        frame = recognize(frame)
        cv2.imshow(previewName, frame)

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

# Create two threads as follows
thread1 = camThread("Camera 1", 0)
thread2 = camThread("Camera 2", 1)
thread1.start()
thread2.start()