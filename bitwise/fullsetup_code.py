# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import cv2

def plt_imshow(title, image):
	# convert the image frame BGR to RGB color space and display it
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.imshow(image)
	plt.title(title)
	plt.grid(False)
	plt.show()

# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
plt_imshow("Rectangle", rectangle)

# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
plt_imshow("Circle", circle)

# a bitwise 'AND' is only 'True' when both inputs have a value that
# is "ON' -- in this case, the cv2.bitwise_and function examines
# every pixel in the rectangle and circle; if *BOTH* pixels have a
# value greater than zero then the pixel is turned 'ON (i.e., 255)
# in the output image; otherwise, the output value is set to
# 'OFF' (i.e., 0)
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
plt_imshow("AND", bitwiseAnd)

# a bitwise 'OR' examines every pixel in the two inputs, and if
# *EITHER* pixel in the rectangle or circle is greater than zero,
# then the output pixel has a value of 255, otherwise it is 0
bitwiseOr = cv2.bitwise_or(rectangle, circle)
plt_imshow("OR", bitwiseOr)

# the bitwise 'XOR' is identical to the 'OR' function, with one
# exception: both the rectangle and circle are not allowed to *BOTH*
# have values greater than 0 (only one can be 0)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
plt_imshow("XOR", bitwiseXor)

# finally, the bitwise 'NOT' inverts the values of the pixels; pixels
# with a value of 255 become 0, and pixels with a value of 0 become
# 255
bitwiseNot = cv2.bitwise_not(circle)
plt_imshow("NOT", bitwiseNot)