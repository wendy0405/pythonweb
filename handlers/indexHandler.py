# base handler
import tornado.web
import cv2
import os
class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        upload_path = os.path.join(os.path.dirname(__file__),'files')
        file_metas = self.request.files.get('file')
        for meta in file_metas:
            filepath = os.path.join(upload_path,'files.jpg')
            with open(filepath,'wb') as up:      
                up.write(meta['body'])
                print "finsh save"
        image = cv2.imread(filepath)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_alt2.xml')
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.10,
            minNeighbors = 5,
            minSize = (5,5),
            # flags = cv2.CV_HAAR_SCALE_IMAGE
          )
        print "find "+format(len(faces))+" face!"
        for(x,y,w,h) in faces:
            cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

        cv2.imshow("Find Faces!",image)
        cv2.waitKey(0)      

# routers    
routers = [
    (r"/index",IndexHandler)
]