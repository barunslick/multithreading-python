import numpy as np
import cv2
import time
import os
import concurrent.futures
start = time.perf_counter()
path_of_image = 'Combined'
directory = os.path.join(os.getcwd(),path_of_image)
set_images = []
def make_set(image):
	try:
		img = cv2.imread(os.path.join(directory,image),cv2.IMREAD_GRAYSCALE)
		resized_img = cv2.resize(img,(60,60))
		return resized_img
	except Exception as e:
		pass	
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
	result = executor.map(make_set,os.listdir(directory))
	final = [r for r in result]
stop = time.perf_counter()
print(f'Total time took {round(stop-start,2)} secs')
