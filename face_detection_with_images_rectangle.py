
import cv2
#Reading the image
img = cv2.imread("lena.jpg",1)
#Creating a cascadeClassifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#converting the img into gray image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Searching the face as rectangle cordinates
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    print(x,y,w,h)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Image",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
