import cv2 as cv

min_val = 0
max_val = 255

img = cv.imread("/home/user/Изображения/road.png", cv.IMREAD_GRAYSCALE)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# edges = cv.Canny(img, min_val, max_val)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 255, 0), 2)

cv.imshow("Binary Image", img)
cv.waitKey(0)
