# # name = "ITB_84_SanjayR"
# # x = name.split("_")
# # dept = x[0]
# # Reg = x[1]
# # _name = x[2]

# while True:
#     success, img = cap.read()
#     #img = captureScreen()
#     #imgS = cv2.resize(img,(0,0),None,0.25,0.25)
#     imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     facesCurFrame = face_recognition.face_locations(imgS)
#     encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)    
#     if facesCurFrame:
#         for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
#             matches = face_recognition.compare_faces(known_face_encodings,encodeFace)
#             faceDis = face_recognition.face_distance(known_face_encodings,encodeFace)
#             #print(faceDis)
#             matchIndex = np.argmin(faceDis)
            
#             if faceDis[matchIndex]< 0.50:  
#                 name = known_face_names[matchIndex].upper()
#                 #markAttendance(name)
#             else: name = 'Unknown'
#             #print(name)
#             y1,x2,y2,x1 = faceLoc    
#             cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#             cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#             cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#     else:
#             cv2.putText(img,'no face found',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   
#     cv2.imshow('Webcam',img)
#     cv2.waitKey(1)







# import face_recognition,cv2,os,pickle
# import numpy as np

# known_face_encodings=[]
# known_face_names=[]
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# facial_encodings_folder='S:\Project\project\'

# def load_facial_encodings_and_names_from_memory():
# 	for filename in os.listdir(facial_encodings_folder):
# 		known_face_names.append(filename[:-4])
# 		with open (facial_encodings_folder+filename, 'rb') as fp:
# 			known_face_encodings.append(pickle.load(fp)[0])
            
        
# load_facial_encodings_and_names_from_memory()


# video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)


# face_locations = []
# face_encodings = []
# face_names = []
# process_this_frame = True

# while True:
# # Grab a single frame of video
#     ret, frame = video_capture.read()

# # Resize frame of video to 1/4 size for faster face recognition processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

# # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#     rgb_small_frame = small_frame[:, :, ::-1]

# # Only process every other frame of video to save time
#     if process_this_frame:
# # Find all the faces and face encodings in the current frame of video
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         face_names = []
#         for face_encoding in face_encodings:
#     # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"

#     # # If a match was found in known_face_encodings, just use the first one.
#     # if True in matches:
#     #     first_match_index = matches.index(True)
#     #     name = known_face_names[first_match_index]

#     # Or instead, use the known face with the smallest distance to the new face
#             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]

#             face_names.append(name)

#     process_this_frame = not process_this_frame


# # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
# # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

# # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

# # Draw a label with a name below the face
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# # Display the resulting image
#     cv2.imshow('Video', frame)
#     flag=-1
#     if(len(face_names)!=0):
#         count=0
#     for person in face_names:
#         if(person=='Unknown'):
#             count+=1
#     if(count==len(face_names)):
#         flag=1
#     else:
#         flag=0


# # Hit 'q' on the keyboard to quit!


#     if cv2.waitKey(1) & 0xFF==ord('q') or flag==0:
#         break

    

# # Release handle to the webcam
#     video_capture.release()
#     cv2.destroyAllWindows()



# class camThread(threading.Thread):
#     def __init__(self, previewName, camID):
#         threading.Thread.__init__(self)
#         self.previewName = previewName
#         self.camID = camID
#     def run(self):
#         print("Starting" + self.previewName)
#         camPreview(self.previewName, self.camID)

# def camPreview(previewName, camID):
#     cv2.namedWindow(previewName)
#     cam = cv2.VideoCapture(camID)
#     rval, frame = cam.read()
#     if rval:  # try to get the first frame
#         while rval:
#         success, frame = capture.read()
#         frame = captureScreen()
#         frameS = cv2.resize(frame,(0,0),None,0.25,0.25)
#             frameS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
#             facesCurFrame = face_recognition.face_locations(frameS)
#             encodesCurFrame = face_recognition.face_encodings(frameS,facesCurFrame)    

#             if facesCurFrame:
#                 for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
#                     matches = face_recognition.compare_faces(known_face_encodings,encodeFace)
#                     faceDis = face_recognition.face_distance(known_face_encodings,encodeFace)
#                     print(faceDis)
#                     matchIndex = np.argmin(faceDis)

#                     y1,x2,y2,x1 = faceLoc    
                    
#                     if faceDis[matchIndex]< 0.50:  
#                         name = known_face_names[matchIndex].upper()
#                         markAttendance(name)

#                         cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#                         cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#                         cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#                     else: 
#                         name = 'Unknown'
#                         push(frame)

#                         cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
#                         cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
#                         cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

#             else:
#                     cv2.putText(frame,'no face found',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   
#             cv2.imshow(previewName ,frame)
#             if cv2.waitKey(1) & 0xFF==ord('q'):
#                 break


#     while rval:
#         # success, frame = capture.read()
#         #frame = captureScreen()
#         #frameS = cv2.resize(frame,(0,0),None,0.25,0.25)
#         frameS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#         facesCurFrame = face_recognition.face_locations(frameS)
#         encodesCurFrame = face_recognition.face_encodings(frameS,facesCurFrame)    
#         if facesCurFrame:
#             for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
#                 matches = face_recognition.compare_faces(known_face_encodings,encodeFace)
#                 faceDis = face_recognition.face_distance(known_face_encodings,encodeFace)
#                 #print(faceDis)
#                 matchIndex = np.argmin(faceDis)
                
#                 if faceDis[matchIndex]< 0.50:  
#                     name = known_face_names[matchIndex].upper()
#                     #markAttendance(name)
#                 else: 
#                     name = 'Unknown'
#                 #print(name)
#                 y1,x2,y2,x1 = faceLoc    
#                 cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#                 cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#                 cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#         else:
#                 cv2.putText(frame,'no face found',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   
#         cv2.imshow('Webcam',frame)
        
#         if cv2.waitKey(1) & 0xFF==ord('q'):q
#             break
 
# Create two threads as follows
# thread1 = camThread("Camera 1", 0)
# thread2 = camThread("Camera 2", 1)
# thread1.start()
# thread2.start()