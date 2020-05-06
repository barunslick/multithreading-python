import numpy as np
import cv2
import concurrent.futures
import os
import time
path_of_image = 'Combined' 
start = time.perf_counter()
set_images = []
directory = os.path.join(os.getcwd(),path_of_image)
for img in os.listdir(directory):
	try:
		image = cv2.imread(os.path.join(directory,img),cv2.IMREAD_GRAYSCALE)
		resized_image = cv2.resize(image,(60,60))
		set_images.append([resized_image])
	except Exception as e:
		pass	
stop = time.perf_counter()
print (f'total time of {round(stop-start,2)} seconds')                 
