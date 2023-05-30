import cv2
img = cv2.imread("solar-system.jpg")


cv2.putText(img,
"Sun",
(100,80),
cv2.FONT_HERSHEY_COMPLEX,
2,
(0,0,255))

cv2.putText(img,
"mercury",
(110,180),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255))

cv2.putText(img,
"venus",
(190,260),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255))

cv2.putText(img,
"earth",
(280,160),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255))

cv2.putText(img,
"mars",
(370,260),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255)) 

cv2.putText(img,
"jupiter",
(500,400),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255))  

cv2.putText(img,
"saturn",
(750,350),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255))  

cv2.putText(img,
"uranus",
(950,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255)) 

cv2.putText(img,
"neptune",
(1080,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255)) 

cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
