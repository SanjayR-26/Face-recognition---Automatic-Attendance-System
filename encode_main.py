import os
import face_recognition
import pickle
import cv2


path = 'test_images'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
#print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeList = findEncodings(images)

# encodeList = findEncodings(images)
# #print(encodeList)

dictionary = dict(zip(classNames, encodeList))
# print(dictionary)
with open('datafile.txt', 'wb') as fh:
   pickle.dump(dictionary, fh)


print("encoding successfull")

# the file names of the the images should not have space in between -- error fixed




