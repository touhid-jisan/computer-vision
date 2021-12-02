# import the necessary packages
import numpy as np
import imutils
import cv2


def template_scale(template_path, imgae_path):
	template = cv2.imread(template_path)
	template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	tH, tW = template.shape[:2]
	cv2.imshow("Template", template)
	cv2.waitKey(0)
	# loop over the images to find the template in

	# load the image, convert it to grayscale, and initialize the
	# bookkeeping variable to keep track of the matched region
	image = cv2.imread(imgae_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	
	flag = False
	for scale in np.linspace(0.2, 1.0, 20)[::-1]:
		# resize the image according to the scale, and keep track
		# of the ratio of the resizing
		resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])
		# if the resized image is smaller than the template, then break
		# from the loop
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break
		# detect edges in the resized, grayscale image and apply template
		# matching to find the template in the image
		# edged = cv2.Canny(resized, 50, 200)
		result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF_NORMED)
		print(np.amax(result))
		_, maxVal, _, maxLoc = cv2.minMaxLoc(result)
		clone = np.dstack([resized, resized, resized])
		cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),(maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
		cv2.imshow("Visualize", clone)
		cv2.waitKey(0)
		threshold = 0.9
		if np.amax(result) > threshold:
			flag = True
			
			return flag


# load the image image, convert it to grayscale, and detect edges
template_path = 'security_bar.png'
imgae_path = 'security.png'

flag = template_scale(template_path, imgae_path)
print(flag)