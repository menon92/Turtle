import os

from PIL import Image
import numpy as np

def rotate_image():

	#Directory containing images you wish to convert
	input_dir = "/home/menon/Pictures"

	directories = os.listdir(input_dir) 

	index = 0
	for folder in directories:
		#Ignoring .DS_Store dir
		if folder == '.DS_Store':
			pass

		else:
			# print (folder)

			folder2 = os.listdir(input_dir + '/' + folder)
			index2 = 0

			for image in folder2:
				if image == ".DS_Store":
					pass

				else:
					try :
						im = Image.open(input_dir+"/"+folder+"/"+image) #Opening image
						
						# rotate image 90, 180, 270 degree
						angle = 90
						for i in range(0, 3):
							
							new_image = im.rotate(angle)
							angle += angle
							new_image.save(input_dir + "/" + folder + "/"  + image + str(i) + ".jpg") 
			
					except Exception as e:
						print (e)
						print ("Removing image" + image)

rotate_image()
