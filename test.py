import cv2
image = cv2.imread(r'./test.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(image)
print "find "+format(len(faces))+" face!"
for(x,y,w,h) in faces:
    cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

cv2.imshow("Find Faces!",image)
cv2.waitKey(0)   