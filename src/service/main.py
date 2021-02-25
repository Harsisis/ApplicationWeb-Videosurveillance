import urllib
import cv2
import numpy as np
import time
import urllib.request

url = 'http://192.168.68.103:8080/photo.jpg'

while True:
  imgResp = urllib.request.urlopen(url)
  imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
  img = cv2.imdecode(imgNp, -1)

  cv2.imshow('IPWebcam', img)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
