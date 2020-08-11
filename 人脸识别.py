import cv2 as cv

image = cv.imread("E:/1.jpg")
cv.imshow("input",image)
h,w = image.shape[:2]
detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt.xml")
faces = detector.detectMultiScale(image, scaleFactor=1.01, minNeighbors=4,minSize=(30,30), maxSize=(w//2,h//2))
for x,y,width,height in faces:
    cv.rectangle(image,(x,y),(x+width,y+height),(124,125,124),2,cv.LINE_8,0)
cv.imshow("face",image)
cv.waitKey(0)
cv.destroyAllWindows()
